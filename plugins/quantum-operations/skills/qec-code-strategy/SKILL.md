---
name: qec-code-strategy
description: Select and reason about quantum error-correcting codes and logical operations in a hardware-agnostic way. Use for surface/color/LDPC/bosonic code tradeoffs, transversal gates, code switching, state preparation, logical error budgets, and decoder/control requirements.
---

# QEC Code Strategy

Do not select a code by popularity, asymptotic parameters alone, or vendor.

## Capture assumptions first

- physical error model, bias, leakage, and relevant correlations;
- connectivity, dimensionality, locality, and transport model;
- physical gate, measurement, reset, and syndrome-extraction cycle times;
- target total logical failure probability and workload duration;
- logical gate set and dominant logical operations;
- how logical measurements/gates alter checks, boundaries, detector models, or code blocks;
- classical decoding latency/throughput budget and available decoder compute;
- logical-measurement/feed-forward deadlines;
- available physical-qubit scale and classical interconnect constraints.

## Compare executable logical architectures

Compare code families **together with their logical-operation strategy** on:
- threshold / below-threshold behavior under the stated noise model;
- encoding rate and distance scaling;
- syndrome-extraction depth and detector production rate;
- transversal/native logical gates;
- lattice-surgery, deformation, teleportation, or code-switching overhead;
- state-preparation and logical-measurement protocols;
- magic-state requirements and factory interfaces;
- decoder accuracy, tail latency, memory, communication, and parallelism;
- whether logical operations require changing decoding graphs/models;
- classical feed-forward critical paths;
- physical qubits, spacetime volume, and wall-clock runtime.

A high-rate code with expensive decoding or logical operations can lose to a lower-rate code at system level. Conversely, a slower physical modality may permit sophisticated software decoding without specialized hardware.

## Decoder feasibility is a code-selection constraint

Before accepting a QEC strategy, estimate:
- syndrome bytes/events generated per cycle;
- simultaneous live code blocks;
- target p99/p99.9 decode deadline where relevant;
- buffering/look-ahead needed by the decoder;
- backlog stability under logical-operation bursts;
- failure semantics when decoding does not converge.

Route experimental threshold/logical-error work to `qec-simulation-decoding`. Route sustained online execution requirements to `real-time-qec-decoding`.

## Tools

Useful tooling includes MQT QECC for QEC synthesis/decoding/logical-compilation studies and TQEC for topological/surface-code design automation. Verify current APIs before implementation and do not infer support for a code/protocol from a neighboring module.

## Implementation gate

Before selecting or coding a QEC architecture, load `references/implementation.md`. It defines the machine model, candidate record, measured-data distance selection, detector-rate calculation, logical-ISA completeness check, and acceptance criteria.

Also apply `../quantum-operations/references/implementation-contract.md`. Do not compare code-family labels without concrete logical operations, decoder, syndrome circuit, and error model.
