# Example 7: native superconducting qutrit control

A superconducting qutrit uses the lowest three levels of one nonlinear circuit as the computational basis.

One experimentally demonstrated compiler decomposes a qutrit unitary into two-state Givens rotations. For each selected two-level subspace:

~~~text
R_ij(theta, phi)
~~~

drive the transition with a calibrated microwave pulse while suppressing leakage and unwanted level shifts.

Verification stack:
- qutrit Clifford randomized benchmarking.
- interleaved RB for selected gates.
- simultaneous RB for crosstalk.
- process tomography for representative operations.
- cycle benchmarking for two-qutrit CSUM.

Experimental evidence:
- 98.89 +/- 0.05% average qutrit Clifford fidelity in a superconducting qutrit control experiment.
- a separate five-qutrit processor demonstrated a two-qutrit CSUM process fidelity of 0.85.

This is a native-qutrit control path, but production use still requires a backend that exposes those calibrated qutrit pulses.
