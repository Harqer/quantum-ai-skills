# Algorithmic gate compression: implementation reference

## Contract

Input records the problem specification, required equivalence relation, error/success target, baseline algorithm/resource model, and target hardware capabilities. Output records the candidate algorithm, equivalence class, proof/validation, width, native gate/2Q count, depth, measurement/feed-forward, and error/success model.

## Procedure

1. Identify the dominant scaling term: Trotter steps, oracle calls, arithmetic repetitions, amplitude amplification, synthesis precision, or repeated state preparation.
2. Search for a transformation at the mathematical/algorithmic layer.
3. Derive asymptotic and finite-instance cost using the same resource model.
4. Establish the required equivalence relation.
5. Lower baseline and candidate through the same downstream hardware model.
6. Keep the candidate only if it improves the requested Pareto objective after conversion overhead.

## Floquet adiabatic specialization

For a classical target Hamiltonian with commuting endpoint terms, use
```text
W_s(dt) =
  product_(j,k in E) exp(+i s dt Z_j Z_k)
  product_j          exp(-i (1-s) dt X_j)
```
Fix finite `dt` and use `M=T/dt` steps while varying `s` slowly. This produces a Floquet Hamiltonian and is an alternative algorithm for the same classical optimization objective under the paper's assumptions, not exact simulation of the original continuous-time path.

For Max-Cut each step contains one parameterized ZZ interaction per edge and one X rotation per vertex. On hardware with native parameterized ZZ, lower directly.

## Verification

Exact candidates require exact circuit/function equivalence. Objective-equivalent candidates require objective/success validation against the declared criterion. Compare finite native resources, not only asymptotics.

## Failure boundaries

Do not use Floquet replacement for exact cryptographic functions, arbitrary nonclassical target Hamiltonians, or tasks requiring the original continuous-time unitary.
