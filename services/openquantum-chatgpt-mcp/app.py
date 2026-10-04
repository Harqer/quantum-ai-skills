from __future__ import annotations

import dataclasses
import os
import time
from datetime import date, datetime
from enum import Enum
from typing import Any

from mcp.server import MCPServer
from mcp.server.transport_security import TransportSecuritySettings
from mcp.types import ToolAnnotations
from openquantum_sdk.auth import ClientCredentials, ClientCredentialsAuth
from openquantum_sdk.clients import ManagementClient, SchedulerClient
from openquantum_sdk.models import JobCreate, JobPreparationCreate

SERVER_NAME = "Open Quantum ChatGPT Bridge"
MAX_CREDITS = float(os.getenv("OPENQUANTUM_MCP_MAX_CREDITS", "2"))
MAX_SHOTS = int(os.getenv("OPENQUANTUM_MCP_MAX_SHOTS", "128"))

mcp = MCPServer(
    SERVER_NAME,
    instructions=(
        "Use Open Quantum's official SDK lifecycle. Discover a backend before work. "
        "Always prepare a job and review the quote before any submission. "
        "submit_prepared_job is intentionally locked to one server-allowlisted "
        "preparation ID and requires explicit spend confirmation for non-zero cost."
    ),
)


def _clients() -> tuple[SchedulerClient, ManagementClient]:
    client_id = os.environ.get("OPENQUANTUM_CLIENT_ID")
    client_secret = os.environ.get("OPENQUANTUM_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise RuntimeError("Open Quantum credentials are not configured on the server.")
    auth = ClientCredentialsAuth(
        creds=ClientCredentials(client_id=client_id, client_secret=client_secret)
    )
    management = ManagementClient(auth=auth)
    scheduler = SchedulerClient(auth=auth, management_client=management)
    return scheduler, management


def _plain(value: Any) -> Any:
    if dataclasses.is_dataclass(value):
        return _plain(dataclasses.asdict(value))
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(v) for v in value]
    if hasattr(value, "__dict__"):
        return {
            k: _plain(v)
            for k, v in vars(value).items()
            if not k.startswith("_")
        }
    return value


def _organization_id(management: ManagementClient, requested: str | None) -> str:
    if requested:
        return requested
    result = management.list_user_organizations(limit=20)
    organizations = list(getattr(result, "organizations", []) or [])
    if not organizations:
        raise RuntimeError("No Open Quantum organization is available for this SDK key.")
    if len(organizations) > 1:
        raise RuntimeError(
            "Multiple organizations are available; pass organization_id explicitly."
        )
    return organizations[0].id


def _quote_summary(preparation_result: Any) -> list[dict[str, Any]]:
    summary: list[dict[str, Any]] = []
    for plan in getattr(preparation_result, "quote", []) or []:
        priorities = []
        base = float(getattr(plan, "price", 0) or 0)
        for priority in getattr(plan, "queue_priorities", []) or []:
            increase = float(getattr(priority, "price_increase", 0) or 0)
            priorities.append(
                {
                    "name": getattr(priority, "name", None),
                    "queue_priority_id": getattr(priority, "queue_priority_id", None),
                    "price_increase": increase,
                    "total_credits": base + increase,
                }
            )
        summary.append(
            {
                "name": getattr(plan, "name", None),
                "execution_plan_id": getattr(plan, "execution_plan_id", None),
                "base_credits": base,
                "queue_priorities": priorities,
            }
        )
    return summary


def _selected_cost(
    preparation_result: Any, execution_plan_id: str, queue_priority_id: str
) -> float:
    for plan in getattr(preparation_result, "quote", []) or []:
        if getattr(plan, "execution_plan_id", None) != execution_plan_id:
            continue
        base = float(getattr(plan, "price", 0) or 0)
        for priority in getattr(plan, "queue_priorities", []) or []:
            if getattr(priority, "queue_priority_id", None) == queue_priority_id:
                return base + float(getattr(priority, "price_increase", 0) or 0)
    raise ValueError("The requested execution plan / queue priority is not in this quote.")


@mcp.tool(
    title="List Open Quantum backends",
    annotations=ToolAnnotations(read_only_hint=True, open_world_hint=False),
)
def list_backends(limit: int = 50) -> dict[str, Any]:
    """List backend classes visible to the configured Open Quantum account."""
    _, management = _clients()
    result = management.list_backend_classes(limit=max(1, min(limit, 100)))
    return {
        "backends": [_plain(x) for x in (getattr(result, "backend_classes", []) or [])],
        "pagination": _plain(getattr(result, "pagination", None)),
    }


@mcp.tool(
    title="Get Open Quantum backend",
    annotations=ToolAnnotations(read_only_hint=True, open_world_hint=False),
)
def get_backend(backend_class_id: str) -> dict[str, Any]:
    """Get one backend's live details, including constraint_data when available."""
    scheduler, _ = _clients()
    return _plain(scheduler.get_backend_class(backend_class_id))


@mcp.tool(
    title="Prepare Open Quantum job",
    annotations=ToolAnnotations(
        read_only_hint=False, destructive_hint=False, open_world_hint=False
    ),
)
def prepare_job(
    qasm: str,
    backend_class_id: str = "rigetti:cepheus-1-108q",
    shots: int = 10,
    name: str = "ChatGPT Open Quantum test",
    organization_id: str | None = None,
    job_subcategory_id: str = "oth:oth",
    input_format: str = "qasm",
    timeout_seconds: int = 45,
) -> dict[str, Any]:
    """Upload circuit text and obtain Open Quantum validation plus a quote. This does not create a QPU job or spend credits."""
    if not qasm.strip():
        raise ValueError("qasm must not be empty")
    if shots < 1 or shots > MAX_SHOTS:
        raise ValueError(f"shots must be between 1 and {MAX_SHOTS}")

    scheduler, management = _clients()
    org_id = _organization_id(management, organization_id)
    upload_id = scheduler.upload_job_input(file_content=qasm.encode("utf-8"))
    prep = scheduler.prepare_job(
        JobPreparationCreate(
            organization_id=org_id,
            backend_class_id=backend_class_id,
            name=name,
            upload_endpoint_id=upload_id,
            job_subcategory_id=job_subcategory_id,
            shots=shots,
            input_format=input_format,
            configuration_data={},
        )
    )

    deadline = time.monotonic() + max(1, min(timeout_seconds, 60))
    result = scheduler.get_preparation_result(prep.id)
    while getattr(result, "status", None) not in ("Completed", "Failed"):
        if time.monotonic() >= deadline:
            break
        time.sleep(1)
        result = scheduler.get_preparation_result(prep.id)

    return {
        "preparation_id": prep.id,
        "status": getattr(result, "status", None),
        "message": getattr(result, "message", None),
        "backend_class_id": backend_class_id,
        "organization_id": org_id,
        "shots": shots,
        "quote_summary": _quote_summary(result),
        "submission_enabled": os.getenv("OPENQUANTUM_ENABLE_SUBMIT", "").lower()
        in ("1", "true", "yes"),
        "hard_credit_cap": MAX_CREDITS,
    }


@mcp.tool(
    title="Get Open Quantum preparation",
    annotations=ToolAnnotations(read_only_hint=True, open_world_hint=False),
)
def get_preparation(preparation_id: str) -> dict[str, Any]:
    """Fetch a preparation's current validation status and quote."""
    scheduler, _ = _clients()
    result = scheduler.get_preparation_result(preparation_id)
    return {
        "preparation_id": preparation_id,
        "status": getattr(result, "status", None),
        "message": getattr(result, "message", None),
        "quote_summary": _quote_summary(result),
        "hard_credit_cap": MAX_CREDITS,
    }


@mcp.tool(
    title="Submit prepared Open Quantum job",
    annotations=ToolAnnotations(
        read_only_hint=False, destructive_hint=True, open_world_hint=False
    ),
)
def submit_prepared_job(
    preparation_id: str,
    execution_plan_id: str,
    queue_priority_id: str,
    confirm_spend: bool = False,
) -> dict[str, Any]:
    """Create a real Open Quantum job from an already prepared quote. Server-side allowlisting and the credit cap are mandatory."""
    enabled = os.getenv("OPENQUANTUM_ENABLE_SUBMIT", "").lower() in ("1", "true", "yes")
    allowed = os.getenv("OPENQUANTUM_ALLOWED_PREPARATION_ID", "")
    if not enabled:
        raise PermissionError("QPU submission is disabled on this server.")
    if not allowed or preparation_id != allowed:
        raise PermissionError(
            "This preparation_id is not server-allowlisted for submission."
        )

    scheduler, _ = _clients()
    prep_result = scheduler.get_preparation_result(preparation_id)
    if getattr(prep_result, "status", None) != "Completed":
        raise RuntimeError(
            f"Preparation is not Completed: {getattr(prep_result, 'status', None)}"
        )

    cost = _selected_cost(prep_result, execution_plan_id, queue_priority_id)
    if cost > MAX_CREDITS:
        raise PermissionError(
            f"Quoted cost {cost} credits exceeds hard cap {MAX_CREDITS}."
        )
    if cost > 0 and not confirm_spend:
        raise PermissionError(
            f"This job costs {cost} credits. Re-call with confirm_spend=true only after explicit user approval."
        )

    job = scheduler.create_job(
        JobCreate(
            job_preparation_id=preparation_id,
            execution_plan_id=execution_plan_id,
            queue_priority_id=queue_priority_id,
        )
    )
    return {
        "job": _plain(job),
        "charged_quote_credits": cost,
        "note": "Disable OPENQUANTUM_ENABLE_SUBMIT after the intended job is created.",
    }


@mcp.tool(
    title="Get Open Quantum job",
    annotations=ToolAnnotations(read_only_hint=True, open_world_hint=False),
)
def get_job(job_id: str) -> dict[str, Any]:
    """Fetch the current state of one Open Quantum job."""
    scheduler, _ = _clients()
    return _plain(scheduler.get_job(job_id))


@mcp.tool(
    title="Get Open Quantum job results",
    annotations=ToolAnnotations(read_only_hint=True, open_world_hint=False),
)
def get_job_results(job_id: str) -> dict[str, Any]:
    """Download the result JSON for a completed Open Quantum job."""
    scheduler, _ = _clients()
    job = scheduler.get_job(job_id)
    return {
        "job_id": job_id,
        "status": getattr(job, "status", None),
        "result": _plain(scheduler.download_job_output(job)),
    }


@mcp.tool(
    title="Get Open Quantum job calibration",
    annotations=ToolAnnotations(read_only_hint=True, open_world_hint=False),
)
def get_job_calibration(job_id: str) -> dict[str, Any]:
    """Download calibration tagged to a completed job, when Open Quantum provides it."""
    scheduler, _ = _clients()
    job = scheduler.get_job(job_id)
    if not getattr(job, "calibration_data_url", None):
        return {
            "job_id": job_id,
            "status": getattr(job, "status", None),
            "calibration_available": False,
        }
    return {
        "job_id": job_id,
        "status": getattr(job, "status", None),
        "calibration_available": True,
        "calibration": _plain(scheduler.download_job_calibration(job)),
    }


def _transport_security() -> TransportSecuritySettings:
    hosts = {
        "localhost",
        "localhost:*",
        "127.0.0.1",
        "127.0.0.1:*",
    }
    for key in ("VERCEL_URL", "VERCEL_PROJECT_PRODUCTION_URL", "MCP_PUBLIC_HOST"):
        value = (os.getenv(key) or "").strip()
        if value:
            value = value.removeprefix("https://").removeprefix("http://").rstrip("/")
            hosts.add(value)
            hosts.add(f"{value}:*")
    return TransportSecuritySettings(allowed_hosts=sorted(hosts))


app = mcp.streamable_http_app(
    json_response=True,
    stateless_http=True,
    transport_security=_transport_security(),
)
