---
name: bosonic-cavity-architecture
description: Model experimentally grounded bosonic oscillator encodings, especially superconducting microwave cavities with nonlinear ancillas, without confusing oscillator Hilbert-space capacity with usable logical dimension.
---

# Bosonic Cavity Architecture

Use this workflow when a workload may store or process quantum information in harmonic-oscillator modes: superconducting microwave cavities/resonators, trapped-ion motion, or photonic/CV modes. For implementation-grade FTQC candidates, prefer hardware whose encoding, controls, measurement/reset, and error-correction path have been experimentally demonstrated.

## Required classification

Classify every claim separately as:

1. **oscillator capacity** -- the ideal harmonic oscillator has an unbounded Fock basis; this is not a realizable logical dimension;
2. **simulation cutoff** -- a numerical truncation N_cut chosen only for simulation convergence;
3. **encoded logical dimension** -- d logical states defined by a concrete code;
4. **demonstrated controllable subspace** -- states and controls actually exercised on hardware;
5. **fault-tolerant logical resource** -- encoded information with an explicit QEC/stabilization and logical-operation path.

Never substitute one category for another.

## Hardware routes

### Superconducting microwave cavity + nonlinear ancilla

Model the storage oscillator and nonlinear ancilla separately. Common demonstrated controls include cavity displacement, dispersive conditional phase/rotation, SNAP-style number-selective phases, echoed conditional displacement (ECD), ancilla rotations/readout/reset, and parametric/engineered dissipation where the device supports them.

A cavity-only carrier count is incomplete. Cost at minimum:
- storage modes;
- transmon/fluxonium or other nonlinear control ancillas;
- readout modes;
- pump/control channels when relevant;
- stabilization/QEC cycles;
- oscillator energy or mean photon number;
- loss/dephasing/leakage;
- gate and reset latency.

### Trapped-ion motion

Treat phonon modes as bosonic oscillators and ion internal states as control/ancilla resources. Cost cooling, motional heating/dephasing, sideband operations, mode crowding, measurement/reset, and any syndrome-extraction cycle. Do not infer public native bosonic programmability merely because a trapped-ion QPU physically has motional modes.

### Photonic/CV modes

Separate propagating optical modes from long-lived memories. Gaussian control alone is not enough for arbitrary reversible Boolean computation; identify the required non-Gaussian resource, measurement/feed-forward, state preparation, loss budget, and error-correcting encoding.

## SHA/reversible-oracle rule

For an exact coherent oracle such as

    |m>|y> -> |m>|y XOR SHA256(m)>

preserve the full coherent input/output dimension. For 440 coherent message bits plus a 256-bit arbitrary target, the semantic Hilbert-space requirement is 2^696.

Do not report ceil(696/log2(d)) cavities unless d is a defensible encoded logical dimension with the required computation, entangling, readout, reset, and QEC path. An infinite oscillator Hilbert space does not make one-cavity SHA a hardware architecture.

For SHA-like workloads, compare at least:
- binary/qudit baseline;
- bosonic memory + nonlinear ancilla hybrid;
- native encoded-bosonic computation only when logical arithmetic primitives are concrete.

Keep information-capacity bounds separate from executable and fault-tolerant resource estimates.

## Implementation gate

Load references/implementation.md and references/research.md. If modifying a reversible workload also load reversible-arithmetic, ancilla-lifetime, qudit-architecture, ftqc-resource-estimation, and fault-tolerant-verification as needed. Accept a bosonic candidate only after the resource ledger includes control ancillas and QEC/stabilization overhead and the logical map is independently verified.
