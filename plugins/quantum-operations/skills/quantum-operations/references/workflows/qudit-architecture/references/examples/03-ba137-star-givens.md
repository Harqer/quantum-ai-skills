# Example 3: 137Ba+ star-topology qudit compiler

The 25-level 137Ba+ experiment couples one S_1/2 state |0> to D_5/2 states |i> with 1762 nm electric-quadrupole transitions.

Allowed elementary rotations act only on span{|0>,|i>}:

~~~text
G_0i(theta) = exp[-theta (|0><i| - |i><0|)]
~~~

Compile target U in U(d) using the experimentally matched star topology:

~~~text
V = U
record = []

for i from d-1 down to 1:
    choose theta that eliminates V[i,0]
    V = G_0i(theta) V
    append G_0i(theta) to record

for k from d-1 down to 1:
    apply S_0k = G_0k(pi/2)
    for i > k:
        choose theta that eliminates V[i,k]
        V = G_0i(theta) V
        append G_0i(theta)
    apply S_0k again

assert V is identity within numerical tolerance

physical pulse sequence =
    reverse(record) with adjoints
~~~

Generic pulse count:

~~~text
N = (d-1)(d+4)/2
~~~

At d=16, sufficient to encode four virtual qubits, the generic decomposition can require 150 Givens rotations for an arbitrary local U. This is why the carrier-count reduction cannot be evaluated without pulse depth.
