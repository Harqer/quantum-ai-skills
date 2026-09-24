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

strict=True makes pytket check pass pre/postcondition compatibility.

## Preserve checkpoints

Before each pipeline:

~~~python
before = circuit.copy()
before_gate_count = before.n_gates
before_depth = before.depth()
~~~

After the pass:

~~~python
after_gate_count = circuit.n_gates
after_depth = circuit.depth()
~~~

Treat apply() returning True as a pass-execution result, then measure the selected resource objective explicitly.

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

Current API note: use AutoRebase and verify the installed pytket version against the current pass documentation.

## Architecture routing

Only route once an architecture is selected.

A representative architecture-aware path is:

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

The AASRouting pass relabels/routs against the architecture and may change the circuit gate representation.

Record logical-to-physical mapping and re-run cleanup/rebase afterward as needed.

## Pauli simplification caution

For PauliSimp / GreedyPauliSimp, explicitly decide whether global phase preservation is required.

When the equivalence relation requires exact global phase, select a pass/configuration whose documented semantics preserve that phase relation.

## Recommended comparison workflow

~~~text
candidate_0 = original

candidate_1 =
  logical peephole / Clifford / redundancy optimization

candidate_2 =
  phase/Pauli-specific optimization if preconditions hold

candidate_3 =
  architecture placement/routing

candidate_4 =
  post-routing cleanup + final rebase
~~~

Keep every checkpoint. Compare all candidates under:
- exact semantic verification;
- native 2Q count;
- native depth;
- non-Clifford demand;
- implicit wire swaps/permutations;
- logical/physical width.

## Verification

pytket optimization is not its own proof.

For important rewrites:
- export before/after to a mutually supported format;
- verify with MQT QCEC or another independent checker;
- for phase-sensitive transformations, compare the correct equivalence relation;
- assert measurements/classical controls remain attached to the intended qubits/bits.

Source:
https://docs.quantinuum.com/tket/api-docs/passes.html
