# Executable example: ZX reduction and exact equality

**Definition.** Rewrite a circuit into a ZX graph, reduce it and extract a circuit. Always verify the candidate implements the same map, including any permitted permutation boundary.

Run: `pip install pyzx`.

~~~python
import pyzx as zx
original = zx.Circuit(2)
original.add_gate("CNOT", 0, 1)
original.add_gate("CNOT", 0, 1)

graph = original.to_graph()
zx.simplify.full_reduce(graph)
candidate = zx.extract_circuit(graph.copy())
assert original.verify_equality(candidate, up_to_swaps=False, up_to_global_phase=True)
assert candidate.twoqubitcount() <= original.twoqubitcount()
print("verified 2-qubit cost:", original.twoqubitcount(), "->", candidate.twoqubitcount())
~~~

**Primary official example:** https://pyzx.readthedocs.io/en/stable/notebooks/simplify.html

**Verification:** Verify equivalence after extraction; compare T-count, two-qubit gates and depth against the original. The explicit equality precondition is a material gate in accepting optimization.
