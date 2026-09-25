# IR interoperability: implementation reference

Interchange is a semantic translation problem. Establish semantic preservation through the explicit round-trip and feature checks below.

## Canonical semantic checklist

Before conversion, inventory:

~~~text
qubit order / endian convention
initialization assumptions
unitary gates and parameters
measurement basis and destination bits
reset
classical conditions
loops / switch / while
timing/delay/barrier semantics
physical-qubit identifiers
global/relative phase requirements
detector annotations
logical observables
custom QEC/logical operations
~~~

After conversion, every required item must either:
1. exist in the target IR with matching semantics; or
2. be carried in a documented sidecar/extension; or
3. cause the conversion to fail.

Report every unsupported semantic explicitly and preserve it through a documented extension or sidecar when the workflow requires it.

## OpenQASM 3.1 dynamic example

~~~qasm
OPENQASM 3.1;
include "stdgates.inc";

qubit q;
bit m;

h q;
m = measure q;

if (m == 1) {
    x q;
}

reset q;
~~~

OpenQASM 3.1 semantics:
- measure is projective Z-basis measurement and writes the result to a classical bit;
- reset performs a partial trace/discard followed by preparation of |0>;
- reset is therefore non-unitary and is not equivalent to reversible uncomputation.

Current specification:
https://openqasm.com/versions/3.1/

## OpenQASM 3.1 control flow

OpenQASM 3.1 supports classical control constructs including:
- if/else;
- for;
- while;
- switch;
- classical subroutines/externs.

A target/backend may support only a subset. Validate target support rather than assuming language support equals hardware support.

## QIR profiles

QIR is LLVM-based and target profiles constrain which runtime/QIS constructs are valid.

When using current Microsoft QDK Qiskit interop, hardware QIR generation must target an allowed profile such as Base or Adaptive_RI rather than Unrestricted.

A dynamic Qiskit circuit with classical branching can be emitted for Adaptive_RI:

~~~python
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qsharp.interop.qiskit import QSharpBackend
from qsharp import TargetProfile

qreg = QuantumRegister(3, name="q")
creg = ClassicalRegister(3, name="c")
qc = QuantumCircuit(qreg, creg)

qc.h([0, 1, 2])
qc.measure_all(add_bits=False)

with qc.switch(creg) as case:
    with case(7):
        qc.x(0)
    with case(1, 2):
        qc.z(1)
    with case(case.DEFAULT):
        qc.cx(0, 1)

qc.measure_all(add_bits=False)

backend = QSharpBackend()
qir = backend.qir(
    qc,
    target_profile=TargetProfile.Adaptive_RI,
)
~~~

When a program uses adaptive behavior outside the Base profile, preserve the adaptive semantics and surface the profile diagnostic so the caller can select an appropriate target profile.

## QIR resource-estimator boundary

Current qdk.qre QIRApplication expects base-profile QIR.

Therefore an adaptive runtime-control program may require:
- a separate logical/resource-count application model; or
- a semantics-preserving static abstraction for estimation.

Route Adaptive_RI QIR through an interface that advertises support for that profile, and use a Base-profile representation only after an explicit semantics-preserving transformation.

## Stim boundary

Stim circuit/DEM representations include QEC-specific semantics such as:
- DETECTOR;
- OBSERVABLE_INCLUDE;
- detector coordinates;
- noise instructions.

Carry these annotations through the documented QEC sidecar because standard OpenQASM lacks direct equivalents.

If converting a Stim QEC circuit through OpenQASM/QIR:
- preserve detector/observable metadata in a sidecar or tool-specific representation;
- verify the reconstructed detectors after round trip;
- fail conversion if the downstream task requires them and no preservation path exists.

## Round-trip acceptance test

For every conversion path A -> B -> A or A -> B -> executable target:

1. compare qubit/register ordering;
2. compare measurement destination mapping;
3. compare reset locations;
4. compare branch predicates and branch bodies;
5. compare parameters/angle units;
6. compare phase semantics when relevant;
7. verify circuit equivalence for the unitary portion;
8. test dynamic branches separately;
9. compare resource counts to detect hidden decomposition;
10. verify QEC sidecar metadata when detectors/observables are required.

## Unsupported conversion rule

When the target IR lacks a required feature, raise or report an explicit unsupported-feature result and identify the semantic that needs another representation.

Examples:
- detector annotations lost through ordinary QASM;
- dynamic control sent to a Base-profile-only target;
- pulse/timing semantics lowered into an IR without timing support;
- reset converted into a unitary placeholder.

Sources:
- OpenQASM 3.1: https://openqasm.com/versions/3.1/
- QIR specification: https://github.com/qir-alliance/qir-spec
- current QDK Qiskit/QIR interop: https://github.com/microsoft/qdk/wiki/Qiskit-Interop
