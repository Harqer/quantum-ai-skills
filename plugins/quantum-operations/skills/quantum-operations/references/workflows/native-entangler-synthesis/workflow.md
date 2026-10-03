---
name: native-entangler-synthesis
description: Lower two-qubit interactions directly into hardware-native parameterized entanglers, canonical SU(4) forms, and virtual single-qubit phases to minimize physical 2Q gates and depth.
---

# Native Entangler Synthesis

Use this workflow after architecture-independent simplification and before final hardware execution. Read the selected backend's current native gate set, angle domain, virtual-gate semantics, and compiler controls. Canonicalize two-qubit interactions and emit the strongest native entangler that implements them directly instead of expanding through fixed-angle CNOT/CZ building blocks.

Track physical two-qubit interactions, angle/duration/error model, local corrections, and depth. Do not infer support from another hardware generation.

Provider runtime optimizations such as automatic single-qubit squashing are measured backend behavior, not guaranteed user-side compile reductions.

## Implementation gate

Load `references/implementation.md`, `references/research.md`, and the Quantinuum example. Revalidate the target backend's native gate set and submission option immediately before production code.
