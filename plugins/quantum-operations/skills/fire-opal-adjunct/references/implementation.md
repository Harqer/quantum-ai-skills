# Fire Opal adjunct: implementation reference

Fire Opal is a present-day real-hardware error-suppression execution layer. Keep QEC and FTQC logical-resource requirements in their dedicated fault-tolerant models.

API checked against Q-CTRL Fire Opal documentation in September 2026.

## Install

~~~text
pip install fire-opal qiskit
~~~

Pin a tested version in a production environment and record it with results.

## Authenticate through environment-managed credentials

~~~python
import os
import fireopal as fo

fo.authenticate_qctrl_account(
    api_key=os.environ["QCTRL_API_KEY"],
)
~~~

For IBM Cloud:

~~~python
credentials = fo.credentials.make_credentials_for_ibm_cloud(
    token=os.environ["IBM_CLOUD_API_KEY"],
    instance=os.environ["IBM_QUANTUM_CRN"],
)
~~~

For Amazon Braket/IonQ, use make_credentials_for_braket with an authorized IAM role ARN from the environment/configuration.

## Discover supported devices

~~~python
devices = fo.show_supported_devices(
    credentials=credentials,
)["supported_devices"]

if not devices:
    raise RuntimeError("No accessible Fire Opal-supported devices")
~~~

Select backend_name from the returned supported-device set at execution time.

Current documented provider coverage includes cloud-accessible IBM Quantum Platform devices and IonQ systems through Amazon Braket.

## Convert a circuit

~~~python
from qiskit import qasm3

circuit_qasm = qasm3.dumps(qc)
~~~

Fire Opal execute accepts QASM 2 or 3 strings.

## Validate before hardware execution

~~~python
validation = fo.validate(
    circuits=[circuit_qasm],
    credentials=credentials,
    backend_name=backend_name,
)

errors = validation.get("results", [])
warnings = validation.get("warnings", [])

if errors:
    raise RuntimeError(
        f"Fire Opal validation failed: {errors}"
    )
~~~

Use validation as the non-metered compatibility gate and submit hardware jobs after validation succeeds.

## Execute

~~~python
job = fo.execute(
    circuits=[circuit_qasm],
    shot_count=shot_count,
    credentials=credentials,
    backend_name=backend_name,
)
~~~

execute returns a FireOpalJob immediately.

Retrieve:

~~~python
result = job.result()
~~~

Result payload formats can evolve; consume documented keys for the installed version and preserve the raw result alongside parsed metrics.

## Repeated submissions

For repeated workloads where documented/current support applies, Fire Opal exposes iterate rather than repeatedly invoking independent execute jobs.

If iterate is used, ensure stop_iterate is called when the session is complete.

## FTQC boundary

Record Fire Opal improvements as present-day hardware metrics, while the following FTQC quantities continue to come from the fault-tolerant models:
- fewer logical qubits;
- lower required code distance;
- removal of magic-state factories;
- proof of logical fault tolerance;
- claim that an over-wide circuit now fits hardware.

Keep Fire Opal metrics in a separate present-day-hardware result record:

~~~text
backend
shots
raw/mitigated result metrics
validation warnings
Fire Opal version
provider job IDs / metadata
~~~

Sources:
- https://docs.q-ctrl.com/references/fire-opal/fireopal
- https://docs.q-ctrl.com/references/fire-opal/fireopal/fireopal.validate.html
- https://docs.q-ctrl.com/references/fire-opal/fireopal/fireopal.execute
