---
name: qubit-reuse-compilation
description: Reduce executable circuit width by scheduling causal cones, measuring dead qubits mid-circuit, resetting them, and reusing physical carriers without changing observable semantics.
---

# Qubit Reuse Compilation

Use this workflow when the target supports mid-circuit measurement/reset and the circuit contains causal cones that can finish before the rest of the computation.

Build a dependency/causal-cone model, order cones to minimize simultaneously live qubits, emit measurement+reset at each proven release boundary, and remap later logical qubits onto released physical slots. Evaluate the time-reversed dual when supported.

Treat width, added measurement/reset operations, depth, routing, and fidelity as a Pareto problem. Never measure a qubit that remains coherently required.

## Implementation gate

Load `references/implementation.md`, `references/research.md`, and the Quantinuum HyperTKET example. Route lower-level state-lifetime questions to ancilla-lifetime and measurement/byproduct legality to fault-tolerant-runtime-control.
