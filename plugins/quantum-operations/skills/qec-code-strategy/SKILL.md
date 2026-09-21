---
name: qec-code-strategy
description: Select and reason about quantum error-correcting codes and logical operations in a hardware-agnostic way. Use for surface/color/LDPC/bosonic code tradeoffs, transversal gates, code switching, state preparation, and logical error budgets.
---

# QEC Code Strategy

Do not select a code by popularity or vendor.

Capture assumptions first:
- physical error model and bias/correlations;
- connectivity/dimensionality/locality;
- measurement/reset speed and reliability;
- target logical failure probability;
- logical gate set and dominant operations;
- classical decoding latency budget;
- available physical-qubit scale.

Then compare code families and logical-operation strategies on:
- threshold / below-threshold regime;
- encoding rate and distance scaling;
- syndrome-extraction depth;
- transversal/native logical gates;
- lattice-surgery or deformation overhead;
- decoder complexity/latency;
- magic-state/code-switching requirements;
- state-preparation and measurement overhead.

Useful tooling includes MQT QECC for QEC synthesis/decoding/logical-compilation studies and TQEC for topological/surface-code design automation. Verify current APIs before implementation.
