---
name: semantic-gate-reduction
description: Reduce quantum work before decomposition using algebraic identities, virtual permutations, constant propagation, common-subexpression elimination, and cross-boundary fusion.
---

# Semantic Gate Reduction

Optimize at the highest representation that still exposes algorithm structure. Represent rotations and permutations as logical wire views when the semantics permit virtual relabeling, propagate proven constants before reversible synthesis, normalize XOR/parity expressions, and keep named semantic regions intact long enough to expose cancellation, fusion, common subexpressions, and shared nonlinear work. Reorder commuting operations through explicit algebraic rules so critical paths and temporary lifetimes shrink while semantic dependencies remain visible.

Evaluate sharing and recomputation through the downstream FTQC objective rather than gate count alone. A shared expression introduces storage, routing, and cleanup cost, while recomputation introduces extra cycles and non-Clifford demand; preserve both candidates when they occupy different Pareto points. After each rewrite, verify the exact logical map, required phase relation, live outputs, and ancilla final states, then carry the candidate into downstream FTQC costing.

## Implementation gate

Load `references/implementation.md` before coding semantic rewrites. It defines the semantic IR, virtual-wire maps, constant-propagation legality, XOR canonicalization, common-subexpression cost rule, commutation restrictions, SHA-style rotation example, and verification conditions. Apply `../quantum-operations/references/implementation-contract.md` so each production rewrite is supported by an explicit legality rule and verification path.
