# Tensor T optimization: implementation reference

## Supported input

A circuit region reducible to Clifford+T / phase-polynomial form with a well-defined signature tensor. Preserve qubit mapping, Hadamard-gadget boundaries, phase requirements, and any postselection/correction semantics.

## Exact pipeline

1. Normalize the Clifford+T region.
2. Compile non-Clifford blocks to symmetric binary signature tensors.
3. Preserve the original factorization/matrix and qubit mapping.
4. Obtain a lower-rank factorization from AlphaTensor-Quantum, TOpt, or another exact compatible optimizer.
5. Optionally apply published CS/CCZ gadgetization rules.
6. Resynthesize optimized blocks.
7. Reinsert Clifford blocks in original order.
8. Verify the complete result.

For the supported order-3 binary tensor representation, factorization rank maps to phase/T factors. Gadgetization changes T-equivalent cost, so measure after gadget mapping.

## Public implementation boundary

The AlphaTensor-Quantum repository supplies RL research code/demos and published decompositions. Circuit-to-Tensor supplies the practical circuit->tensor and factorization->circuit path. RL training is not required if a published or independently produced valid factorization is available.

## Verification

Run Circuit-to-Tensor/Feynman verification when supported; independently verify small blocks; check mapping/block order; count T, T-depth, CCZ/Toffoli, ancillas, and Clifford 2Q cost; reject unaccounted postselection for deterministic workloads.

## Failure boundaries

Partition dynamic measurement/reset regions and unsupported non-Clifford structures before applying this formalism.
