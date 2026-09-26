# Example 8: beyond-break-even GKP qutrit and ququart

Hardware:

~~~text
storage: 3D superconducting microwave cavity
control ancilla: tantalum transmon
coupling: dispersive
logical dimension: d=3 or d=4
~~~

For dimension d define:

~~~text
ell_d = sqrt(pi*d)
S_X = D(ell_d)
S_Z = D(i*ell_d)
X_d = D(sqrt(pi/d))
Z_d = D(i*sqrt(pi/d))
~~~

Finite-energy stabilization:

1. Apply echoed conditional displacement ECD pulses and ancilla rotations for one stabilizer direction.
2. Reset the transmon ancilla.
3. Update the cavity phase frame.
4. Repeat for S_X, S_Z, S_X-dagger, S_Z-dagger.
5. Repeat the four-round cycle.

For logical qutrit Pauli measurement, use two binary ancilla measurements to distinguish the three eigenvalues. For the ququart, first resolve even versus odd and then resolve the remaining pair.

Measured QEC gain:

~~~text
qutrit d=3: 1.82 +/- 0.03
ququart d=4: 1.87 +/- 0.03
~~~

This is the preferred demonstrated qudit-QEC reference when the hardware model includes a bosonic cavity.
