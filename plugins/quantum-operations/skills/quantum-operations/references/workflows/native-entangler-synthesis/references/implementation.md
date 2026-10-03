# Native entangler synthesis: implementation reference

## Capability record

Record backend, native 1Q/2Q generators, parameter domains, minimum angles, virtual operations, connectivity, parallelism, submission/compile switch, and error/duration-vs-angle behavior.

## Lowering

1. Simplify commuting Pauli rotations and local 1Q gates.
2. Partition maximal two-qubit regions.
3. Compute canonical/nonlocal content (KAK/Cartan coordinates for general SU(4) when applicable).
4. Match directly to an exposed native parameterized entangler.
5. Synthesize only necessary local pre/post rotations.
6. Re-squash local gates and count physical native interactions.

A `CX-RZ(theta)-CX` Pauli gadget can lower to native RZZ when backend definitions match. Derive angle/sign from the target definition.

## Quantinuum

Current Helios docs expose Rxy, virtual Rz, fixed ZZ, parameterized RZZ, measurement/reset. Current H2 docs additionally expose general RXXYYZZ/TK2 when selected at submission. Confirm the exact backend before TK2.

Quantinuum reports arbitrary-angle 2Q gates can roughly halve 2Q gates on applicable circuits. Helios runtime also squashes 1Q gates by default; reported Rxy reductions are ~50% on random mirror and ~25% on phase estimation, but workload dependent and not user-configurable.

## Verification

Prove exact unitary equivalence up to declared global phase; compare native 2Q count/depth; enforce angle floors/rounding; include local rotations and routing/transport; use post-compile/post-runtime stats when available.

## Failure boundaries

Do not transfer H2-only gates to Helios without current support. Do not round small angles away unless both backend threshold and algorithmic error budget permit it.
