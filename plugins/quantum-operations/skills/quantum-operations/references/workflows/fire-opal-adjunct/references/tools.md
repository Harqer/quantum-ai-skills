# Fire Opal API map

Official docs: https://docs.q-ctrl.com/fire-opal

## Core

| Need | API |
| --- | --- |
| Q-CTRL login | `authenticate_qctrl_account(api_key=...)` |
| Organization | `fo.config.configure_organization(...)` |
| IBM credentials | `make_credentials_for_ibm_cloud(token, instance)` |
| Braket credentials | `make_credentials_for_braket(arn)` |
| Devices | `show_supported_devices(credentials)` |
| Compatibility gate | `validate(circuits, credentials, backend_name)` |
| One job | `execute(...)` |
| Repeated jobs | `iterate(...)` |
| Observable job | `estimate_expectation(...)` |
| Repeated observable jobs | `iterate_expectation(...)` |
| Release iterative session | `stop_iterate(credentials, backend_name)` |
| Managed QAOA | `solve_qaoa(...)` |
| Many-body dynamics | `simulate_dynamics(...)` |
| Monte Carlo | `integrate_monte_carlo(...)` |
| History | `activity_monitor(...)` |
| Metadata | `get_action_metadata(...)` |
| Recover result | `get_result(action_id)` |
| Versions | `print_package_versions()` |

## Limits and behavior

- Real hardware execution; simulators are not supported by Fire Opal.
- Maximum 300 circuits/parameter dictionaries per job.
- Maximum 40 concurrent jobs.
- OpenQASM 2/3 circuit input.
- Virtual-qubit circuits only; Fire Opal chooses physical layout.
- `execute` supports multiple classical registers.
- Current public provider docs: IBM Quantum Platform and IonQ through Amazon Braket.
- Fire Opal's free tier documents 10 calls per Fire Opal function per user per day; verify the account's current plan before relying on that limit.
- Retrieve results through Fire Opal to retain its post-processing.

## Current IBM-specific options

~~~python
IbmRunOptions(
    session_id=None,
    job_tags=None,
    reduce_approximation=False,
)
~~~

Use `reduce_approximation=True` when near-identity rotations must survive optimization.

## QASM requirements

Supported circuits require measurements, a quantum register, and supported gates. For `execute`, at least one classical register is required; other circuit-execution APIs currently require exactly one classical register.

Current gate list includes common one-qubit rotations/Cliffords, CX/CY/CZ, SWAP, RXX/RZZ, controlled rotations/U gates, CCX, CSWAP, barrier, and measurement. Check the live circuit-requirements page before generating provider workloads.

## Version note

A current Q-CTRL mid-circuit-measurement notebook reports `fire-opal 9.0.2`, but production code should pin the version actually installed and use `print_package_versions()`; documentation follows semantic versioning and can advance independently.


## Alternate integration surfaces

Use these only when the surrounding platform is already part of the workload:

- IBM Premium: Qiskit Functions **Performance Management** exposes the same suppression class as Fire Opal `execute/iterate`; **Optimization Solver** mirrors the managed QAOA workflow.
- qBraid: beta Fire Opal integration; Q-CTRL API-key authentication is still required.
- Wolfram Quantum Framework: enable Fire Opal during hardware execution with the framework's Fire Opal option.
- QCentroid: configure Fire Opal as an authenticated provider/backend.
- Aqarios Luna: `QAOA_FO`/Q-CTRL provider paths wrap Fire Opal.

For direct Python integrations, prefer the `fireopal` package because its action IDs, validation, sessions, result recovery, run options, and specialized solvers are explicit.
