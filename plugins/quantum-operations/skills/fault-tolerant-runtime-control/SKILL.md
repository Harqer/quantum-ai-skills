---
name: fault-tolerant-runtime-control
description: Design the classical control plane for fault-tolerant quantum execution. Use for Pauli/Clifford frame tracking, decoded logical measurements, conditional operations, magic-state injection control, mid-circuit measurement, reset/reuse legality, and feed-forward deadlines.
---

# Fault-Tolerant Runtime Control

Fault-tolerant execution is a closed loop between quantum operations, measurements, decoding, logical-frame state, and classical decisions.

Do not model the classical controller as zero-cost or semantically passive.

## Maintain explicit frame state

Track the logical Pauli or Clifford frame separately from the physical quantum state.

For each logical operation:
- state whether it is physically executed, virtually frame-tracked, measurement-mediated, or compiled into another primitive;
- define how errors/corrections update the frame;
- define how later logical measurements are conjugated/interpreted through that frame;
- ensure conditional operations consume the correct decoded logical outcome.

Avoid physically applying corrections when frame updates are semantically equivalent and the target architecture supports deferred correction.

## Logical measurements and feed-forward

For every measurement-dependent operation, identify:
- raw measurement inputs;
- decoder/correction required before interpretation;
- logical outcome produced;
- classical function applied to that outcome;
- next quantum operation that depends on it;
- maximum allowed feed-forward latency.

The deadline is determined by the dependency graph, not by an arbitrary controller target.

## Mid-circuit measurement and qubit reuse

Measurement/reset may reduce lifetime or non-Clifford cost, but it is not a generic qubit-deallocation primitive.

Before measuring an algorithmic or ancilla qubit, prove one of:
- its state is no longer entangled with live quantum data;
- the measurement is part of a known measurement-assisted construction whose byproduct is classically tracked/corrected;
- the algorithm intentionally exports that information to the classical domain.

Do not measure coherent workspace merely to reduce width if doing so reveals or destroys information required by the coherent algorithm.

Reset/reuse is legal only after the prior logical information has been safely removed, measured under an allowed protocol, or uncomputed.

## Measurement-assisted uncomputation

Measurement-assisted gadgets can replace expensive coherent inverses in some cases.

For example, temporary logical-AND constructions can erase an ancilla using measurement and classically controlled Clifford correction rather than paying the original non-Clifford cost again.

Apply such gadgets only when:
- phase/byproduct semantics match the surrounding computation;
- measurement outcomes are available within the required control deadline;
- the target QEC/logical ISA supports the required measurement/correction operation;
- ancilla reset/reuse is verified after the gadget.

Do not replace arbitrary compute/uncompute pairs with measurement without a proven construction.

## Magic-state and non-Clifford control

For injection/teleportation/distillation interfaces, model:
- measurement outcomes;
- acceptance/rejection;
- Pauli/Clifford byproducts;
- retries or postselection;
- factory-to-data synchronization;
- conditional corrections or frame updates.

A magic state is not consumed by an abstract T gate with zero classical control cost.

## Failure semantics

Define behavior for:
- decoder result late but eventually available;
- decoder convergence failure;
- rejected magic-state/factory output;
- measurement ambiguity or repeated-measurement protocol;
- controller/decoder desynchronization.

Prefer safe stalls or protocol-defined retries over applying an operation using stale logical-frame information.

## Verification

Test:
- frame-update algebra against direct circuit simulation on small instances;
- logical measurement interpretation under injected Pauli faults;
- conditional-branch correctness;
- measurement-assisted gadget byproducts;
- reset/reuse disentanglement;
- feed-forward timing assumptions against the runtime schedule.

See `references/research.md`.

## Implementation gate

Before coding controller/frame logic, load `references/implementation.md` plus `references/research.md`. The implementation reference defines the Pauli-frame bit representation, H/S/CNOT update rules, general Pauli measurement reinterpretation, non-Clifford boundary, and feed-forward deadline calculation.

Also apply `../quantum-operations/references/implementation-contract.md`.
