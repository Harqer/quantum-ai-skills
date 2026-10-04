# IR interoperability: implementation reference

Interchange is a semantic translation problem. Establish semantic preservation through the explicit round-trip and feature checks below.

## Canonical semantic checklist

Before conversion, inventory:

~~~text
qubit order / endian convention
logical-position -> wire mapping
implicit/final output permutation
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
1. exist in the target IR with matching semantics;
2. be carried in a documented sidecar/extension; or
3. cause the conversion to fail.

### Permutation boundary

Implicit permutations are part of circuit semantics even when they are absent from the visible gate list.

Before exporting a circuit with an implicit or virtual permutation:
1. determine whether the target representation carries an equivalent input/output mapping;
2. if yes, translate the mapping explicitly;
3. otherwise materialize an equivalent permutation in the circuit;
4. if neither is possible, fail rather than silently changing the computation.

Do not assume that parser success implies permutation preservation. For example, pytket's OpenQASM converters explicitly do not account for implicit qubit permutations.

Measurements and classical outputs must be interpreted through the final permutation. Arithmetic/register endianness must remain attached to **logical positions**, not whichever wire IDs exist after conversion.

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

OpenQASM 3.1 supports classical control constructs including if/else, for, while, switch, and classical subroutines/externs. A target/backend may support only a subset. Validate target support rather than assuming language support equals hardware support.

## QIR profiles

QIR is LLVM-based and target profiles constrain which runtime/QIS constructs are valid.

When using current Microsoft QDK Qiskit interop, hardware QIR generation must target an allowed profile such as Base or Adaptive_RI rather than Unrestricted. Preserve adaptive semantics and surface profile diagnostics rather than silently weakening the program.

## QIR resource-estimator boundary

Current qdk.qre QIRApplication expects base-profile QIR.

Therefore an adaptive runtime-control program may require:
- a separate logical/resource-count application model; or
- a semantics-preserving static abstraction for estimation.

## Stim boundary

Stim circuit/DEM representations include QEC-specific semantics such as DETECTOR, OBSERVABLE_INCLUDE, detector coordinates, and noise instructions.

Carry these annotations through a documented QEC sidecar because standard OpenQASM lacks direct equivalents. Fail conversion if the downstream task requires them and no preservation path exists.

## Round-trip acceptance test

For every conversion path A -> B -> A or A -> B -> executable target:

1. compare logical/register ordering and endianness;
2. compare implicit/final permutations and logical-to-wire mappings;
3. compare measurement destination mapping after applying the final permutation;
4. compare reset locations;
5. compare branch predicates and branch bodies;
6. compare parameters/angle units;
7. compare phase semantics when relevant;
8. verify circuit equivalence for the unitary portion;
9. test dynamic branches separately;
10. compare resource counts to detect hidden decomposition;
11. verify QEC sidecar metadata when detectors/observables are required.

## Unsupported conversion rule

When the target IR lacks a required feature, raise or report an explicit unsupported-feature result and identify the semantic that needs another representation.

Examples:
- an implicit output permutation is dropped by an ordinary QASM export;
- detector annotations are lost through ordinary QASM;
- dynamic control is sent to a Base-profile-only target;
- pulse/timing semantics are lowered into an IR without timing support;
- reset is converted into a unitary placeholder.

Sources:
- OpenQASM 3.1: https://openqasm.com/versions/3.1/
- QIR specification: https://github.com/qir-alliance/qir-spec
- current QDK Qiskit/QIR interop: https://github.com/microsoft/qdk/wiki/Qiskit-Interop
- pytket OpenQASM implicit-permutation warning: https://docs.quantinuum.com/tket/api-docs/qasm.html
- Qiskit permutation/layout model: https://qiskit.qotlabs.org/docs/api/qiskit/qiskit.transpiler.TranspileLayout
