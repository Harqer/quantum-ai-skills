---
name: reversible-arithmetic
description: Optimize exact reversible arithmetic for FTQC, including adders, compressors, modular arithmetic, multi-operand sums, constant arithmetic, carry-save forms, and compute/uncompute scheduling.
---

# Reversible Arithmetic

- Choose arithmetic structure from the whole workload, not an isolated adder benchmark.
- For multi-operand sums, compare carry-save/compressor networks against repeated carry propagation.
- Delay carry propagation until a semantic boundary requires ordinary binary form.
- Specialize arithmetic by known constants and eliminate impossible carries/controls.
- Compare ripple, prefix/lookahead, in-place, out-of-place, measurement-assisted, phase/rotation-based, and carry-save constructions under the FTQC cost model.
- Account for both forward and inverse/uncompute cost.
- Optimize ancilla lifetime jointly with gate count and depth.
- Report at least logical qubits, Toffoli/CCZ/T-related cost, Clifford depth, and downstream physical estimate impact.
