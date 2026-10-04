---
name: semantic-gate-reduction
description: Reduce quantum work before decomposition using algebraic identities, permutation-aware lowering, constant propagation, common-subexpression elimination, and cross-boundary fusion.
---

# Semantic Gate Reduction

Optimize at the highest representation that still exposes algorithm structure. Treat exact register permutations, rotations, reversals, and reindexings as semantic mappings first: lower them into tracked logical-wire views or bit dependencies when useful, but do not synthesize state-moving SWAP networks solely to represent a change of logical order. Preserve the logical-position-to-wire map through downstream Boolean, arithmetic, measurement, and output semantics.

Keep semantic permutation cost separate from hardware routing cost. Before physical layout, a permutation may often be absorbed into virtual-qubit mapping. After physical placement, connectivity-induced state movement is a real hardware cost and may be removed only together with a sound layout/mapping update. At interchange boundaries, either preserve permutation metadata, materialize it explicitly, or fail the conversion; never silently drop it.

Propagate proven constants before reversible synthesis, normalize XOR/parity expressions, and keep named semantic regions intact long enough to expose cancellation, fusion, common subexpressions, and shared nonlinear work. Evaluate sharing and recomputation through the downstream FTQC objective rather than gate count alone.

After each rewrite, verify the exact logical map, register ordering/significance, required phase relation, live outputs, ancilla final states, and any final output permutation before carrying the candidate into downstream FTQC costing.

## Implementation gate

Load `references/implementation.md` before coding semantic rewrites. For permutation-aware lowering, also load `references/examples/permutation-aware-lowering.md`. The implementation reference defines the semantic IR, permutation maps, arithmetic-significance invariant, materialization boundaries, constant-propagation legality, XOR canonicalization, common-subexpression cost rule, commutation restrictions, and verification conditions. Apply `../quantum-operations/references/implementation-contract.md` so each production rewrite is supported by an explicit legality rule and verification path.
