---
name: fault-tolerant-runtime-control
description: Design the classical control plane for fault-tolerant quantum execution. Use for Pauli/Clifford frame tracking, decoded logical measurements, conditional operations, magic-state injection control, mid-circuit measurement, reset/reuse legality, and feed-forward deadlines.
---

# Fault-Tolerant Runtime Control

Model fault-tolerant execution as a closed loop linking quantum operations, measurements, decoding, logical-frame state, and classical decisions. Maintain an explicit Pauli or Clifford frame, classify each logical operation as physical, frame-tracked, measurement-mediated, or compiled into another primitive, and update subsequent measurement interpretation and conditional control from that frame. When a frame update is semantically equivalent to a physical correction and the architecture supports deferred correction, keep the correction in software and carry its effect forward.

For every measurement-dependent operation, record the raw measurement inputs, decoder contribution, corrected logical outcome, classical function, dependent quantum event, and feed-forward deadline. Measurement and reset become available for ancilla cleanup when the selected protocol proves that the quantum information has been safely exported, corrected, or uncomputed; the controller then tracks the resulting byproduct before reuse. Magic-state injection, teleportation, and distillation interfaces should expose their measurement outcomes, acceptance decisions, byproducts, retries, and synchronization points as first-class runtime events.

Define explicit behavior for late decoder results, decoder convergence failure, rejected factory outputs, repeated-measurement protocols, and controller/decoder resynchronization. Feed these events into the runtime scheduler so the system inserts protocol-defined stalls or retries and every dependent quantum operation consumes a current logical state.

## Implementation gate

Load `references/implementation.md` together with `references/research.md` before coding controller or frame logic. The implementation reference defines the Pauli-frame bit representation, H/S/CNOT update rules, general Pauli-measurement reinterpretation, the non-Clifford boundary, and feed-forward deadline calculation. Apply `../quantum-operations/references/implementation-contract.md` so frame transitions and measurement-assisted cleanup are implemented from explicit algebra and protocol rules.
