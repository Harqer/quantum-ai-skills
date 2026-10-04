# pytket optimization: implementation reference

API state checked against pytket 2.18.1 documentation.

## Build explicit pass pipelines

Use SequencePass so ordering and predicates are explicit.

~~~python
from pytket.passes import (
    SequencePass,
    FullPeepholeOptimise,
    RemoveRedundancies,
    CliffordSimp,
)

logical_pass = SequencePass(
    [
        FullPeepholeOptimise(),
        CliffordSimp(),
        RemoveRedundancies(),
    ],
    strict=True,
)

logical_pass.apply(circuit)
~~~

`strict=True` makes pytket check pass pre/postcondition compatibility.

## Preserve checkpoints

Before and after each pass, record gate count, depth, and the implicit qubit permutation.

~~~python
before = circuit.copy()
before_perm = before.implicit_qubit_permutation()

logical_pass.apply(circuit)

after_perm = circuit.implicit_qubit_permutation()
~~~

Two circuits can have the same visible command sequence but different semantics because pytket may encode SWAPs as implicit wire permutations. Treat that permutation as part of the checkpoint.

## Implicit-permutation boundary

pytket can replace explicit SWAP gates with implicit wire swaps:

~~~python
perm = circuit.implicit_qubit_permutation()
~~~

Keep them implicit while later pytket passes can consume the mapping. Before crossing a framework/IR boundary, verify that the target preserves the permutation.

pytket's OpenQASM converters do **not** account for implicit qubit permutations. If exporting through such a boundary, either preserve the mapping separately or materialize it:

~~~python
exportable = circuit.copy()
exportable.replace_implicit_wire_swaps()
~~~

For pytket -> Qiskit conversion, current `tk_to_qiskit` also leaves implicit swaps unresolved by default; use its documented `replace_implicit_swaps=True` option when the permutation cannot be carried separately.

Do not materialize implicit swaps merely for internal bookkeeping if the next optimizer/router can use the permutation freedom.

## Rebase explicitly

For a known native gate set:

~~~python
from pytket.circuit import OpType
from pytket.passes import AutoRebase

rebase = AutoRebase(
    {OpType.Rz, OpType.SX, OpType.CX},
    allow_swaps=False,
)
rebase.apply(circuit)
~~~

When AutoRebase lacks a known decomposition, provide the reviewed exact decomposition through RebaseCustom.

## Architecture routing

Only route once an architecture is selected.

~~~python
from pytket.architecture import Architecture
from pytket.passes import AASRouting

arch = Architecture([
    (0, 1),
    (1, 2),
    (2, 3),
])

routing = AASRouting(arch)
routing.apply(circuit)
~~~

Record logical-to-physical mapping and implicit/output permutations before and after routing. After physical placement, do not treat routing state movement as a free semantic permutation unless the physical mapping is updated consistently.

## Pauli simplification caution

For PauliSimp / GreedyPauliSimp, explicitly decide whether global phase preservation is required.

## Recommended comparison workflow

~~~text
candidate_0 = original
candidate_1 = logical simplification + permutation tracking
candidate_2 = phase/Pauli optimization if legal
candidate_3 = architecture placement/routing
candidate_4 = post-routing cleanup + final rebase
~~~

Compare all candidates under:
- exact semantic verification;
- native 2Q count;
- native depth;
- non-Clifford demand;
- implicit/output permutations;
- logical/physical width.

## Verification

pytket optimization is not its own proof.

For important rewrites:
- verify before/after with MQT QCEC or another independent checker when supported;
- inspect or materialize implicit permutations before exporting to a representation that cannot carry them;
- assert measurements/classical outputs remain attached to the intended logical values;
- for phase-sensitive transformations, compare the correct equivalence relation.

Sources:
- https://docs.quantinuum.com/tket/api-docs/passes.html
- https://docs.quantinuum.com/tket/user-guide/manual/manual_circuit.html
- https://docs.quantinuum.com/tket/api-docs/qasm.html
- https://docs.quantinuum.com/tket/extensions/pytket-qiskit/api.html
