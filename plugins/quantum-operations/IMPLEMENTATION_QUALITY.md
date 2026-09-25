# Implementation Quality Standard

Quantum Operations exposes one concise cataloged router and keeps implementation-grade specialist workflows under its references tree.

## Instruction style

Write skill guidance as affirmative, action-oriented prose. State the representation to build, the transformation to apply, the proof or validation to run, the condition that enables a technique, and the result that establishes completion. Prefer smooth paragraphs for the routing and decision layer, while equations, code, tables, and compact procedural structures remain available in implementation references when they make the mechanics clearer.

When a technique has a limited validity domain, describe the valid domain and the alternative path for other cases. This keeps constraints precise while giving the agent a concrete next action.

## Acceptance rule

A routed workflow is considered implementation-ready for a technique only when the material loaded for that technique satisfies:

- explicit inputs and outputs;
- semantic and hardware/QEC preconditions;
- exact algorithm, equations, circuit, or executable API path;
- a concrete worked example when the technique is nontrivial;
- verification/invariants;
- unsupported/failure cases;
- explicit tool-version checking for version-sensitive APIs.

The authoritative checklist is:
[skills/quantum-operations/references/implementation-contract.md](skills/quantum-operations/references/implementation-contract.md).

If one of these elements is missing for the requested technique, the agent researches the primary source/current API and extends the workflow reference before treating the implementation as production-ready.

## Coverage

| Skill | Implementation layer |
| --- | --- |
| quantum-operations | router + `references/implementation-contract.md` |
| semantic-gate-reduction | `references/workflows/semantic-gate-reduction/workflow.md` + `workflow references/implementation.md` |
| boolean-fusion | `references/workflows/boolean-fusion/workflow.md` + `workflow references/implementation.md` |
| ancilla-lifetime | `references/workflows/ancilla-lifetime/workflow.md` + `workflow references/implementation.md` |
| reversible-arithmetic | `references/workflows/reversible-arithmetic/workflow.md` + `workflow references/implementation.md` + exact Cuccaro/temp-AND examples |
| clifford-t-optimization | `references/workflows/clifford-t-optimization/workflow.md` + `workflow references/implementation.md` |
| pyzx-optimization | `references/workflows/pyzx-optimization/workflow.md` + `workflow references/implementation.md` + tools index |
| pytket-optimization | `references/workflows/pytket-optimization/workflow.md` + `workflow references/implementation.md` + tools index |
| qec-code-strategy | `references/workflows/qec-code-strategy/workflow.md` + `workflow references/implementation.md` |
| qec-simulation-decoding | `references/workflows/qec-simulation-decoding/workflow.md` + `workflow references/implementation.md` + tools index |
| real-time-qec-decoding | `references/workflows/real-time-qec-decoding/workflow.md` + research + exact DEM/Tanner, Walking Cat, BeamSearch examples |
| lattice-surgery | `references/workflows/lattice-surgery/workflow.md` + `workflow references/implementation.md` + tools index |
| magic-state-factories | `references/workflows/magic-state-factories/workflow.md` + `workflow references/implementation.md` |
| fault-tolerant-runtime-control | `references/workflows/fault-tolerant-runtime-control/workflow.md` + `workflow references/implementation.md` + research |
| ftqc-runtime-scheduling | `references/workflows/ftqc-runtime-scheduling/workflow.md` + `workflow references/implementation.md` + research |
| ftqc-resource-estimation | `references/workflows/ftqc-resource-estimation/workflow.md` + `workflow references/implementation.md` + tools index |
| fault-tolerant-verification | `references/workflows/fault-tolerant-verification/workflow.md` + `workflow references/implementation.md` + tools index |
| ir-interoperability | `references/workflows/ir-interoperability/workflow.md` + `workflow references/implementation.md` |
| fire-opal-adjunct | `references/workflows/fire-opal-adjunct/workflow.md` + `workflow references/implementation.md` |

## Review test

A fresh reviewer should be able to answer these questions before coding:

1. What exact representation enters this technique?
2. What exact semantic object must leave it?
3. What conditions make the transformation legal?
4. What algorithm/circuit/API sequence implements it?
5. Which example demonstrates the non-obvious steps?
6. What independent test proves the result?
7. Which cases are unsupported or require another skill?
8. Which external API facts must be revalidated because they can change?

The documentation passes this standard when every answer comes directly from the loaded skill, implementation reference, worked example, primary specification, or current tool documentation.

## Scope

This standard keeps the single router `SKILL.md` concise. Deep equations, circuits, APIs, and examples live under `references/workflows/` so context is loaded progressively.
