# Implementation Quality Standard

Quantum Operations exposes one concise cataloged router and keeps implementation-grade specialist workflows under its references tree.

## Instruction style

Write skill guidance as affirmative, action-oriented prose. Put routing/decision rules in `workflow.md`; put equations, exact algorithms, APIs, code, verification, and failure boundaries in `references/implementation.md` and worked examples. Keep provider observations separate from portable transformations.

## Acceptance rule

A routed workflow is implementation-ready only when it supplies:

- explicit inputs and outputs;
- semantic and hardware/QEC preconditions;
- exact algorithm, equations, circuit, or executable API path;
- a concrete worked example for nontrivial mechanics;
- verification/invariants;
- unsupported/failure cases;
- explicit tool-version checking for version-sensitive APIs.

The authoritative checklist is:
`skills/quantum-operations/references/implementation-contract.md`.

## Coverage

| Workflow | Implementation layer |
| --- | --- |
| semantic-gate-reduction | semantic IR + legality + exact rewrite verification |
| algorithmic-gate-compression | problem-contract replacement rules + Floquet worked example |
| boolean-fusion | ANF/XOR-AND reduction + multiplicative-complexity verification |
| ancilla-lifetime | liveness + pebbling + cleanup contracts |
| qubit-reuse-compilation | causal-cone ordering + MCMR rewrite + Quantinuum HyperTKET example |
| reversible-arithmetic | exact arithmetic + Cuccaro/temp-AND examples |
| clifford-t-optimization | phase-safe non-Clifford optimization |
| tensor-t-optimization | signature tensors + factorization/resynthesis + Circuit-to-Tensor example |
| native-entangler-synthesis | canonical 2Q lowering + parameterized entanglers + Quantinuum examples |
| pyzx-optimization | ZX transformations + verification |
| pytket-optimization | explicit pass pipelines + checkpoints |
| qec-code-strategy | code selection + logical ISA |
| transversal-teleportation | transversal/teleport/reset/reuse + correlated decoding |
| qldpc-architecture | exact finite qLDPC construction and mapping |
| toric-code-architecture | toric/topological implementation and decoding examples |
| qudit-architecture | experimentally grounded multilevel carrier implementations |
| qec-simulation-decoding | detector/noise/decoder benchmarking |
| real-time-qec-decoding | streaming decoding and deadline engineering |
| lattice-surgery | patch/logical-operation implementation + tools |
| magic-state-factories | distillation/cultivation/catalysis resource model |
| fault-tolerant-runtime-control | frames, measurements, feed-forward, reuse legality |
| ftqc-runtime-scheduling | dependency-aware whole-machine schedule |
| ftqc-resource-estimation | layered logical/classical/physical estimates |
| fault-tolerant-verification | equivalence, detector, logical, ancilla, resource regression |
| ir-interoperability | semantic OpenQASM/QIR/framework translation |
| fire-opal-adjunct | current Fire Opal validation/execution boundary |

## Review test

Before coding, a fresh reviewer must be able to answer:

1. What exact representation enters?
2. What exact semantic object leaves?
3. What conditions make the transformation legal?
4. What algorithm/circuit/API sequence implements it?
5. Which example demonstrates the non-obvious steps?
6. What independent test proves the result?
7. Which cases are unsupported or route elsewhere?
8. Which external API facts must be revalidated?

A provider runtime optimization is documented as measured backend behavior unless the user can explicitly invoke/configure it. An alternative algorithm is never presented as an exact circuit rewrite unless equivalence is actually proved.

## Scope

Keep the single router concise. Deep equations, circuits, APIs, research, and examples live under `references/workflows/` so context is loaded progressively.
