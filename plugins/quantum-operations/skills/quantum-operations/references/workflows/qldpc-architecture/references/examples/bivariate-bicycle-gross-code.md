# Bivariate-bicycle [[144,12,12]] Gross code: reproduction record

This example is an implementation record for the finite BB code used in Bravyi et al., *High-threshold and low-overhead fault-tolerant quantum memory*. It demonstrates the level of detail required before a qLDPC candidate enters resource estimation.

## Source parameters

The public reference implementation labels this instance `[[144,12,12]]` and sets:

~~~text
ell = 12
m = 6
a = (3, 1, 2)
b = (3, 1, 2)
n = 2 * ell * m = 144
~~~

Using cyclic shifts `x` on the order-12 coordinate and `y` on the order-6 coordinate:

~~~text
A = x^3 + y + y^2
B = y^3 + x + x^2
Hx = [A | B]
Hz = [B^T | A^T]
~~~

The published/reference parameter record is `[[144,12,12]]`: 144 data qubits, 12 logical qubits, distance 12.

Primary paper/preprint:
https://arxiv.org/abs/2308.07915

Reference implementation:
https://github.com/sbravyi/BivariateBicycleCodes

## Construct the same code with qldpc

Current qLDPC documentation includes the same order/polynomial pair:

~~~python
from sympy.abc import x, y
from qldpc import codes

code = codes.BBCode(
    {x: 12, y: 6},
    x**3 + y + y**2,
    y**3 + x + x**2,
)

assert code.dimension == 12
~~~

The current documentation reports this as a 144-data-qubit BB code with 12 logical qubits. Its layout example reports a best-known folded-layout maximum communication distance of about 7.211 grid units for that layout search.

Reference:
https://qldpc.readthedocs.io/examples/bivariate_bicycle_codes.html

## Reproduce Hx and Hz directly

~~~python
import numpy as np

ell, m = 12, 6
I_ell = np.eye(ell, dtype=np.uint8)
I_m = np.eye(m, dtype=np.uint8)

x = {
    i: np.kron(np.roll(I_ell, i, axis=1), I_m) % 2
    for i in range(ell)
}
y = {
    i: np.kron(I_ell, np.roll(I_m, i, axis=1)) % 2
    for i in range(m)
}

A = (x[3] + y[1] + y[2]) % 2
B = (y[3] + x[1] + x[2]) % 2

Hx = np.hstack([A, B]) % 2
Hz = np.hstack([B.T, A.T]) % 2

assert Hx.shape == (72, 144)
assert Hz.shape == (72, 144)
assert not np.any((Hx @ Hz.T) % 2)
~~~

The commuting-circulant construction makes the CSS commutation identity explicit.

## Verify k independently

Compute binary ranks over GF(2), rather than NumPy real-valued rank:

~~~python
def gf2_rank(matrix: np.ndarray) -> int:
    a = (matrix.copy() & 1).astype(np.uint8)
    rows, cols = a.shape
    rank = 0
    for col in range(cols):
        pivots = np.flatnonzero(a[rank:, col])
        if len(pivots) == 0:
            continue
        pivot = rank + int(pivots[0])
        a[[rank, pivot]] = a[[pivot, rank]]
        for row in range(rows):
            if row != rank and a[row, col]:
                a[row] ^= a[rank]
        rank += 1
        if rank == rows:
            break
    return rank

k = 144 - gf2_rank(Hx) - gf2_rank(Hz)
assert k == 12
~~~

## Verify sparsity

Each polynomial has three monomials. Each BB stabilizer therefore has weight 6 for this construction. Verify the concrete matrices rather than inheriting that property by name:

~~~python
assert set(Hx.sum(axis=1).tolist()) == {6}
assert set(Hz.sum(axis=1).tolist()) == {6}
assert set(Hx.sum(axis=0).tolist()) == {3}
assert set(Hz.sum(axis=0).tolist()) == {3}
~~~

Across X and Z checks, each data qubit participates in six checks total.

## Distance provenance

Use the paper/reference implementation for the exact `d=12` parameter or reproduce it with an exact distance certificate/solver. The current `qldpc` method `get_distance_bound(num_trials=...)` is documented as an upper-bound search, so a successful heuristic search supplies a bound rather than an exact-distance proof.

Store:

~~~text
distance:
  value: 12
  provenance: Bravyi et al. / reference instance
  independent_exact_certificate: <path or null>
  heuristic_upper_bound: <value or null>
~~~

## Syndrome-extraction resource record

The BB memory protocol uses 144 data qubits plus one syndrome/check ancilla per stabilizer location, for 288 physical qubits in the reference memory example. The public implementation pipelines X- and Z-check measurement through eight time steps, with preparation/measurement overlapping the six check-data interactions. The preprint describes the entangling syndrome circuit with its own depth convention; record both the CNOT/entangling depth and full repeated-cycle depth explicitly.

Build the schedule from the published/reference implementation rather than inventing a generic weight-6 ordering. Then verify:
- no data/check interaction conflict inside a layer;
- one complete X and Z syndrome is produced per repeated cycle;
- stabilizer transformation matches `Hx` and `Hz`;
- single physical faults propagate within the claimed circuit-distance behavior;
- reset/measurement/idle and leakage assumptions match the target hardware.

Reference implementation:
https://github.com/sbravyi/BivariateBicycleCodes/blob/main/decoder_setup.py

## Circuit-level decoder experiment

Treat the complete repeated syndrome circuit as the source of detector/error mechanisms. The paper's decoder setup constructs decoding matrices from faults inserted at circuit locations; a production reproduction may encode the same circuit in Stim or another detector framework as long as the noise process and detector/logical observables are preserved.

Use BP+OSD as a baseline and BP+LSD as a parallelizable comparison point:

~~~python
from ldpc import BpOsdDecoder
from ldpc.bplsd_decoder import BpLsdDecoder

bp_osd = BpOsdDecoder(
    H_detector,
    error_channel=list(error_priors),
    bp_method="product_sum",
    max_iter=max_iter,
    schedule="serial",
    osd_method="osd_cs",
    osd_order=2,
)

bp_lsd = BpLsdDecoder(
    H_detector,
    error_channel=list(error_priors),
    bp_method="product_sum",
    max_iter=max_iter,
    schedule="serial",
    lsd_method="lsd_cs",
    lsd_order=0,
)
~~~

Confirm the exact constructor names/arguments against the installed `ldpc` version before execution; current documentation is version 2.1.0.

For each physical error point report shots, logical failures, confidence interval, decoder mean/p99/p99.9 latency, throughput, and fallback/convergence behavior. A memory threshold/result is valid only for the stated circuit and noise model.

## Hardware-routing record

Build a placement for all 288 data/check qubits and map the six incident data-check edges per check. Record:
- native versus long-range edges;
- maximum and distribution of communication distances;
- routing/transport layers;
- added error and time per nonlocal interaction;
- parallel-conflict/crosstalk restrictions;
- resulting syndrome-cycle time.

This is the point at which the nominal high encoding rate becomes a hardware-level overhead claim.

## Logical-computation status

This Gross-code reproduction establishes an executable **memory** candidate. It does not, by itself, establish universal fault-tolerant computation.

For a compute architecture, complete the logical ISA using the qLDPC logical-operation literature:
- automorphism-based or transversal Clifford gates where proven for the selected code;
- dynamic syndrome circuits for shift automorphisms where applicable;
- generalized surgery, code switching, teleportation, or a heterogeneous code boundary for missing Clifford/addressable operations;
- magic-state injection/factories or a specialized qLDPC magic-state construction for non-Clifford gates.

Feed the final operation costs into the runtime scheduler and resource estimator.

## Acceptance output

The completed record for this example should contain:

~~~text
code:
  family: bivariate-bicycle
  n_data: 144
  k: 12
  d: 12
  Hx/Hz hashes
  row/column weights

qec:
  syndrome_ancillas: 144
  total_memory_qubits_before_routing_extras: 288
  schedule
  cycle_time
  detector model

decoder:
  algorithm/config
  logical-error curve
  confidence intervals
  mean/p99/p99.9 latency
  throughput

hardware:
  placement
  nonlocal/routed edges
  movement/routing cost
  routing error/time

logical_isa:
  operation -> protected protocol

resources:
  physical qubits
  classical decoder resources
  wall-clock and spacetime volume
  failure budget
~~~

Only after this record and the corresponding surface-code record share the same workload, hardware/noise assumptions, and target failure probability should their overheads be compared.
