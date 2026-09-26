# Proven qutrit and qudit implementation research

This map prioritizes experimental demonstrations and current access documentation. Proposal-only higher-dimensional architectures are excluded from the production candidate set.

1. Ringbauer et al., A universal qudit quantum processor with trapped ions, Nature Physics 18, 1053-1057 (2022). 40Ca+ processor, local dimension up to seven, single-qudit benchmarking, qutrit entangling operations and full qudit readout.
   https://doi.org/10.1038/s41567-022-01658-0

2. Hrmo et al., Native qudit entanglement in a trapped ion quantum processor, Nature Communications 14, 2242 (2023). Native light-shift entangler demonstrated for d=2 through d=5 on 40Ca+.
   https://doi.org/10.1038/s41467-023-37375-2

3. Shi et al., Efficient implementation of a quantum algorithm with a trapped ion qudit, Nature Communications 17, 1911 (2026). 137Ba+, multitone d=5 and d=8 Grover algorithm.
   https://doi.org/10.1038/s41467-026-68746-0

4. Low et al., Quantum logic operations and algorithms in a single 25-level atomic qudit, Nature Communications 17, 7098 (2026). 137Ba+ S_1/2 and D_5/2 encoding, 25-level SPAM, star-topology Givens compilation, virtual-qubit algorithm demonstrations.
   https://doi.org/10.1038/s41467-026-72662-8

5. Towards a Multiqudit Quantum Processor Based on a 171Yb+ Ion String: Realizing Basic Quantum Algorithms, Quantum Reports 7, 19 (2025). Eight individually controlled four-level qudits, 435 nm E2 encoding, algorithm demonstrations.
   https://doi.org/10.3390/quantum7020019

6. Morvan et al., Qutrit Randomized Benchmarking, Physical Review Letters 126, 210504 (2021). Five superconducting qutrit processor and two-qutrit CSUM benchmarking.
   https://doi.org/10.1103/PhysRevLett.126.210504

7. Kononenko et al., Characterization of control in a superconducting qutrit using randomized benchmarking, Physical Review Research 3, L042007 (2021). Lowest three levels of a superconducting circuit; 98.89 +/- 0.05% average qutrit Clifford fidelity.
   https://doi.org/10.1103/PhysRevResearch.3.L042007

8. Yurtalan et al., Implementation of a Walsh-Hadamard Gate in a Superconducting Qutrit, Physical Review Letters 125, 180504 (2020). Experimental single-qutrit gate synthesis.
   https://doi.org/10.1103/PhysRevLett.125.180504

9. Galda et al., Implementing a Ternary Decomposition of the Toffoli Gate on Fixed-Frequency Transmon Qutrits, arXiv:2109.00558 (2021). Cloud fixed-frequency transmons; four two-transmon operations versus eight binary CNOTs on linear topology.
   https://arxiv.org/abs/2109.00558

10. Fedorov et al., Implementation of a Toffoli gate with superconducting circuits, Nature 481, 170-172 (2012). Direct experimental proof that a third transmon level can reduce Toffoli decomposition cost.
    https://doi.org/10.1038/nature10713

11. Brock et al., Quantum error correction of qudits beyond break-even, Nature 641, 612-618 (2025). GKP qutrit and ququart in a microwave cavity with transmon ancilla; gains 1.82 and 1.87.
    https://doi.org/10.1038/s41586-025-08899-y

12. Lindon et al., Complete Unitary Qutrit Control in Ultracold Atoms, Physical Review Applied 19, 034089 (2023). Arbitrary SU(3) control with two resonant microwave tones.
    https://doi.org/10.1103/PhysRevApplied.19.034089

13. Meng et al., Experimental realization of high-dimensional quantum gates with ultrahigh fidelity and efficiency, Physical Review A 109, 022612 (2024). Single-photon polarization-spatial ququart gates and controlled X4; reported 99.73% average gate fidelity and 99.47% efficiency.
    https://doi.org/10.1103/PhysRevA.109.022612

14. Iqbal et al., Qutrit toric code and parafermions in trapped ions, Nature Communications 16, 6301 (2025). Z3 toric state up to 24 qutrits on Quantinuum H2, with each qutrit encoded into two physical qubits. Treat as encoded-qudit evidence rather than native-qutrit hardware.
    https://doi.org/10.1038/s41467-025-61391-z

15. Generalized Ramsey interferometry explored with a single nuclear spin qudit, npj Quantum Information 4, 53 (2018). Four-level Tb3+ nuclear-spin qudit with independently addressable transitions; implementation background for multitone nuclear-spin control.
    https://doi.org/10.1038/s41534-018-0101-3

## Current access evidence

Quantinuum public H2 and Helios documentation exposes qubit-native single-qubit rotations and two-qubit ZZ operations through Guppy, pytket, QIR and Nexus. Treat published qudit experiments as special experimental capabilities unless an account or provider interface explicitly exposes qudit controls.

Current qBraid device discovery checked in September 2026 exposes available trapped-ion and superconducting QPUs through qubit-oriented QASM, Qiskit, Braket or IonQ circuit interfaces and reports them in qubits. The connected interface has no native-qudit job format.

Neutral-atom multiqudit entangling control is not yet experimentally demonstrated in the 2026 literature reviewed here. Single-qutrit atomic control is experimental; proposed multiqudit neutral-atom entanglers remain research-only.
