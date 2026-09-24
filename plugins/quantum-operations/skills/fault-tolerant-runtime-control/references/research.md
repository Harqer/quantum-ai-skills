# Fault-tolerant runtime-control research notes

## Frame tracking and slow diagnostics

- Chamberland, Iyer, Poulin, **Fault-Tolerant Quantum Computing in the Pauli or Clifford Frame with Slow Error Diagnostics** (2017), arXiv:1704.06662.
  - Establishes why logical corrections can often be tracked in software rather than physically applied immediately.
  - Also shows that slow diagnostics interact with logical-gate execution and cannot be ignored by the runtime design.

## Measurement-assisted uncomputation

- Craig Gidney, **Halving the cost of quantum addition** (2017/2018), arXiv:1709.06648.
  - Temporary logical-AND uses four T gates to compute an AND into an ancilla and can erase the ancilla later without another four T gates by measurement-assisted cleanup.
  - This is a specific proven gadget, not permission to measure arbitrary coherent workspace.

- Liu, Zhou, Meng, **Quantum Uncomputation of Clean and Dirty Ancilla Qubits** (2026), arXiv:2608.09578.
  - Reinforces that valid uncomputation has nontrivial dependency/structure requirements, particularly for dirty ancillas.

## Dynamic control

- Fault-tolerant circuits generally combine unitary operations, projective measurements, and classically controlled operations. Runtime correctness therefore includes the classical dependency graph, not only quantum gate equivalence.

## WCA example

- Ye, Maksymov, Delfosse, arXiv:2608.25027.
  - WCA keeps a logical Clifford frame and determines which logical Pauli representative to measure after conjugating through that frame.
  - Logical measurement outcomes are on the execution critical path.
  - Treat these as an example of frame-based control, not a universal instruction set.

## Verification note

For small circuits, independently compare a frame-tracked implementation with an equivalent implementation that applies explicit corrections. For large FT schedules, validate update rules algebraically and with stabilizer/detector simulation where applicable.
