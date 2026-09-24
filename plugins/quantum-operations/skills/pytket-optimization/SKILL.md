---
name: pytket-optimization
description: Use pytket passes for circuit resynthesis, Clifford/Pauli/phase-gadget simplification, rebasing, placement, routing, and explicit compiler pipelines. Use as a measured compiler layer, not a one-click oracle.
---

# pytket Optimization

Build explicit pass sequences and retain checkpoints.

- Consider `FullPeepholeOptimise`, `CliffordResynthesis`, `CliffordSimp`, `OptimisePhaseGadgets`, `PauliSimp`/`GreedyPauliSimp`, KAK-style resynthesis, and rebasing where their preconditions fit.
- Apply strong unconstrained logical optimization before hard architecture constraints unless the target problem demands co-optimization.
- Route/map only when a physical/logical architecture is actually part of the question.
- Re-run cleanup after routing/mapping.
- Some Pauli simplification passes do not preserve global phase; decide whether that is acceptable before use.
- Compare multiple pipelines under identical constraints; never accept a lower abstract gate count if FTQC cost worsens.

See `references/tools.md`.

## Implementation gate

Before writing a pytket pipeline, load `references/implementation.md`; use `references/tools.md` only as a link/version index. The implementation reference defines explicit `SequencePass`, `AutoRebase`, architecture routing, checkpoints, phase cautions, and independent verification.

Also apply `../quantum-operations/references/implementation-contract.md`.
