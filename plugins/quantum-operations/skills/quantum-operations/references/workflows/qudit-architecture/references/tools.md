# Qudit implementation tools and access boundaries

## Native trapped-ion experiments

The strongest native-qudit demonstrations currently come from research hardware rather than a standard OpenQASM qudit ABI.

40Ca+:
- local optical transitions at 729 nm.
- light-shift entangler using approximately 401 nm beams near a motional mode.
- native qudit entanglement demonstrated through d=5.

137Ba+:
- digital qudit states drawn from S_1/2 and D_5/2 manifolds.
- 1762 nm star-topology optical transitions in the 25-level experiment.
- RF multitone control within D_5/2 in the d=5 and d=8 Grover experiment.

171Yb+:
- four-level ququarts demonstrated in an eight-ion processor using E2 optical transitions at 435 nm.

## Quantinuum

Public hardware: H2 and Helios trapped-ion QCCD systems.
Programming: Guppy, pytket and QIR through Quantinuum Nexus.

Current public documentation is qubit-oriented. Verify provider-specific qudit access before assuming the qutrit and qudit experiments can be submitted through the standard customer interface.

https://docs.quantinuum.com/systems/

## qBraid and OpenQuantum

The connected qBraid device catalog checked September 2026 exposes QPUs through qubit-oriented QASM, Qiskit, Braket and IonQ formats. Use it for device discovery and qubit workloads. Native-qudit execution requires an interface that explicitly exposes d-level controls.

## Superconducting qutrits

Qiskit or OpenQASM logical access alone is insufficient. Proven qutrit and transient-level paths depend on pulse-level control or provider-calibrated custom gates that address the 1-2 transition and multilevel interactions.

Treat archived ibmq_jakarta results as evidence for the ternary Toffoli mechanism rather than a currently executable backend.

## Bosonic GKP qudits

The 2025 beyond-break-even GKP result is a custom circuit-QED experiment rather than a commodity cloud backend. Reproduction requires a high-Q three-dimensional cavity, a dispersively coupled transmon ancilla, calibrated oscillator displacements and ECD gates, transmon rotations and repeated ancilla reset.

## Simulation

Represent a qudit directly as a d-dimensional state/tensor when the simulator supports it. Otherwise embed it into ceil(log2(d)) qubits and mark unused binary states invalid. Embedded binary simulation verifies the logical mapping but does not reproduce the real multilevel pulse-control advantage.
