---
name: fault-tolerant-verification
description: Verify optimized and fault-tolerant quantum designs with equivalence checking, stabilizer/detector validation, logical-observable checks, ancilla cleanup, and resource-regression tests. Use after structural or QEC transformations.
---

# Fault-Tolerant Verification

Use layered, independent checks.

- Verify logical pre/post-optimization circuits for exact or explicitly allowed approximate equivalence.
- Use MQT QCEC for circuit/compilation equivalence where compatible; choose exact vs approximate checks deliberately.
- Use Stim detector/observable checks for stabilizer/QEC circuits.
- Check logical operators and fault propagation, not only noiseless functional truth tables.
- Assert ancilla reset/uncompute/disentanglement contracts.
- Maintain known-answer/property tests for reversible primitives and complete algorithms.
- Add resource-regression tests for logical width, non-Clifford counts/depth, cycles, and physical estimates.
- For FT gadgets/state prep, validate the stated fault-tolerance order/model; functional equivalence alone is insufficient.

See `references/tools.md`.

## Implementation gate

Before declaring a candidate verified, load `references/implementation.md`; use `references/tools.md` as a source index. The implementation reference defines exact/approximate QCEC workflows, dynamic-circuit limits, clean/dirty ancilla tests, detector checks, single-fault gadget tests, and resource regressions.

Also apply `../quantum-operations/references/implementation-contract.md`. Inconclusive or unsupported verification is not success.
