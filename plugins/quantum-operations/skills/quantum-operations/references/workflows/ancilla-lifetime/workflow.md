---
name: ancilla-lifetime
description: Minimize peak logical width and garbage through liveness analysis, compute-use-uncompute scheduling, clean/dirty/borrowed ancillas, recomputation, and reversible pebbling.
---

# Ancilla and Lifetime Optimization

Treat qubits as a liveness and scheduling problem. Build versioned def-use intervals for every temporary, move each inverse cleanup directly after the last dependent use when the dependency graph permits it, and pool ancilla slots whose live intervals are disjoint and whose contracts are compatible. Track clean, dirty, borrowed, measured, and resettable ancillas as distinct state contracts so allocation and release preserve the required quantum state and correlations.

Evaluate storage and recomputation together. Reversible pebbling provides the space-time model for deciding which intermediates stay live and which are recomputed, while mandatory simultaneous dependencies remain explicit in the schedule. Feed peak logical width, added recomputation, logical cycles, routing pressure, and error-budget impact into the downstream FTQC cost model, then verify that every released ancilla satisfies its restoration and disentanglement contract.

## Implementation gate

Load `references/implementation.md` before changing ancilla allocation or lifetime. That reference defines the clean, dirty, measured, and resettable contracts; SSA liveness; linear-scan allocation; legal reversible-pebbling moves; storage-versus-recomputation costing; and release tests. Apply `../quantum-operations/references/implementation-contract.md` so every implementation follows an explicit state contract and a proven cleanup path.
