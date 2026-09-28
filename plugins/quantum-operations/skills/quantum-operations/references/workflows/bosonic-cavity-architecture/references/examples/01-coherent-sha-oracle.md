# Example: exact coherent SHA-256 oracle on bosonic hardware

Target semantic map:

    |m>|y> -> |m>|y XOR SHA256(m)>

with arbitrary coherent 440-bit m and arbitrary coherent 256-bit y.

## Capacity statement

The logical input/output space has dimension 2^696. This is a semantic requirement only.

An oscillator has a formally infinite Fock basis, but this does not justify one oscillator, 22 word modes, 87 byte modes, or any other packed count without a concrete encoded logical dimension and workload-sufficient controls.

## Candidate evaluation

For each proposed bosonic encoding:
1. specify code family and demonstrated logical dimension d;
2. specify mean occupation/energy and simulation cutoff independently;
3. specify logical preparation, measurement, reset, and stabilization/QEC;
4. specify the nonlinear ancilla and inter-mode gate required by reversible SHA arithmetic;
5. compile at least one exact nonlinear SHA gadget and one modular-addition gadget;
6. verify truth table, phases, leakage, ancilla restoration, and noisy behavior;
7. compare total storage modes + nonlinear ancillas + readout modes + QEC overhead against the binary/qudit baseline.

A d=3 or d=4 demonstrated GKP memory may be costed at that demonstrated dimension under matching assumptions. A hypothetical d=256 GKP/binomial/cat mode must remain proposal or information_theoretic_only until the required logical controls and QEC are established.

## Acceptance condition

A bosonic width reduction is accepted only if the complete hardware-aware ledger improves a requested resource while preserving the exact coherent XOR oracle. Otherwise report the capacity bound separately and retain the executable baseline.
