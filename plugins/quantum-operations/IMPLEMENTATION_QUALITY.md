# Implementation Quality Standard

Quantum Operations separates concise routing guidance from implementation-grade references.

## Acceptance rule

A skill is considered implementation-ready for a technique only when the material loaded for that technique satisfies:

- explicit inputs and outputs;
- semantic and hardware/QEC preconditions;
- exact algorithm, equations, circuit, or executable API path;
- a concrete worked example when the technique is nontrivial;
- verification/invariants;
- unsupported/failure cases;
- explicit tool-version checking for version-sensitive APIs.

The authoritative checklist is:
[skills/quantum-operations/references/implementation-contract.md](skills/quantum-operations/references/implementation-contract.md).

If one of these elements is missing for the requested technique, the agent must research the primary source/current API and extend the reference before treating the implementation as production-ready.

## Coverage

| Skill | Implementation layer |
| --- | --- |
| quantum-operations | router + `references/implementation-contract.md` |
| semantic-gate-reduction | `references/implementation.md` |
| boolean-fusion | `references/implementation.md` |
| ancilla-lifetime | `references/implementation.md` |
| reversible-arithmetic | `references/implementation.md` + exact Cuccaro/temp-AND examples |
| clifford-t-optimization | `references/implementation.md` |
| pyzx-optimization | `references/implementation.md` + tools index |
| pytket-optimization | `references/implementation.md` + tools index |
| qec-code-strategy | `references/implementation.md` |
| qec-simulation-decoding | `references/implementation.md` + tools index |
| real-time-qec-decoding | research + exact DEM/Tanner, Walking Cat, BeamSearch examples |
| lattice-surgery | `references/implementation.md` + tools index |
| magic-state-factories | `references/implementation.md` |
| fault-tolerant-runtime-control | `references/implementation.md` + research |
| ftqc-runtime-scheduling | `references/implementation.md` + research |
| ftqc-resource-estimation | `references/implementation.md` + tools index |
| fault-tolerant-verification | `references/implementation.md` + tools index |
| ir-interoperability | `references/implementation.md` |
| fire-opal-adjunct | `references/implementation.md` |

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

If any answer requires guessing, the documentation is still ambiguous and fails this standard.

## Scope

This standard does not require every `SKILL.md` to become a textbook. `SKILL.md` remains the routing/decision layer; deep equations, circuits, APIs, and examples live under `references/` so context is loaded progressively.
