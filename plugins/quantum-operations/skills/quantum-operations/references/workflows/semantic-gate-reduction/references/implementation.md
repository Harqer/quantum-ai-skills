# Semantic gate reduction: implementation reference

This reference defines exact transformations for optimization **before** primitive gate decomposition.

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
wire_map          # logical position -> current wire
side_effects      # measurement/reset/classical output/etc.
phase_sensitive   # whether relative/global phase is observable
~~~

Use SSA-style value versions so an expression is reusable only when its operands are the same versions.

## 1. Permutation-aware lowering

For an n-bit register `x`, represent an exact permutation `P` as a view:

~~~text
view[i] = x[P(i)]
~~~

A rotate-right by `r` is:

~~~text
view[i] = x[(i + r) mod n]
~~~

Lowering may remove the high-level permutation operation while preserving its semantics as a wire map or bit-level dependency graph. No SWAP gate is required merely because the logical order changed.

Example for an 8-bit rotate-right by 2:

~~~text
logical position: 0 1 2 3 4 5 6 7
current wire:     2 3 4 5 6 7 0 1
~~~

### Why this is preferred

Prematurely synthesizing a semantic permutation into SWAPs can:
- add two-qubit work not required by the algorithm;
- hide algebraic structure from later optimization;
- constrain placement before hardware topology is known;
- force a router to optimize an artificial state-movement network.

Prefer:

~~~text
semantic permutation
-> tracked logical-wire map / dependency graph
-> semantic optimization
-> physical placement and routing
~~~

not:

~~~text
semantic permutation
-> SWAP network
-> try to remove the SWAPs later
~~~

### Arithmetic-significance invariant

A register's numeric meaning is defined by its **logical positions and declared endianness**, not by current wire IDs or physical-qubit indices.

For little-endian binary arithmetic:

~~~text
value(x) = sum_i 2^i * bit_at_logical_position(i)
~~~

For big-endian arithmetic, use the declared big-endian weight function instead.

If a permuted view is consumed by an adder, comparator, multiplier, or modular primitive, resolve each logical position through the current `wire_map`. Carry/borrow adjacency follows logical significance positions, not physical adjacency.

A permutation can therefore remain virtual across arithmetic **only when the arithmetic implementation consumes the mapped logical positions correctly**. Otherwise materialize the permutation before that primitive.

### Semantic permutation versus routing

Keep these separate:

1. **Semantic permutation:** changes logical identity/order. Track it in `wire_map`; it may require zero gates.
2. **Physical routing:** moves quantum state because selected physical qubits cannot perform a required interaction directly. Optimize this after layout using the target topology, native gate set, timing, and calibration/error model.

Before layout, permutation-elision is generally a virtual-mapping transformation. After layout, do not delete a routing SWAP unless the physical mapping is updated consistently and connectivity constraints remain satisfied.

### Materialization boundary

Materialize a permutation only when the next boundary cannot preserve or consume the mapping, for example:
- an arithmetic or logical primitive that assumes canonical contiguous ordering;
- a measurement/output interface with fixed bit positions;
- an IR/framework conversion that cannot carry the permutation;
- a physical-layout boundary that requires a concrete mapping.

When possible, absorb the permutation into placement or output interpretation instead of emitting a standalone SWAP network.

### Interchange rule

At every conversion boundary, one of these must happen:

~~~text
preserve permutation metadata
OR materialize equivalent gates
OR fail explicitly
~~~

Never silently drop an implicit permutation.

Current examples:
- Qiskit `ElidePermutations` tracks a pre-layout output permutation in `virtual_permutation_layout`.
- pytket can keep implicit wire swaps, but its OpenQASM converters do not account for them; materialize them or preserve the mapping separately before export.

### Verification

For each permutation rewrite:
1. compare the mathematical permutation with `wire_map`;
2. verify every consumer resolves logical positions through that map;
3. verify arithmetic register significance and carry/borrow ordering;
4. verify measurement and output-bit interpretation;
5. check permutation metadata survives every compiler boundary;
6. after placement, compare native two-qubit count/depth and final logical-to-physical mapping;
7. use exact circuit equivalence for phase-sensitive quantum rewrites.

Use `references/examples/permutation-aware-lowering.md` for a small exhaustive arithmetic example and framework-boundary checks.

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

For word XOR, apply bitwise through the current logical-wire maps rather than materializing register permutations first.

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

Share only when the selected FTQC objective improves.

## 5. Commutation/reordering

Always allow operations on disjoint qubit sets to commute.

For overlapping operations, require an explicit algebraic rule. Examples:

~~~text
Rz(a) Rz(b) on same qubit -> Rz(a+b)
XOR/CNOT networks may be rescheduled using linear GF(2) equivalence
diagonal Z/phase operations commute with each other
~~~

## 6. Cross-boundary fusion

Keep named semantic blocks until a lowering boundary is necessary.

Example:

~~~text
t = ROTR(x,a) XOR ROTR(x,b) XOR ROTR(x,c)
~~~

may lower directly into XOR dependencies over three indexed views. Lowering each permutation into a SWAP network first destroys that representation and can increase downstream routing cost.

## Verification

For each rewrite:
1. test semantic IR before/after exhaustively at small widths when classical/reversible;
2. use an exact circuit-equivalence checker for phase-sensitive regions;
3. assert the same logical outputs and required ancilla final states;
4. assert the same declared register values under the current endianness;
5. compare downstream FTQC and hardware-routing metrics, not only primitive gate count.

## Failure cases

- Virtual permutations are invalid if aliases are treated as independent qubits.
- Arithmetic is invalid if numeric significance is inferred from current wire/physical indices instead of logical register positions.
- A compiler boundary is invalid if required permutation metadata is dropped.
- Post-layout routing operations cannot be removed without a sound physical-mapping update.
- Phase-sensitive rewrites require the intended quantum equivalence relation, not only basis-state truth-table equality.

## Sources

- Qiskit `ElidePermutations`: https://qiskit.qotlabs.org/docs/api/qiskit/qiskit.transpiler.passes.ElidePermutations
- Qiskit `TranspileLayout`: https://qiskit.qotlabs.org/docs/api/qiskit/qiskit.transpiler.TranspileLayout
- pytket implicit qubit permutations: https://docs.quantinuum.com/tket/user-guide/manual/manual_circuit.html
- pytket OpenQASM conversion warning: https://docs.quantinuum.com/tket/api-docs/qasm.html
- permutation-aware synthesis/mapping: https://arxiv.org/abs/2305.02939
