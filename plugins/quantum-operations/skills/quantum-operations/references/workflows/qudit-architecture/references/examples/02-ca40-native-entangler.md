# Example 2: 40Ca+ native two-qudit light-shift gate

Hardware record from the 2023 experiment:

~~~text
ions: two 40Ca+
trap: segmented surface Paul trap
ion height: about 110 micrometres
temperature: about 35 K
axial COM: about 1.1 MHz
radial modes: about 3.5 and 3.2 MHz
quantization field: about 3.6 G
local-control wavelength: 729 nm
light-shift wavelength: about 401.2 nm
typical LS pulse: about 35 microseconds
~~~

Implement one local rotation R between |0> and |j> by a resonant 729 nm pulse. Pulse phase sets the rotation axis and pulse area sets the angle.

For the entangler:

1. Prepare the two ions in the selected d-level basis.
2. Apply the state-dependent light-shift pulse U_LS.
3. Apply the cyclic basis permutation X_d.
4. Repeat the U_LS and X_d pattern required to symmetrize state-dependent phases.
5. Tune gate detuning, duration, or optical power to obtain target theta.
6. Verify that equal-index states keep one phase and unequal-index states acquire exp(i theta).

Measured extracted gate fidelities:

~~~text
d=2  99.6(1)%
d=3  98.7(2)%
d=4  97.0(3)%
d=5  93.7(3)%
~~~

The d-dependence is part of the design-space sweep.
