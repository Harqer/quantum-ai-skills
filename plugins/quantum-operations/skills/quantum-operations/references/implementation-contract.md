# Implementation-grade documentation contract

A routed skill is **implementation-ready** when the loaded material specifies every semantic step required to execute the requested transformation.

Before writing production code from a skill, verify that the loaded skill/reference set provides all applicable items below.

## Required fields

1. **Inputs**
   - representation or file/API type;
   - qubit/register ordering;
   - classical/quantum value assumptions;
   - hardware/QEC assumptions when relevant.

2. **Outputs**
   - exact semantic map;
   - which registers are modified;
   - which ancillas must be restored;
   - resource/metadata output shape.

3. **Preconditions**
   - gate set / IR restrictions;
   - code/noise-model assumptions;
   - clean/dirty ancilla contracts;
   - phase/global-phase requirements;
   - tool version/API assumptions.

4. **Algorithm**
   - equations, gate sequence, or pseudocode precise enough to implement;
   - ordering requirements;
   - termination/commit conditions;
   - exceptional/unsupported cases.

5. **Worked example**
   - at least one small exact example;
   - state/register mapping before and after;
   - expected resource or detector result when applicable.

6. **Verification**
   - executable or algebraic invariant;
   - known-answer test;
   - independent equivalence/fault test where available.

7. **Failure boundaries**
   - cases where the technique is invalid;
   - cases requiring a different routed skill;
   - approximations or heuristics that require explicit declaration and justification.

## Research-completion condition

When a required item is absent for the requested implementation, complete that item from the primary specification, paper, or current tool documentation before coding.

Instead:
1. load the skill implementation reference/examples;
2. verify current external API documentation if the gap is tool-version-dependent;
3. research the primary paper/specification if the gap is algorithmic;
4. add the missing implementation reference before producing production code.

The router may remain concise. Detailed implementation material belongs in references/ and references/examples/.

## Evidence-linked strategy acceptance

Each named optimization **strategy**, including a sub-technique within a larger workflow, must point to:

1. A precise and source-backed algorithm or documented library implementation with a direct publication, API or maintained code link.
2. A concrete code example with declared dependencies, inputs, register/bit semantics, outputs, and a reproducible execution path.
3. An explicit correctness check (state map, ancilla cleanup, unitary/equivalence, CSS commutation, decoded logical result, or resource/schedule invariant).
4. A measured before/after cost or target-dependent metric whenever an optimization improvement is claimed.
5. A documented validity scope including code family, noise model, target operation, qudit gate access, or hardware timing as applicable.

Read the compact [evidence manifest](../../../EVIDENCE_INDEX.md) to locate the relevant example and verified upstream source. The source and code are separate evidence: published hardware results establish demonstrated device behavior; simulator results establish the tested mathematical/software path; a successful syntax check establishes only parsability. Record the actual executed test and environment before elevating a strategy to validated status.

Keep speculative research and historical alternatives out of the normal agent routing context. Store useful research citations in their dedicated research references; route production transformations only through the evidence-linked implementations. Maintain correctness boundary conditions without repetitive negative-status prose.
