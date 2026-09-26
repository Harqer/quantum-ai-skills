# Example 11: explicit stabilizer-measurement circuit primitive

A parity-check matrix does not define circuit-level performance. This example gives the exact ancilla primitive that must be scheduled across the toric lattice.

## Z-type plaquette check

For data qubits `d0..d3` and ancilla `a`:

~~~python
import stim

def measure_z_check(data, ancilla):
    c = stim.Circuit()
    c.append("R", [ancilla])
    for q in data:
        c.append("CX", [q, ancilla])
    c.append("M", [ancilla])
    return c
~~~

The ancilla starts in |0>, receives parity through data-to-ancilla CNOTs, and is measured in Z.

## X-type star check

~~~python
def measure_x_check(data, ancilla):
    c = stim.Circuit()
    c.append("RX", [ancilla])
    for q in data:
        c.append("CX", [ancilla, q])
    c.append("MX", [ancilla])
    return c
~~~

The ancilla starts in |+>, acts as CNOT control, and is measured in X.

## Production lowering

Build the full round by assigning every data-check edge to conflict-free interaction layers, then add:
- `DETECTOR` annotations across repeated measurements;
- logical `OBSERVABLE_INCLUDE` definitions;
- gate/idle/reset/measurement noise;
- the target hardware timing model;
- a validated hook-error ordering.

Verify single-fault propagation and detector determinism before generating a detector error model. Do not treat the isolated four-CNOT primitive as a fault-tolerant toric syndrome schedule by itself.

Stim:
https://github.com/quantumlib/Stim
