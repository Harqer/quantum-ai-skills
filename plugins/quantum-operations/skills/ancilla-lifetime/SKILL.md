---
name: ancilla-lifetime
description: Minimize peak logical width and garbage through liveness analysis, compute-use-uncompute scheduling, clean/dirty/borrowed ancillas, recomputation, and reversible pebbling.
---

# Ancilla and Lifetime Optimization

Treat qubits as a liveness/scheduling problem.

- Draw def-use intervals for every temporary.
- Apply compute -> consume -> uncompute as soon as dependencies allow.
- Pool temporaries whose live intervals do not overlap.
- Distinguish clean, dirty, borrowed, measured, and resettable ancilla contracts.
- Compare storage against recomputation when width is the limiting resource.
- Use reversible pebbling on dependency graphs, but do not claim it removes mandatory simultaneous dependencies.
- Include QEC implications: extra logical qubits can dominate physical-qubit footprint, while recomputation can increase logical cycles and error budget.
- Verify every released ancilla is restored/disentangled as required.
