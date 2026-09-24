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

## Implementation gate

Before coding an arithmetic primitive, load `references/implementation.md` and the relevant worked example:
- `references/examples/cuccaro-adder.md` for an exact ripple-carry MAJ/UMA construction;
- `references/examples/temporary-logical-and.md` for measurement-assisted 4-T temporary-AND compute/erase.

Also apply `../quantum-operations/references/implementation-contract.md`. Every arithmetic implementation must state endianness, overflow/modulus semantics, ancilla contracts, and forward/cleanup cost.
