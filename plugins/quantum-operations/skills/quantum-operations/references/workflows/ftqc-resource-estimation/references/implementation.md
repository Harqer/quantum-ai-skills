# FTQC resource estimation: implementation reference

This reference separates **logical costing tools** from **physical FTQC estimators** and from the repository runtime scheduler.

## Microsoft QDK QRE path

API checked against current qdk.qre documentation in September 2026.

Install the current estimator package according to Microsoft documentation:

~~~text
pip install --upgrade "qdk[qre]"
~~~

### OpenQASM application example

~~~python
from qdk.qre import estimate
from qdk.qre.application import OpenQASMApplication
from qdk.qre.models import (
    GateBased,
    SurfaceCode,
    RoundBasedFactory,
)

app = OpenQASMApplication(qasm_text)

arch = GateBased(
    error_rate=1e-4,
    gate_time=100,          # ns
    measurement_time=500,   # ns
)

isa_query = SurfaceCode.q() * RoundBasedFactory.q()

results = estimate(
    app,
    arch,
    isa_query=isa_query,
    max_error=0.01,
)

frame = results.as_frame()
~~~

Replace the example timings and error rates with the measured or specified parameters of the target hardware before producing a production estimate.

### Other supported application types

Current qdk.qre exposes application wrappers including:
- QSharpApplication;
- CirqApplication;
- OpenQASMApplication;
- QIRApplication.

QIRApplication expects base-profile QIR. Check profile compatibility before using QIR generated for adaptive execution.

### Pareto output

Use the estimator Pareto set rather than collapsing to one score:

~~~python
from qdk.qre import plot_estimates
plot_estimates(results, runtime_unit="ms")
~~~

Store the raw frame/result data with model versions and assumptions.

## Qualtran logical resource path

Qualtran is useful for compositional algorithm costing before/alongside physical QEC estimation.

~~~python
from qualtran.resource_counting import (
    get_cost_value,
    QECGatesCost,
    QubitCount,
)

gate_counts = get_cost_value(
    bloq,
    QECGatesCost(),
)

qubit_count = get_cost_value(
    bloq,
    QubitCount(),
)
~~~

QECGatesCost returns a GateCounts-style resource record for expensive/FT-relevant operations.

QubitCount estimates peak qubits by recursively examining decompositions.

### Important QubitCount limitation

Current Qualtran documentation states that its qubit-count cost assumes sequential execution of sub-bloqs and does not fully tetris/interleave lifetimes. Treat it as an estimator, not a substitute for ancilla-lifetime or ftqc-runtime-scheduling.

## Reconcile logical and physical estimates

Maintain one canonical resource record:

~~~text
logical:
  qubits
  T
  CCZ/Toffoli
  rotations + precision
  measurements
  Clifford 2Q
  dependency depth

qec:
  code
  distance/parameters
  logical operation cycles

factories:
  type
  count
  footprint
  throughput
  output error

classical:
  decoder workers
  memory/network
  latency distribution

runtime:
  baseline cycles
  decoder stalls
  factory stalls
  routing stalls
  wall-clock

physical:
  data/QEC qubits
  factory qubits
  total peak qubits
~~~

Attach this repository's decoder queue and control-plane costs explicitly alongside the QRE output so the complete runtime model remains visible.

## Error budget

Partition a declared total budget rather than inventing per-layer tolerances:

~~~text
epsilon_total >=
    epsilon_algorithm
  + epsilon_synthesis
  + epsilon_logical_qec
  + epsilon_factory
  + epsilon_decoder_or_protocol
~~~

Use a more rigorous composition bound when available; document it.

## Acceptance test

Every estimate must be reproducible from:
- application/circuit hash;
- logical resource counts;
- hardware architecture parameters;
- QEC/factory model and version;
- error budget;
- decoder/runtime inputs;
- estimator package versions;
- raw estimator result, not only a headline number.
