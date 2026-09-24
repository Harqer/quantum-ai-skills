# Boolean fusion: implementation reference

Use Algebraic Normal Form (ANF) as the default exact representation for XOR/AND-heavy Boolean regions.

## Representation

For Boolean inputs x_0 ... x_{n-1}, ANF is:

~~~text
f(x) = XOR over monomials S of a_S * PRODUCT(x_i for i in S)
~~~

Coefficients a_S are in GF(2). Represent a monomial by an input-bit mask.

## Truth table -> ANF (Möbius transform)

Given values[mask] = f(mask) for all 2^n inputs:

~~~python
coeff = values.copy()
for bit in range(n):
    for mask in range(1 << n):
        if mask & (1 << bit):
            coeff[mask] ^= coeff[mask ^ (1 << bit)]
~~~

Afterwards coeff[mask] == 1 means that monomial appears in ANF.

Apply independently to each output bit.

Verification: reconstruct the truth table from the ANF and compare all 2^n assignments for small functions.

## Direct reversible synthesis of one output

For a target initialized to t, implement:

~~~text
t <- t XOR f(x)
~~~

without modifying source bits.

- constant term 1: X(t)
- degree-1 monomial x_i: CX(x_i,t)
- degree-2 monomial x_i x_j: CCX(x_i,x_j,t) or an FT-lowered equivalent
- higher degree: route to the multi-control strategy chosen by clifford-t-optimization / ancilla policy

This gives exact Boolean semantics but is not necessarily FT-cost optimal.

## SHA-256 Boolean identities

For bit variables x,y,z:

~~~text
Ch(x,y,z) = (x AND y) XOR ((NOT x) AND z)
          = z XOR xy XOR xz

Maj(x,y,z) = xy XOR xz XOR yz
~~~

These ANFs show that both functions contain the nonlinear product xz.

### Shared-product candidate

If two live outputs need both Ch and Maj from the same version of x,y,z:

~~~text
tmp <- x AND z
ch  ^= z
ch  ^= x AND y
ch  ^= tmp
maj ^= x AND y
maj ^= tmp
maj ^= y AND z
uncompute tmp
~~~

Do not automatically share every repeated product. Compare:

~~~text
saved nonlinear recomputations
vs.
temporary allocation + lifetime + cleanup + routing/fanout
~~~

In an FT schedule, sharing can reduce total T/CCZ demand but increase logical width and lengthen the temporary live interval.

## Product DAG

Build one DAG node per unique monomial over the same input versions.

Each node stores:

~~~text
support_mask
producer
consumers[]
compute_cost
uncompute_cost
live_interval
~~~

A monomial may be materialized once and shared only if its lifetime/cost passes the ancilla optimization rule.

## Mutually exclusive controls

If a proof establishes a AND b = 0 for all reachable states, eliminate monomials containing ab.

This requires a semantic invariant; do not infer exclusivity from naming or observed test cases.

## Reversible boundary

ANF simplification proves only the classical Boolean map. If the synthesized implementation uses relative-phase gates, verify the full quantum transformation separately.

## Tests

For every fused Boolean region:
1. exhaustive truth-table equality for manageable input count;
2. source registers unchanged;
3. all clean temporaries returned to |0>;
4. dirty temporaries restored exactly;
5. independent quantum equivalence if relative-phase/non-classical synthesis is used;
6. resource regression for nonlinear count, logical width, and uncompute cost.
