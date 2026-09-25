---
name: pytket-optimization
description: Use pytket passes for circuit resynthesis, Clifford/Pauli/phase-gadget simplification, rebasing, placement, routing, and explicit compiler pipelines. Use as a measured compiler layer with checkpoints and independent verification.
---

# pytket Optimization

Build explicit pass sequences and preserve checkpoints between logical optimization, rebasing, architecture routing, and post-routing cleanup. Select `FullPeepholeOptimise`, `CliffordResynthesis`, `CliffordSimp`, phase-gadget or Pauli simplification, KAK-style resynthesis, and rebasing according to their documented preconditions, then measure gate counts, native two-qubit cost, depth, non-Clifford demand, and wire mappings after each stage.

Apply the strongest architecture-independent simplification before hard mapping when that matches the workload, and move architecture constraints earlier when co-optimization is part of the design. After placement or routing, run the appropriate cleanup and final rebase for the selected native set. Treat global-phase semantics as an explicit equivalence choice for Pauli-oriented passes, then compare multiple pipelines under identical constraints and carry the strongest Pareto candidates into independent verification and FTQC costing.

## Implementation gate

Load `references/implementation.md` before writing a pytket pipeline, and use `references/tools.md` as the source/version index. The implementation reference defines explicit `SequencePass`, `AutoRebase`, architecture routing, checkpoints, phase handling, and independent verification. Apply `../quantum-operations/references/implementation-contract.md` so every pass is chosen from current API semantics and measured against the actual FTQC objective.
