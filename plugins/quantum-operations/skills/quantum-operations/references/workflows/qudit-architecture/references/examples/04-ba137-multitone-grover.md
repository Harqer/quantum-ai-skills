# Example 4: 137Ba+ multitone qudit control

The 2026 experiment used one 137Ba+ ion in a surface-electrode trap and selected d=5 or d=8 states from the metastable 5D_5/2 manifold.

Implementation sequence:

1. Enumerate candidate D_5/2 hyperfine states and magnetic-dipole transitions.
2. Select a connected set of d states with strong transitions, lower magnetic sensitivity, and acceptable spectral separation from off-resonant leakage transitions.
3. Generate up to d-1 phase-coherent RF tones with DDS channels.
4. Combine the tones and drive them through trap RF electrodes.
5. Run spectroscopy to locate each transition.
6. Calibrate each transition's Rabi frequency independently.
7. Turn all tones on and optimize amplitudes jointly because simultaneous driving introduces AC Zeeman shifts and other cross-couplings.
8. Use randomized-benchmarking sequences as the objective for the fine calibration.
9. Compile the desired algorithm operation into multitone displacement and SNAP-like pulses.
10. Measure the full qudit population distribution and leakage.

Demonstrated result:

~~~text
d=5 Grover:
  average target-state success: 96.8(3)%
  one-iteration SSO: 99.9(1)%

d=8 Grover:
  average target-state success: 69(6)%
  SSO: 97.1(3)%
~~~

The demonstrated single-qudit Grover implementation avoids inter-particle entangling gates. Multi-qudit workloads require a separately demonstrated entangling primitive.
