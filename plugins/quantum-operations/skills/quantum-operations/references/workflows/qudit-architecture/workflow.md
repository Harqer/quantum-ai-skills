---
name: qudit-architecture
description: Use experimentally demonstrated qutrit/qudit techniques to reduce carrier count, entangling-gate count, ancilla demand, or QEC overhead. Covers native trapped-ion qudits, transient transmon qutrit levels, bosonic GKP qudits, encoded qudits, and proven photonic/atomic qudit controls.
---

# Qudit and Qutrit Architecture

Use qudits only when the selected physical platform exposes the required levels and control operations. A d-level Hilbert space becomes an engineering resource only after state preparation, coherent control, entangling operations when required, readout, leakage handling, and the programming interface are concrete.

Classify every candidate before costing it.

1. Native qudit carrier: one physical ion, atom, photon, or circuit stores one d-level computational unit and the experiment exposes native single-qudit control. Trapped ions currently provide the strongest experimentally demonstrated general-purpose path.
2. Packed virtual qubits in one qudit: map 2^n computational basis states into at least 2^n levels of one carrier. This can reduce carrier and entangling-gate count but increases single-carrier pulse complexity and commonly serializes work that separate qubits could perform in parallel.
3. Transient auxiliary level: the computation remains binary, but an extra physical level such as transmon |2> is used temporarily to synthesize a cheaper multiqubit gate. Count this as gate and ancilla optimization rather than as a new logical qutrit register.
4. Bosonic logical qudit: d logical states are encoded in a harmonic oscillator and actively error corrected. Treat oscillator energy, control ancilla, conditional-displacement gates, and stabilization cycles as physical resources.
5. Encoded qudit on qubits: multiple qubits emulate a qutrit or qudit. This can demonstrate qudit algorithms and QEC semantics but does not reduce physical carrier count.

Prefer experimentally demonstrated protocols. Keep proposal-only multiqudit mechanisms out of the production candidate set unless the user explicitly requests research-only options.

## Proven implementation routes

### Native trapped-ion qudits

Use atomic sublevels of trapped ions as computational states. Demonstrations include universal local processing up to d=7 in 40Ca+, native two-qudit entangling gates through d=5 in 40Ca+, multitone algorithm execution at d=5 and d=8 in 137Ba+, a 25-level 137Ba+ digital qudit with high-fidelity SPAM, and an eight-ion 171Yb+ ququart processor.

For the 40Ca+ light-shift entangler, local rotations use resonant 729 nm pulses between |0> and |j>, while the two-qudit state-dependent force uses two approximately 401 nm beams. The symmetrized entangler implements:

~~~text
G(theta)|jj> = |jj>
G(theta)|jk> = exp(i theta)|jk>, j != k
~~~

and has been experimentally demonstrated for d=2 through d=5.

### Transmon qutrit workspace

Use the third transmon level only where the backend exposes calibrated pulse-level access to the 1-2 transition and the required two-transmon interactions. A demonstrated ternary Toffoli decomposition used four two-transmon operations on fixed-frequency transmons instead of eight order-preserving binary CNOTs on a linear topology. Preserve the logical input/output subspace and verify that final population returns to {|0>,|1>}.

Cloud QASM access to a transmon device does not imply access to its qutrit levels.

### Bosonic GKP qutrit and ququart

Use a long-lived microwave cavity as the oscillator and a transmon ancilla for conditional displacement and control. A 2025 experiment demonstrated beyond-break-even GKP qutrit and ququart memories.

For dimension d:

~~~text
ell_d = sqrt(pi d)
S_X = D(ell_d)
S_Z = D(i ell_d)
X_d = D(sqrt(pi/d))
Z_d = D(i sqrt(pi/d))
~~~

Finite-energy stabilization uses echoed conditional-displacement gates and ancilla rotations, with ancilla reset between rounds.

### Atomic and photonic single-qudit control

Use experimentally demonstrated SU(3) control in ultracold atoms when the workload is dominated by local high-dimensional operations. Use optical ququart gates when polarization-spatial encoding is physically available. These results establish control primitives; they do not by themselves establish scalable fault-tolerant multiqudit computation.

## Access boundary

Hardware capability and public programming access are separate. Mainstream cloud device interfaces currently expose available trapped-ion and superconducting QPUs primarily as qubit gate-model devices through QASM, QIR, Qiskit, Braket, IonQ circuit formats, Guppy, or pytket. Treat native-qudit execution as unavailable through a provider until its public interface exposes the required d-level operations or pulse controls.

## Implementation gate

Load references/implementation.md, references/research.md, references/tools.md, and the smallest relevant worked example. Preserve the binary baseline. Accept the qudit candidate only if it improves a measured resource after charging pulse count, serialization, leakage, SPAM, entangling-gate requirements, QEC, and hardware-access constraints.
