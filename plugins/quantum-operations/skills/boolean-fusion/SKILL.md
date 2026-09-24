---
name: boolean-fusion
description: Optimize XOR/AND-heavy reversible Boolean logic by sharing nonlinear products, cancelling parity work, fusing named Boolean functions, and reducing multiplicative complexity before gate synthesis.
---

# Boolean Fusion

Represent suitable Boolean regions in ANF/XOR-AND form or another explicit exact Boolean IR, then normalize XOR terms modulo 2 and expose repeated nonlinear products. Share a product when the saved nonlinear work outweighs its temporary storage, routing, and cleanup cost, and fuse neighboring Boolean functions when they consume the same versioned source bits. Propagate proven constants and semantic invariants before synthesis so unreachable products and redundant controls disappear at the Boolean level.

Use multiplicative complexity as an intermediate metric and translate the surviving nonlinear structure into Toffoli, CCZ, T-state, ancilla-lifetime, and spacetime costs before selecting a candidate. Preserve the exact reversible map, restore every temporary according to its contract, and verify phase-sensitive quantum implementations independently whenever relative-phase synthesis enters the lowering path.

## Implementation gate

Load `references/implementation.md` before coding Boolean fusion. It defines ANF representation, the exact Möbius transform, reversible synthesis rules, SHA-256 `Ch` and `Maj` identities, product sharing, and verification. Apply `../quantum-operations/references/implementation-contract.md` so the Boolean proof and the quantum-phase proof are both explicit where required.
