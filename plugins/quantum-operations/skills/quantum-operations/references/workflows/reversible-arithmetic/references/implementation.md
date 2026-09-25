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

Name each arithmetic primitive together with its exact contract: full-width or modulo, modulus when applicable, in-place or out-of-place mapping, control behavior, and carry outputs.

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

Keep intermediate multi-operand values in carry-save/compressor form across compatible stages, then perform the final carry-propagate addition at the semantic boundary that requires one binary result.

Verification:
- exhaustive small-width arithmetic identity;
- all temporary carry/compressor bits cleaned according to contract.

## Constant specialization

For addition by known constant K:
- eliminate controls for zero constant bits;
- propagate fixed carries where provable;
- use the actual carry recurrence instead of instantiating a full quantum register containing K unless the chosen library requires it.

Specialize a message block, key, or input value as a constant only when the target workload explicitly fixes that value.

## Concrete examples

- [examples/cuccaro-adder.md](examples/cuccaro-adder.md): exact MAJ/UMA ripple construction.
- [examples/temporary-logical-and.md](examples/temporary-logical-and.md): 4-T temporary AND and measurement-assisted erase.

## Whole-workload rule

Select the adder from the joint logical-width, depth, ancilla, factory, runtime, and logical-failure cost; preserve multiple Pareto candidates when these objectives trade off.

Push candidate costs into ftqc-resource-estimation and ftqc-runtime-scheduling before selecting the production implementation.
