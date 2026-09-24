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

## Stop condition

If a required item is absent for the requested implementation, do **not** fill it from intuition.

Instead:
1. load the skill implementation reference/examples;
2. verify current external API documentation if the gap is tool-version-dependent;
3. research the primary paper/specification if the gap is algorithmic;
4. add the missing implementation reference before producing production code.

The router may remain concise. Detailed implementation material belongs in references/ and references/examples/.
