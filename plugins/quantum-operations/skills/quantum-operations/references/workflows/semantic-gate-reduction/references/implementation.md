# Semantic gate reduction: implementation reference

This reference defines concrete transformations for optimization **before** primitive gate decomposition.

## Semantic IR

Represent each operation with at least:

~~~text
id
op_kind
inputs[]          # versioned values/register views
outputs[]
width
parameters
known_constants   # bit mask/value where proven
wire_map          # logical index -> underlying wire when virtual
side_effects      # measurement/reset/classical output/etc.
phase_sensitive   # whether relative/global phase is semantically observable
~~~

Use SSA-style value versions so an expression is reusable only when its operands are the same versions.

## 1. Permutation-aware lowering

Represent an exact register permutation `P` as a logical view:

~~~text
view[i] = x[P(i)]
~~~

For rotate-right by `r`:

~~~text
view[i] = x[(i + r) mod n]
~~~

Lowering may replace the high-level permutation with a `wire_map` or bit-level dependencies. Do **not** emit SWAPs solely because logical order changed.

### Required invariant

Track:

~~~text
logical position -> current wire -> physical qubit (after layout)
~~~

Logical identity and numeric significance belong to the **logical position**, not the wire or physical-qubit number. For arithmetic, carry/borrow and significance order follow the declared register ordering/endianness after resolving each logical position through `wire_map`.

A virtual permutation is therefore legal across Boolean or arithmetic consumers only when those consumers use the mapped logical positions correctly.

### Semantic permutation versus routing

- **Semantic permutation:** changes logical ordering; it can often be absorbed into mapping with zero intrinsic state movement.
- **Physical routing:** moves state because the selected hardware topology cannot realize a required interaction directly; optimize it after layout.

Before layout, keep useful permutation freedom when possible. After layout, do not delete a routing SWAP unless the physical mapping is updated consistently and connectivity remains valid.

### Materialization boundary

Preserve the mapping until a downstream boundary cannot represent or consume it. Then either:

~~~text
preserve permutation metadata
OR materialize an equivalent permutation
OR fail explicitly
~~~

Typical boundaries are a primitive that assumes canonical ordering, fixed measurement/output positions, IR/framework export, or physical placement.

Current compiler behavior supports this distinction: Qiskit `ElidePermutations` removes pre-layout permutations while tracking `virtual_permutation_layout`; pytket supports implicit wire swaps, while its OpenQASM converters do not account for them.

### Verification

1. Compare the mathematical permutation with `wire_map`.
2. Verify all consumers resolve logical positions through the map.
3. Verify arithmetic significance/carry order and output-bit interpretation.
4. Verify every compiler boundary preserves or materializes the mapping.
5. After placement, compare native routing/two-qubit cost separately.

Worked example: [examples/permutation-aware-lowering.md](examples/permutation-aware-lowering.md).

## 2. Constant propagation for reversible Boolean gates

Track only **proven computational-basis constants**.

For a control bit known to be 0:

~~~text
CX(control=0, target)  -> delete
CCX(... control=0 ...) -> delete
~~~

For a control bit known to be 1:

~~~text
CX(control=1, target)      -> X(target)
CCX(c1=1, c2, target)      -> CX(c2, target)
CCX(c1, c2=1, target)      -> CX(c1, target)
~~~

For a target known constant, update the known value only if the gate controls are themselves known. Otherwise the target ceases to be a proven classical constant.

End the basis-state constant proof at a Hadamard, arbitrary rotation, entangling operation with unknown control, measurement-dependent branch, or any other operation that changes the value's classical-state guarantee.

## 3. XOR normalization

Represent XOR expressions as sets/multisets modulo 2:

~~~text
a XOR a = 0
a XOR 0 = a
a XOR 1 = NOT a
~~~

Canonicalize operands by value ID and cancel duplicates pairwise.

Example:

~~~text
(a XOR b) XOR (b XOR c) -> a XOR c
~~~

For word XOR, apply bitwise.

## 4. Common-subexpression elimination

A candidate expression can be shared only when:
- the operation is pure/reversible over the same versioned operands;
- reuse does not cross a measurement/reset/control-flow boundary that changes semantics;
- the temporary lifetime and cleanup are defined.

Cost comparison:

~~~text
share_cost =
    compute_once
  + fanout/use_cost
  + storage_cost(lifetime)
  + uncompute_cost

recompute_cost =
    sum(compute_at_each_use)
~~~

Share only when the selected FTQC objective improves. A lower gate count alone is insufficient if peak logical width or factory burst demand worsens.

## 5. Commutation/reordering

Always allow operations on disjoint qubit sets to commute.

For overlapping operations, require an explicit algebraic rule. Examples:

~~~text
Rz(a) Rz(b) on same qubit -> Rz(a+b)
XOR/CNOT networks may be rescheduled using linear GF(2) equivalence
diagonal Z/phase operations commute with each other
~~~

For overlapping gates, apply only an explicit algebraic commutation rule whose preconditions are satisfied.

## 6. Cross-boundary fusion

Keep named semantic blocks until a lowering boundary is necessary, but do not turn a semantic block boundary into measurement, checkpoint/reload, forced wire canonicalization, or a separate execution unless the algorithm or selected FT protocol requires it.

For a generic word expression:

~~~text
t = ROTR(x,a) XOR ROTR(x,b) XOR ROTR(x,c)
~~~

lower directly into dependencies over mapped views when legal. Lowering each permutation to SWAPs first can hide simplifications and create avoidable routing work.

## Verification

For each rewrite:
1. test the semantic IR before/after on exhaustive small bit widths when classical/reversible;
2. for quantum phase-sensitive regions use an exact circuit equivalence checker;
3. assert the same live outputs and required ancilla final states;
4. compare downstream FTQC metrics, not only primitive gate count.

## Failure cases

Apply each rewrite within these validity boundaries:
- classical constant propagation applies to values with a proven computational-basis constant;
- virtual permutations crossing arithmetic, interchange, measurement/output, or hardware-placement boundaries preserve or materialize the corresponding mapping;
- CSE uses the same versioned operands within a region whose state has not been changed by measurement or reset;
- phase-sensitive regions use an equivalence relation that preserves the required relative phase.

## Sources

- Qiskit `ElidePermutations`: https://qiskit.qotlabs.org/docs/api/qiskit/qiskit.transpiler.passes.ElidePermutations
- Qiskit `TranspileLayout`: https://qiskit.qotlabs.org/docs/api/qiskit/qiskit.transpiler.TranspileLayout
- pytket implicit qubit permutations: https://docs.quantinuum.com/tket/user-guide/manual/manual_circuit.html
- pytket OpenQASM conversion warning: https://docs.quantinuum.com/tket/api-docs/qasm.html
- permutation-aware synthesis/mapping: https://arxiv.org/abs/2305.02939
