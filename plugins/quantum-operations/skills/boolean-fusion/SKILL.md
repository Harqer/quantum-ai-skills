---
name: boolean-fusion
description: Optimize XOR/AND-heavy reversible Boolean logic by sharing nonlinear products, cancelling parity work, fusing named Boolean functions, and reducing multiplicative complexity before gate synthesis.
---

# Boolean Fusion

- Convert suitable regions to ANF/XOR-AND or another explicit Boolean IR.
- Cancel duplicate XOR terms modulo 2.
- Share repeated product terms only when reuse beats storage/uncomputation cost.
- Fuse adjacent Boolean functions that consume the same source bits.
- Exploit constants and mutually exclusive conditions before synthesis.
- Track multiplicative complexity as an intermediate metric, then translate to Toffoli/CCZ/T-state and spacetime costs.
- Preserve exact reversible semantics and ancilla cleanup.
