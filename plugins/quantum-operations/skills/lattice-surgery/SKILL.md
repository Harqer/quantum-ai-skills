---
name: lattice-surgery
description: Compile and optimize fault-tolerant logical operations using lattice surgery/topological QEC abstractions. Use for patch layouts, Pauli measurements, routing, scheduling, spacetime volume, and surface-code logical compilation.
---

# Lattice Surgery and Topological Compilation

Treat lattice surgery as a logical and spacetime compilation problem. Lower logical operations into the reviewed Pauli-product measurements and patch operations supported by the selected code architecture, then optimize patch placement, movement, routing, merge/split timing, dependency depth, factory interfaces, and congestion while keeping code distance and factory placement parameterized. Track patch identity, logical basis and orientation, space/time coordinates, required ancilla regions, and logical correlation surfaces throughout the transformation.

Use TQEC as the primary modern reference for surface-code and lattice-surgery design automation when its model matches the task, and evaluate alternative compilers against the same logical semantics and resource model. Verify each geometric rewrite by recompiling the baseline and candidate, preserving the intended logical observables/correlation surfaces, generating detector-annotated circuits, and comparing logical error behavior, physical footprint, and spacetime volume under the same assumptions.

## Implementation gate

Load `references/implementation.md` before implementing a lattice-surgery compiler or geometry, and use `references/tools.md` as the project/version index. The implementation reference gives the current TQEC CNOT-to-correlation-surfaces-to-compilation-to-Stim-to-simulation flow and its verification requirements. Apply `../quantum-operations/references/implementation-contract.md` and pin the TQEC version or commit used by production examples.
