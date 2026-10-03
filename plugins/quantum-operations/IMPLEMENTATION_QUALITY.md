# Implementation Quality Standard

Quantum Operations exposes one concise cataloged router and keeps implementation-grade specialist workflows under its references tree.

## Instruction style

Write skill guidance as affirmative, action-oriented prose. Put the decision rule in `workflow.md`; put equations, exact algorithms, APIs, code, verification, and failure boundaries in `references/implementation.md` and worked examples. Keep provider observations separate from portable transformations.

## Acceptance rule

A routed workflow is implementation-ready only when it supplies explicit inputs/outputs, semantic and hardware/QEC preconditions, exact algorithm/circuit/API steps, a concrete nontrivial example, verification/invariants, unsupported/failure cases, and tool-version checking for version-sensitive APIs.

The authoritative checklist is `skills/quantum-operations/references/implementation-contract.md`.

## Added gate-reduction coverage

| Workflow | Implementation layer |
| --- | --- |
| algorithmic-gate-compression | problem-contract replacement rules + Floquet worked example |
| qubit-reuse-compilation | causal-cone ordering + MCMR rewrite + Quantinuum HyperTKET example |
| tensor-t-optimization | signature tensors + factorization/resynthesis + Circuit-to-Tensor example |
| native-entangler-synthesis | canonical 2Q lowering + parameterized entanglers + Quantinuum examples |

These complement the existing semantic-gate-reduction, reversible-arithmetic, boolean-fusion, ancilla-lifetime, Clifford+T, QEC, scheduling, resource-estimation, verification, interoperability, and Fire Opal workflows.

## Review test

Before coding, a fresh reviewer must be able to answer:
1. What exact representation enters?
2. What exact object leaves?
3. What conditions make the transformation legal?
4. What algorithm/circuit/API sequence implements it?
5. Which example demonstrates the non-obvious steps?
6. What independent test proves the result?
7. Which cases are unsupported or route elsewhere?
8. Which external API facts must be revalidated?

A provider runtime optimization is documented as a measured backend behavior unless the user can explicitly invoke/configure it. An alternative algorithm is never presented as an exact circuit rewrite unless equivalence is actually proved.
