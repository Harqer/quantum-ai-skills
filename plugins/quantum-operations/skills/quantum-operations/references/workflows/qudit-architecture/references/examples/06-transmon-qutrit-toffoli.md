# Example 6: transient transmon qutrit for Toffoli reduction

This pattern keeps three logical qubits binary and uses |2> of one or more transmons only during the gate.

Logical contract:

~~~text
input state in {|0>,|1>}^3
temporary transitions may populate |2>
output returns to {|0>,|1>}^3
output truth table and relative phases equal Toffoli
~~~

The 2021 fixed-frequency-transmon experiment implemented an order-preserving Toffoli with four two-transmon operations. The corresponding order-preserving binary decomposition on the same linear topology required eight CNOTs.

Measured average process fidelity on one tested triplet:

~~~text
78.00% +/- 1.93%
~~~

Implementation requirements:
- pulse-level or calibrated custom-gate access to the 1-2 transition.
- calibrated multilevel two-transmon interaction.
- explicit leakage measurement after the gate.
- phase calibration over the computational subspace.

Use this strategy when it lowers the measured entangling error or depth on the actual device. A normal QASM circuit submitted to a modern transmon QPU does not automatically expose this capability.
