# Permutation-aware lowering: exact arithmetic example

Use this example when an exact register permutation feeds later logic or arithmetic.

## Goal

Implement a width-`w` rotate-right as a logical view, consume that view in modular addition, and prove that no arithmetic meaning was lost.

For little-endian logical positions:

~~~text
rot[i] = x[(i + r) mod w]
value(rot) = sum_i 2^i * rot[i]
z = (value(rot) + value(y)) mod 2^w
~~~

The current physical or compiler wire holding `rot[i]` is irrelevant to its numeric weight. Weight comes from logical position `i`.

## Framework-neutral representation

~~~python
class RegisterView:
    def __init__(self, wires):
        self.wires = tuple(wires)  # indexed by logical position

    def permute(self, p):
        return RegisterView([self.wires[p[i]] for i in range(len(p))])

    def wire_at(self, logical_position):
        return self.wires[logical_position]


def rotr_view(view, r):
    w = len(view.wires)
    return view.permute([(i + r) % w for i in range(w)])


def lower_adder_operand(view):
    # Return wires in logical significance order.
    # A concrete adder may use these non-contiguously.
    return [view.wire_at(i) for i in range(len(view.wires))]
~~~

No SWAP operation appears in `rotr_view`; lowering updates only the logical-position-to-wire map.

## Exhaustive arithmetic check

~~~python
def rotr_int(x, r, w):
    mask = (1 << w) - 1
    return ((x >> r) | ((x << (w - r)) & mask)) & mask


def bit(x, i):
    return (x >> i) & 1


def value_from_rotr_view(x, r, w):
    # Logical position i reads source position (i + r) mod w.
    return sum(bit(x, (i + r) % w) << i for i in range(w))


for w in range(2, 7):
    for r in range(w):
        for x in range(1 << w):
            assert value_from_rotr_view(x, r, w) == rotr_int(x, r, w)

            for y in range(1 << w):
                explicit = (rotr_int(x, r, w) + y) % (1 << w)
                virtual = (value_from_rotr_view(x, r, w) + y) % (1 << w)
                assert virtual == explicit
~~~

This proves the virtual permutation itself does not change arithmetic. A quantum adder must still connect its logical bit-`i` machinery to `view.wire_at(i)`.

## Materialization test

If a downstream primitive assumes canonical wire order, materialize the current permutation before that boundary. Verify the materialized circuit and virtual-view circuit implement the same register map.

## Framework boundary checks

### Qiskit

Qiskit's `ElidePermutations` is a pre-layout optimization that removes permutation operations while tracking the induced virtual permutation. It becomes a no-op after layout because the same transformation is not generally sound once physical connectivity is fixed.

Source:
https://qiskit.qotlabs.org/docs/api/qiskit/qiskit.transpiler.passes.ElidePermutations

### pytket

Inspect an implicit permutation with:

~~~python
perm = circuit.implicit_qubit_permutation()
~~~

Before ordinary OpenQASM export, materialize it unless the workflow preserves the mapping separately:

~~~python
exportable = circuit.copy()
exportable.replace_implicit_wire_swaps()
~~~

pytket documents that its QASM converters do not account for implicit qubit permutations.

Sources:
- https://docs.quantinuum.com/tket/user-guide/manual/manual_circuit.html
- https://docs.quantinuum.com/tket/api-docs/qasm.html

## Acceptance invariants

A permutation-aware lowering is acceptable only when:

~~~text
logical value before lowering
    == logical value after lowering

all consumers resolve logical positions through the current map

arithmetic significance and carry/borrow order are unchanged

measurement/output interpretation applies the final permutation

any compiler boundary preserves, materializes, or rejects the mapping
~~~

After physical placement, separately optimize real routing cost; do not reinterpret connectivity-induced state movement as a free semantic permutation.
