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

## 1. Virtual word permutations / rotations

For an n-bit register x, represent a logical rotate-right by r as a view:

~~~text
view_x_r[i] = x[(i + r) mod n]
~~~

No SWAP gates are emitted.

Example for 8 bits, ROTR2:

~~~text
logical index: 0 1 2 3 4 5 6 7
physical wire: 2 3 4 5 6 7 0 1
~~~

Materialize the permutation only when the next operation requires a concrete physical ordering that cannot consume the view.

### Legality

Virtual relabeling is valid only when:
- the operation is exactly a permutation of wire identities;
- no measurement/classical output depends on the old naming convention before the view is resolved;
- two aliases are not accidentally treated as independent qubits.

Verification: compare the logical bit permutation against the mathematical word operation for every index.

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

Do not propagate a basis-state constant through a Hadamard, arbitrary rotation, entangling operation with unknown control, measurement-dependent branch, or any operation that invalidates the proof.

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

Do not infer commutation of arbitrary overlapping gates from names or matrices without proof.

## 6. Cross-boundary fusion

Keep named semantic blocks until a lowering boundary is necessary.

Example: SHA-style word expression

~~~text
t = ROTR(x,2) XOR ROTR(x,13) XOR ROTR(x,22)
~~~

should remain a word-level XOR of virtual views. Lowering each rotate to SWAPs before combining destroys the zero-gate rotate representation.

## Verification

For each rewrite:
1. test the semantic IR before/after on exhaustive small bit widths when classical/reversible;
2. for quantum phase-sensitive regions use an exact circuit equivalence checker;
3. assert the same live outputs and required ancilla final states;
4. compare downstream FTQC metrics, not only primitive gate count.

## Failure cases

Do not apply:
- classical constant propagation to unknown superposition states;
- virtual permutations across fixed hardware placement boundaries unless remapping metadata is updated;
- CSE across state-changing measurement/reset;
- phase-insensitive Boolean equivalence inside a region where relative phase matters.
