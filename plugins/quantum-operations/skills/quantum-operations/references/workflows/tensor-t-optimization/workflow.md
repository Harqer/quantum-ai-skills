---
name: tensor-t-optimization
description: Reduce exact Clifford+T non-Clifford cost through signature-tensor decomposition, factorization, gadgetization, and verified resynthesis, including AlphaTensor-Quantum-compatible workflows.
---

# Tensor T Optimization

Use this workflow on Clifford+T regions whose expensive resource is T/CCZ/Toffoli demand. Convert supported phase-polynomial regions to symmetric binary signature tensors, search for lower-rank factorizations, optionally group factors into proven CS/CCZ/Toffoli gadgets, and resynthesize the exact circuit.

Treat factor count as an intermediate T-cost metric. Recompute T count/depth, ancillas, Clifford cost, width, and factory demand after resynthesis.

## Implementation gate

Load `references/implementation.md`, `references/research.md`, and the end-to-end Circuit-to-Tensor example. Use current APIs or published decompositions. Verify the resynthesized circuit against the original before accepting any reduction.
