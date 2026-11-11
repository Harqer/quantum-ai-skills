---
name: algorithmic-gate-compression
description: Reduce gate complexity by replacing a costly algorithmic realization with a lower-gate method that preserves the requested problem objective, while keeping exact-equivalence and heuristic replacements distinct.
---

# Algorithmic Gate Compression

Use this workflow before circuit synthesis when the dominant gate count comes from the chosen algorithmic realization rather than local gate decomposition.

Record the problem contract first: exact function/unitary, optimization objective, target approximation/error, success criterion, and whether a different algorithm is permitted. Generate alternative mathematical realizations that attack the dominant scaling term, then compare gate count, depth, width, error/success behavior, and hardware-native structure before decomposition.

Classify every candidate as **exact-equivalent** or **problem-equivalent/heuristic**. Exact cryptographic workloads such as SHA-256 require exact-equivalent transformations. Floquet adiabatic evolution is a problem-solving replacement for suitable classical Hamiltonians, not an exact replacement for continuous adiabatic time evolution.

## Implementation gate

Load `references/implementation.md`, `references/research.md`, and the smallest matching example. Prove the stated equivalence relation before accepting the reduction. Route exact reversible substructure to semantic-gate-reduction, reversible-arithmetic, and boolean-fusion after the algorithmic choice is fixed.
