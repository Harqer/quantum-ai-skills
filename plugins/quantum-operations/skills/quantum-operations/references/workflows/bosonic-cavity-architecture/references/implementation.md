# Bosonic cavity architecture: implementation reference

## Candidate record

Record explicitly:

    platform
    physical_mode
    oscillator_frequency
    encoding_family
    logical_dimension
    codewords_or_stabilizers
    simulation_cutoff
    mean_photon_or_phonon_number
    state_preparation
    native_gaussian_controls
    native_nongaussian_controls
    ancilla_type
    ancilla_mode_coupling
    two_mode_or_interregister_gate
    measurement
    reset
    stabilization_or_qec
    loss_rate
    dephasing_or_heating_rate
    leakage_definition
    gate_durations
    measured_fidelities
    programming_interface
    experimental_reference
    evidence_status

evidence_status must be one of: demonstrated, experimentally_supported_extension, proposal, information_theoretic_only.

## Core oscillator model

Use a, a^dagger, n=a^dagger a. A simulation truncation N_cut represents |0>...|N_cut> and is not a physical dimension claim.

Displacement:

    D(alpha) = exp(alpha a^dagger - alpha* a)

SNAP-style phase:

    S({theta_n}) = sum_n exp(i theta_n) |n><n|

For a lossy cavity, include at minimum the Lindblad term

    d rho/dt = -i[H,rho] + kappa D[a](rho)

and add dephasing/thermal terms when supported by the hardware model. Verify convergence by increasing N_cut until requested observables and leakage change less than a declared tolerance.

## Encodings

### Cat/binomial-style encodings

Treat the codewords, parity/error syndromes, mean occupation, correction interval, and recovery/stabilization as part of the resource model. Do not equate a multi-component cat state with an equal-dimensional freely programmable qudit unless logical basis preparation, a universal or workload-sufficient logical gate set, measurement, and QEC are available.

### GKP qudits

For ideal square GKP dimension d:

    ell_d = sqrt(pi*d)
    S_X = D(ell_d)
    S_Z = D(i*ell_d)
    X_d = D(sqrt(pi/d))
    Z_d = D(i sqrt(pi/d))

Finite-energy implementations require an explicit envelope/energy model and repeated stabilization. For superconducting-cavity implementations, include the nonlinear ancilla and ECD/ancilla-control schedule. Dimension d remains an engineering variable; never extrapolate demonstrated d=3 or d=4 memory results directly to d=256.

## MUST

- preserve the exact workload semantics and coherent input/output dimension;
- distinguish capacity, simulation cutoff, encoded logical dimension, demonstrated control, and FT logical dimension;
- charge control ancillas, readout modes, pumps, resets, stabilization and QEC;
- model loss plus platform-relevant dephasing/heating and ancilla-induced errors;
- report oscillator energy/occupation and a justified simulation cutoff;
- identify a concrete inter-register operation before claiming scalable arithmetic;
- verify leakage and code-space return after every logical gadget;
- state whether public/programmatic hardware access exposes the required controls.

## MUST NOT

- call the oscillator's formally infinite Hilbert space freely usable memory;
- infer k logical bits per cavity from a chosen Fock cutoff;
- claim d=16, d=256, or 32-bit-per-cavity packing without a concrete encoding and workload-sufficient controls;
- treat a cavity count as a physical-device count while omitting transmons/readout/pumps;
- treat SNAP/displacement universality in a truncated ideal oscillator as fault-tolerant logical universality;
- reuse qubit Pauli error rates as a bosonic noise model without a justified effective channel;
- reset or measure a mode carrying coherent live data merely to simplify arithmetic;
- extrapolate single-mode memory demonstrations into multi-mode fault-tolerant processors without labeling the extrapolation.

## Verification

For every candidate test:
1. codeword orthogonality/normalization to tolerance;
2. logical truth table or unitary on the code space, including relative phases;
3. leakage after each gadget and after recovery;
4. stabilizer/logical-Pauli expectation values where applicable;
5. convergence versus N_cut;
6. noisy-channel sensitivity to loss/dephasing/heating;
7. ancilla reset/disentanglement;
8. independent equivalence to the original workload;
9. a resource ledger separating logical modes, control ancillas, readout modes, QEC cycles, pulse depth, runtime, and energy.

Reject width wins that disappear after required ancillas/QEC are charged, or that depend on an undemonstrated logical dimension.
