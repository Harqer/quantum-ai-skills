---
name: fault-tolerant-verification
description: Verify optimized and fault-tolerant quantum designs with equivalence checking, stabilizer/detector validation, logical-observable checks, ancilla cleanup, and resource-regression tests. Use after structural or QEC transformations.
---

# Fault-Tolerant Verification

Verify every transformation in layers. Use exact circuit equivalence for exact rewrites and an explicitly configured approximate-equivalence relation only when the algorithm specification includes an approximation budget. Use MQT QCEC where its supported circuit semantics match the candidate, Stim for detector and logical-observable validation on stabilizer/QEC circuits, and direct algebraic or state-based checks for small phase-sensitive gadgets and ancilla contracts.

Extend functional verification to the fault-tolerant claims themselves. For toric-code candidates, verify the periodic lattice/check convention, CSS commutation, canonical logical-loop symplectic relations, syndrome-defect endpoints, and residual homology: zero syndrome establishes return to the codespace, while trivial residual homology establishes logical success. Check logical operators, detector definitions, fault propagation, state-preparation conditions, clean and dirty ancilla restoration, and the stated fault-tolerance order or noise model. Maintain known-answer and property tests for primitives and complete algorithms, then add resource regressions for logical width, non-Clifford count and depth, QEC cycles, classical decoding load, and physical estimates so a semantically correct optimization also satisfies the intended engineering envelope.

## Implementation gate

Load `references/implementation.md` before declaring a candidate verified, and use `references/tools.md` as the source/version index. The implementation reference defines exact and approximate QCEC workflows, dynamic-circuit handling, clean and dirty ancilla tests, detector checks, single-fault gadget tests, and resource regressions. Apply `../quantum-operations/references/implementation-contract.md` and treat a verification result as complete when the selected checker establishes the requested equivalence relation and every required invariant passes.
