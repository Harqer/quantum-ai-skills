---
name: reversible-arithmetic
description: Optimize exact reversible arithmetic for FTQC, including adders, compressors, modular arithmetic, multi-operand sums, constant arithmetic, carry-save forms, and compute/uncompute scheduling.
---

# Reversible Arithmetic

Choose arithmetic structure from the complete workload and declare each primitive's exact semantic contract: register ordering and endianness, overflow or modulus behavior, in-place or out-of-place mapping, control behavior, carry outputs, ancilla contracts, and cleanup semantics. For multi-operand sums, compare carry-save or compressor networks with repeated carry propagation and keep carry-save form across intermediate stages until a semantic boundary requires an ordinary binary word. Specialize known-constant arithmetic from proven constants and propagate those simplifications before gate decomposition.

Compare ripple, prefix/lookahead, measurement-assisted, phase/rotation-based, carry-save, in-place, and out-of-place constructions using logical width, Toffoli/CCZ/T-equivalent cost, non-Clifford depth, Clifford two-qubit cost, measurement/feed-forward depth, ancilla lifetime, and full compute-plus-cleanup cost. Push the candidate arithmetic schedules into resource estimation and runtime scheduling so width, recomputation, factory pressure, and accumulated logical error are evaluated together.

## Implementation gate

Load `references/implementation.md` before coding an arithmetic primitive, then load `references/examples/cuccaro-adder.md` for the exact MAJ/UMA ripple construction or `references/examples/temporary-logical-and.md` for measurement-assisted temporary-AND compute and erase when those patterns match the task. Apply `../quantum-operations/references/implementation-contract.md` so every arithmetic implementation carries explicit endianness, overflow/modulus semantics, ancilla contracts, and forward/cleanup cost.
