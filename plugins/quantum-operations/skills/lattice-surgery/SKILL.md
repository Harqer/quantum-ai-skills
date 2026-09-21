---
name: lattice-surgery
description: Compile and optimize fault-tolerant logical operations using lattice surgery/topological QEC abstractions. Use for patch layouts, Pauli measurements, routing, scheduling, spacetime volume, and surface-code logical compilation.
---

# Lattice Surgery and Topological Compilation

Treat lattice surgery as a logical/spacetime compilation problem, not merely a gate translation.

- Convert logical operations into Pauli-product measurements / patch operations when appropriate.
- Optimize patch placement, movement, routing, merge/split schedule, and dependency depth.
- Track logical patches, code cycles, spacetime volume, routing congestion, and factory interfaces.
- Keep code distance and factory placement parameterized rather than baked into the logical schedule.
- Verify logical equivalence independently of geometric optimization.
- Use TQEC as a primary modern reference/tool for surface-code/lattice-surgery design automation; compare other lattice-surgery compilers only when their capabilities match the task.

See `references/tools.md`.
