# Reversible arithmetic: implementation reference

## Required interface

Every arithmetic primitive must declare:

~~~text
input registers and endianness
logical-position -> wire mapping when non-canonical
semantic map
modulus/overflow behavior
ancilla contracts
allowed measurements
gate-set / FT interface
forward resource counts
inverse / cleanup resource counts
~~~

Name each arithmetic primitive together with its exact contract: full-width or modulo, modulus when applicable, in-place or out-of-place mapping, control behavior, carry outputs, and cleanup behavior.

## Register-significance invariant

Arithmetic acts on **logical register positions**, not physical wire numbers.

For a declared n-bit register, define the numeric weight of each logical position from the register's endianness. A permuted/rotated/reindexed view may be consumed without physically restoring canonical wire order only if the primitive resolves every logical position through the current mapping.

For ripple-carry arithmetic, carry/borrow propagation follows adjacent **significance positions**. For prefix, lookahead, compressor, comparator, and modular arithmetic, generate/propagate and grouping rules use the same logical significance relation.

Do not infer arithmetic significance from:
- current wire ID;
- physical-qubit index;
- graph adjacency;
- placement order.

If an arithmetic implementation cannot accept a mapped register view, materialize the permutation or adapt the primitive before use.

Verification: for small widths, compare the mapped implementation exhaustively against the declared integer function under the same endianness and modulus.

## Candidate selection

For each arithmetic region, construct at least these candidates when applicable:

1. ripple carry;
2. prefix/lookahead;
3. carry-save/compressor network for multi-operand sums;
4. constant-specialized arithmetic;
5. measurement-assisted arithmetic when runtime control permits it.

Compare candidates on:

~~~text
logical width
Toffoli/CCZ count
T-state equivalent cost
non-Clifford depth
measurement/feed-forward depth
Clifford two-qubit count
ancilla lifetime
full compute + cleanup cost
routing/materialization cost for non-canonical register views
~~~

## Multi-operand carry-save rule

For three n-bit operands x,y,z, a carry-save stage computes bitwise sum/carry words s,c satisfying:

~~~text
x + y + z = s + 2*c
~~~

with no long carry propagation inside the compressor stage.

Keep intermediate multi-operand values in carry-save/compressor form across compatible stages, then perform the final carry-propagate addition at the semantic boundary that requires one binary result.

Verification:
- exhaustive small-width arithmetic identity;
- all temporary carry/compressor bits cleaned according to contract;
- any non-canonical input/output maps resolve to the declared integer values.

## Constant specialization

For addition by known constant K:
- eliminate controls for zero constant bits;
- propagate fixed carries where provable;
- use the actual carry recurrence instead of instantiating a full quantum register containing K unless the chosen library requires it.

Specialize an input value as a constant only when the target workload explicitly fixes that value.

## Concrete examples

- [examples/cuccaro-adder.md](examples/cuccaro-adder.md): exact MAJ/UMA ripple construction.
- [examples/temporary-logical-and.md](examples/temporary-logical-and.md): 4-T temporary AND and measurement-assisted erase.
- [../../semantic-gate-reduction/references/examples/permutation-aware-lowering.md](../../semantic-gate-reduction/references/examples/permutation-aware-lowering.md): preserving numeric significance across a virtual permutation.

## Whole-workload rule

Select the adder from the joint logical-width, depth, ancilla, factory, runtime, logical-failure, and routing/materialization cost. Preserve multiple Pareto candidates when these objectives trade off.

Push candidate costs into ftqc-resource-estimation and ftqc-runtime-scheduling before selecting the production implementation.
