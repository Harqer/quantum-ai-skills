# Permutation-aware lowering: arithmetic example

Use when an exact register permutation feeds later logic or arithmetic.

## Semantic contract

For a width-`w` little-endian register:

~~~text
rot[i] = x[(i + r) mod w]
value(rot) = sum_i 2^i * rot[i]
z = (value(rot) + value(y)) mod 2^w
~~~

The wire holding `rot[i]` does not determine its numeric weight; logical position `i` does.

A lowering can therefore represent the rotation only as:

~~~text
logical position -> current wire
~~~

and connect the later primitive to the mapped wires. No SWAP is required solely to express the permutation.

## Exhaustive check

~~~python
def rotr(x, r, w):
    mask = (1 << w) - 1
    return ((x >> r) | ((x << (w - r)) & mask)) & mask

def value_from_view(x, r, w):
    return sum(((x >> ((i + r) % w)) & 1) << i for i in range(w))

for w in range(2, 7):
    for r in range(w):
        for x in range(1 << w):
            assert value_from_view(x, r, w) == rotr(x, r, w)
            for y in range(1 << w):
                explicit = (rotr(x, r, w) + y) % (1 << w)
                virtual = (value_from_view(x, r, w) + y) % (1 << w)
                assert virtual == explicit
~~~

This verifies that virtual lowering preserves arithmetic **when the adder consumes bits in logical significance order**.

## Boundary rules

- If the next primitive accepts mapped operands, keep the permutation virtual.
- If it assumes canonical ordering, materialize or adapt the primitive first.
- Before layout, preserve permutation freedom when useful.
- After layout, treat connectivity-induced routing separately.
- At IR/framework export, preserve the mapping, materialize it, or fail.

### Qiskit

`ElidePermutations` removes pre-layout permutation operations while tracking the induced virtual permutation. It intentionally does not apply the same transformation after physical layout.

Source: https://qiskit.qotlabs.org/docs/api/qiskit/qiskit.transpiler.passes.ElidePermutations

### pytket

Inspect:

~~~python
perm = circuit.implicit_qubit_permutation()
~~~

Before an OpenQASM export that cannot carry that mapping:

~~~python
exportable = circuit.copy()
exportable.replace_implicit_wire_swaps()
~~~

Sources:
- https://docs.quantinuum.com/tket/user-guide/manual/manual_circuit.html
- https://docs.quantinuum.com/tket/api-docs/qasm.html

## Acceptance

The candidate must preserve:
- the declared logical register value;
- arithmetic significance and carry/borrow ordering;
- final measurement/output interpretation;
- permutation metadata across every boundary where it remains virtual.
