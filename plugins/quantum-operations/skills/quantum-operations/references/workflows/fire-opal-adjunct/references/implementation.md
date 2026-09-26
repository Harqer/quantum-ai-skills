# Fire Opal implementation

API checked against Q-CTRL documentation, September 2026.

## Setup

~~~bash
pip install fire-opal qiskit
~~~

~~~python
import os
import fireopal as fo

fo.authenticate_qctrl_account(
    api_key=os.environ["QCTRL_API_KEY"]
)
~~~

For multiple Q-CTRL organizations:

~~~python
fo.config.configure_organization(
    organization_slug=os.environ["QCTRL_ORG_SLUG"]
)
~~~

Q-CTRL authentication is separate from QPU credentials.

### IBM Quantum

~~~python
credentials = fo.credentials.make_credentials_for_ibm_cloud(
    token=os.environ["IBM_CLOUD_API_KEY"],
    instance=os.environ["IBM_QUANTUM_CRN"],
)
~~~

### IonQ through Amazon Braket

~~~python
credentials = fo.credentials.make_credentials_for_braket(
    arn=os.environ["AWS_BRAKET_ROLE_ARN"]
)
~~~

## Backend discovery

~~~python
devices = fo.show_supported_devices(credentials)
backend_name = devices["supported_devices"][0]
~~~

Resolve this at runtime. Current public documentation covers cloud-accessible IBM Quantum devices and IonQ through Amazon Braket.

## Circuit contract

Execution functions accept OpenQASM 2 or 3 strings.

For Qiskit:

~~~python
from qiskit import qasm3
qasm = qasm3.dumps(qc)
~~~

Requirements:
- at least one quantum register and measurement;
- `execute` supports multiple classical registers;
- other execution functions currently require one classical register;
- use virtual qubits; physical-qubit addressing is rejected;
- stay within the documented Fire Opal gate set and backend width.

Parameterized circuits use unbound QASM 3 plus `parameters`. Prefer this over regenerating circuits because it reduces preprocessing.

## Validate before QPU use

~~~python
validation = fo.validate(
    circuits=[qasm],
    credentials=credentials,
    backend_name=backend_name,
)

if validation.get("results"):
    raise RuntimeError(validation["results"])
~~~

Treat warnings as execution evidence. Fire Opal warns when estimated duration approaches coherence limits and rejects circuits beyond supported hardware limits.

## Raw measurement workloads

~~~python
job = fo.execute(
    circuits=[qasm],
    shot_count=2048,
    credentials=credentials,
    backend_name=backend_name,
)

action_id = job.action_id
status = job.status()
result = job.result()
~~~

`result()` blocks. Poll with `status()` when nonblocking control is required.

Use `execution_results` for circuits with multiple classical registers. Preserve:
- action ID;
- provider job IDs;
- execution metadata;
- warnings;
- Fire Opal/package versions.

Retrieve interrupted jobs with:

~~~python
fo.activity_monitor(limit=20)
result = fo.get_result(action_id)
metadata = fo.get_action_metadata(limit=20)
~~~

Use Fire Opal results rather than provider-native results because Fire Opal post-processing is applied there.

## Batches and iterative algorithms

A single job supports at most 300 circuits or parameter dictionaries. Fire Opal allows up to 40 concurrent jobs.

Use `iterate` for sequential jobs, variational loops, or workloads exceeding one batch:

~~~python
jobs = []
for parameter_batch in batches:
    jobs.append(
        fo.iterate(
            circuits=[parameterized_qasm],
            parameters=parameter_batch,
            shot_count=2048,
            credentials=credentials,
            backend_name=backend_name,
        )
    )

results = [job.result() for job in jobs]
fo.stop_iterate(credentials, backend_name)
~~~

`iterate` manages provider-specific queue/session reuse. Always release the session.

## Expectation values

Use direct expectation APIs when the objective is a Hamiltonian/observable, rather than reconstructing it from raw bitstrings.

~~~python
from fireopal.types import PauliOperator

H = PauliOperator.from_list([
    ("ZZI", 0.5),
    ("IZZ", 0.5),
])

job = fo.estimate_expectation(
    circuits=[qasm],
    observables=H,
    shot_count=2048,
    credentials=credentials,
    backend_name=backend_name,
)

result = job.result()
values = result["expectation_values"]
std = result["standard_deviations"]
~~~

Use `iterate_expectation` for VQE/QML/custom optimization loops, then call `stop_iterate`.

## IBM execution controls

~~~python
from fireopal.run_options import IbmRunOptions

options = IbmRunOptions(
    session_id=None,
    job_tags=["experiment"],
    reduce_approximation=True,
)
~~~

`reduce_approximation=True` lowers Fire Opal's approximation tolerance when small/near-identity rotations must be preserved. Existing IBM Runtime sessions may be supplied through `session_id`.

## Mid-circuit measurements

Fire Opal supports mid-circuit and final measurements. Multiple classical registers are supported with `execute`.

Read named registers from:

~~~python
registers = job.result()["execution_results"][0]
mid = registers["mcm"]
final = registers["final"]
~~~

Reusing the same classical bits overwrites earlier values. Give mid-circuit and terminal data separate bits/registers when both are needed.

## Managed QAOA

Use `solve_qaoa` when Fire Opal should own circuit construction, hardware execution, and classical parameter optimization.

Accepted problem forms include:
- NetworkX graph with `maxcut` or `max-k-cut`;
- nonlinear SymPy binary polynomial;
- diagonal I/Z `PauliOperator`;
- optional exactly-one Hamming-weight constraints.

~~~python
job = fo.solve_qaoa(
    problem=graph,
    problem_type="maxcut",
    credentials=credentials,
    backend_name=backend_name,
)
solution = job.result()
~~~

The result includes the best bitstring, cost, final distribution, iteration count, parameter values, and warnings.

## Managed many-body dynamics

`simulate_dynamics` accepts a model, initial state, simulation definition, observables, shots, backend, and credentials. Fire Opal performs synthesis/Trotterization, hardware-aware mapping, suppression, execution, and observable estimation.

Use it when the task is a supported many-body model rather than manually constructing every Trotter circuit.

## Monte Carlo integration

`integrate_monte_carlo` accepts either a prepared QASM problem or a problem built with Fire Opal objective/distribution helpers.

~~~python
job = fo.integrate_monte_carlo(
    problem=problem,
    credentials=credentials,
    backend_name=backend_name,
    integrator_options={
        "max_iteration_count": 20,
        "target_variance": 1e-3,
    },
)
~~~

Use this path for supported integration/finance workloads instead of manually orchestrating amplitude-estimation circuits.

## Execution policy

Fire Opal is for real hardware; its execution pipeline does not support simulators.

Its pipeline includes hardware-aware compilation/layout, deterministic error suppression such as dynamical-decoupling/control corrections, and measurement-error mitigation. Additional provider jobs tagged for mitigation can appear; Q-CTRL states this calibration overhead is typically about ten seconds or less.

Prefer shallower circuits and outputs distinguishable from a uniform distribution. Validation warnings around T1/coherence limits are a signal to reduce depth before spending hardware time.

Keep Fire Opal distinct from FTQC QEC. Error suppression does not prove logical fault tolerance, reduce algorithmic logical width, or replace a code/factory/resource model.
