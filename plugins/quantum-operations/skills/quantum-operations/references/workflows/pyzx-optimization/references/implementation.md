# PyZX optimization: implementation reference

API state checked against PyZX 0.10.6 documentation.

## Supported input boundary

Load a circuit with:

~~~python
import pyzx as zx

circ = zx.Circuit.load("input.qasm")
# or:
circ = zx.Circuit.from_qasm(qasm_text)
~~~

Current Circuit.from_qasm supports OpenQASM 2 and 3, including reset, measurement, and if statements, but not every parameterized custom-gate form.

Before ZX extraction, check whether the target circuit is unitary. General circuit extraction from a ZX graph does **not** support ground vertices arising from measurements/resets.

## Pipeline A: graph-level full reduction

Use only for a unitary region:

~~~python
import pyzx as zx
from pyzx.extract import extract_circuit

original = zx.Circuit.load("input.qasm")
graph = original.to_graph()

zx.simplify.full_reduce(graph)

candidate = extract_circuit(
    graph,
    optimize_czs=True,
    optimize_cnots=2,
    up_to_perm=False,
    quiet=True,
)
~~~

Checkpoint metrics before accepting candidate:

~~~python
before_2q = original.twoqubitcount()
after_2q = candidate.twoqubitcount()

eq = original.verify_equality(
    candidate,
    up_to_swaps=False,
    up_to_global_phase=True,
)
assert eq is True
~~~

PyZX documentation explicitly warns that extraction is not architecture-aware and can increase 2-qubit cost. Preserve the original and reject a regressive candidate under the selected FTQC metric.

## Pipeline B: circuit-level optimization

For supported gate sets:

~~~python
import pyzx as zx

circ = zx.Circuit.load("input.qasm")
basic = zx.optimize.basic_optimization(circ.copy())
full = zx.optimize.full_optimize(circ.copy())
~~~

For phase-polynomial optimization:

~~~python
phase_opt = zx.optimize.phase_block_optimize(circ.copy())
~~~

### Hard precondition

phase_block_optimize is documented for Clifford+T circuits. Do **not** apply it to circuits containing unsupported smaller-angle rotations or Toffoli-like gates; PyZX documentation warns it may return wrong output.

Implement a preflight gate-set check before calling it.

## Pipeline C: phase teleportation

teleport_reduce performs full-reduce-like simplification while preserving the graph structure and moving/fusing phases:

~~~python
g = original.to_graph()
g2 = zx.simplify.teleport_reduce(g)
~~~

Use this path when preserving graph/circuit structure is important for later extraction or architecture-aware processing.

## Equality semantics

Circuit.verify_equality(other, up_to_swaps=False, up_to_global_phase=True):
- returns True when PyZX can prove equality;
- may return None when the proof procedure is inconclusive.

Treat None as an inconclusive result and continue with an independent equivalence check before accepting the candidate.

For small critical circuits, supplement with tensor comparison:

~~~python
import pyzx as zx
assert zx.compare_tensors(
    original.to_tensor(),
    candidate.to_tensor(),
    preserve_scalar=False,
)
~~~

This is exponential and only for small circuits.

## Production acceptance

Accept an optimized candidate only if:
1. exact equality is independently established;
2. required phase semantics match;
3. two-qubit/non-Clifford/depth metrics improve or remain on the Pareto frontier;
4. any wire permutation from extraction is explicitly represented;
5. architecture-aware routing is performed later by the appropriate tool.

Sources:
- https://pyzx.readthedocs.io/en/latest/api.html
- https://pyzx.readthedocs.io/en/stable/notebooks/simplify.html
