---
name: qec-code-strategy
description: Select and reason about quantum error-correcting codes and logical operations in a hardware-agnostic way. Use for surface/color/LDPC/bosonic code tradeoffs, transversal gates, code switching, state preparation, logical error budgets, and decoder/control requirements.
---

# QEC Code Strategy

Select a QEC architecture from a complete machine and workload model. Capture the physical noise process, leakage and bias, connectivity and locality, gate/measurement/reset/transport timing, syndrome-cycle duration, target logical failure budget, required logical operations, detector-model changes, decoder resources, feed-forward deadlines, and available physical and classical scale. Use those inputs to construct concrete candidate records that pair a code family with its syndrome circuit, decoder, state-preparation and measurement protocols, logical-operation mechanisms, factory interface, routing model, and measured or justified logical-error behavior.

Compare candidates at the system level. Encoding rate, threshold behavior, syndrome depth, logical-gate availability, code switching or lattice-surgery overhead, magic-state demand, decoder tail latency, communication, spacetime volume, and wall-clock runtime should all enter the same comparison. Route every qLDPC candidate that advances beyond family-level screening through `qldpc-architecture`, which requires an exact finite construction, Tanner-edge hardware mapping, syndrome circuit, circuit-level decoder path, and complete logical-operation record. Route toric-code candidates through `toric-code-architecture` so periodic topology, homological logical operators, syndrome-measurement noise, decoder choice, seam/routing cost, dimensionality, and the distinction between memory and universal computation remain explicit. Route bosonic or encoded logical-qutrit/qudit candidates through `qudit-architecture` so physical encoding, generalized Pauli control, leakage, readout, stabilization, and provider access remain concrete. Derive detector throughput from the actual syndrome circuit, select code distance or parameters from measured/simulated logical-error data and the assigned workload budget, and confirm that the candidate exposes a complete logical ISA for every operation the workload needs.

## Implementation gate

Load `references/implementation.md` before selecting or coding a QEC architecture. It defines the machine model, candidate record, measured-data distance selection, detector-rate calculation, logical-ISA completeness check, and acceptance criteria. Apply `../quantum-operations/references/implementation-contract.md` so each comparison uses concrete protocols, syndrome circuits, decoders, and error models rather than code-family labels alone.
