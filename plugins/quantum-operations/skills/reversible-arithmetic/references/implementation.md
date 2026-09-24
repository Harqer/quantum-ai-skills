# Reversible arithmetic: implementation reference

## Required interface

Every arithmetic primitive must declare:

~~~text
input registers and endianness
semantic map
modulus/overflow behavior
ancilla contracts
allowed measurements
gate-set / FT interface
forward resource counts
inverse / cleanup resource counts
~~~

Do not call a primitive simply "adder" without stating whether it is full-width, modulo 2^n, modular by an arbitrary N, in-place, out-of-place, controlled, or produces carry-out.

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
~~~

## Multi-operand carry-save rule

For three n-bit operands x,y,z, a carry-save stage computes bitwise sum/carry words s,c satisfying:

~~~text
x + y + z = s + 2*c
~~~

with no long carry propagation inside the compressor stage.

Do not immediately convert every intermediate back to ordinary binary. Chain compressors until a semantic boundary requires one binary result, then perform the final carry-propagate addition.

Verification:
- exhaustive small-width arithmetic identity;
- all temporary carry/compressor bits cleaned according to contract.

## Constant specialization

For addition by known constant K:
- eliminate controls for zero constant bits;
- propagate fixed carries where provable;
- use the actual carry recurrence instead of instantiating a full quantum register containing K unless the chosen library requires it.

Never treat a message block, key, or input value as constant unless it is truly fixed for the target workload.

## Concrete examples

- refs/examples/cuccaro-adder.md: exact MAJ/UMA ripple construction.
- refs/examples/temporary-logical-and.md: 4-T temporary AND and measurement-assisted erase.

## Whole-workload rule

Do not select an adder by isolated gate count. A lower-depth adder with many ancillas can increase physical footprint; a one-ancilla ripple adder can increase runtime and accumulated logical failure.

Push candidate costs into ftqc-resource-estimation and ftqc-runtime-scheduling before selecting the production implementation.
