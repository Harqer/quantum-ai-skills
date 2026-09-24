---
name: semantic-gate-reduction
description: Reduce quantum work before decomposition using algebraic identities, virtual permutations, constant propagation, common-subexpression elimination, and cross-boundary fusion. Use before generic gate-level optimization.
---

# Semantic Gate Reduction

Optimize at the highest representation that still exposes algorithm structure.

- Keep rotations/permutations as index or wire relabelings when semantics permit.
- Propagate known constants before reversible synthesis.
- Fuse adjacent algorithmic operations before lowering so cancellation and shared work remain visible.
- Reorder commuting work to reduce critical paths and temporary lifetimes.
- Factor shared subexpressions only after comparing storage/uncompute cost against recomputation.
- Preserve named semantic regions long enough for domain-aware optimization.
- Compare candidates only after exact verification and downstream FTQC costing.

## Implementation gate

Before implementing these transformations, load `references/implementation.md`. It defines the semantic IR, virtual-wire maps, constant-propagation legality, XOR canonicalization, CSE cost rule, commutation restrictions, SHA-style rotate example, and verification conditions.

Also apply `../quantum-operations/references/implementation-contract.md`. Do not code a rewrite whose legality condition is absent.
