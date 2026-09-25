# Exact example: Cuccaro ripple-carry adder

Primary reference: Cuccaro, Draper, Kutin, Moulton, A new quantum ripple-carry addition circuit, quant-ph/0410184.

The OpenQASM project publishes a complete Cuccaro-derived adder example using the following exact primitives.

## MAJ and UMA gates

~~~qasm
gate majority a, b, c {
    cx c, b;
    cx c, a;
    ccx a, b, c;
}

gate unmaj a, b, c {
    ccx a, b, c;
    cx c, a;
    cx a, b;
}
~~~

Source:
https://github.com/openqasm/openqasm/blob/main/examples/adder.qasm

## Register semantics

For equal-width little-endian registers a[0..n-1], b[0..n-1]:

~~~text
input:
  cin
  a
  b
  cout=0

output:
  cin restored
  a restored
  b <- a + b + cin (low n bits)
  cout <- final carry
~~~

## Full-adder schedule

~~~qasm
majority cin[0], b[0], a[0];

for uint i in [0 : n-2] {
    majority a[i], b[i+1], a[i+1];
}

cx a[n-1], cout[0];

for uint i in [n-2 : -1 : 0] {
    unmaj a[i], b[i+1], a[i+1];
}

unmaj cin[0], b[0], a[0];
~~~

For a modulo-2^n adder, omit materialization/use of cout only if the chosen construction reverse sweep still restores all scratch and the intended semantic map is exactly modulo 2^n.

## Qiskit implementation checkpoint

Current Qiskit exposes:

~~~python
from qiskit.circuit.library import CDKMRippleCarryAdder

adder = CDKMRippleCarryAdder(
    num_state_qubits=n,
    kind="full",   # "half" or "fixed" also supported
)
~~~

Use this as an independent implementation reference, not as proof that a custom rewrite is correct.

## Known resource shape

The ripple construction is linear-depth and uses 2n + O(1) CCX gates and 5n + O(1) CX gates depending on the variant. Qiskit current synthesis documentation reports this asymptotic form.

## Verification

For n <= 5, exhaustively check every computational-basis input:

~~~text
(cin, a, b, cout=0)
   ->
(cin, a, (a+b+cin) mod 2^n, floor((a+b+cin)/2^n))
~~~

Also assert:
- a unchanged;
- cin restored;
- any helper restored;
- inverse circuit returns the entire state to the input.

For superposition correctness, exact circuit equivalence/statevector tests must supplement basis truth tables if a modified implementation uses phase-relaxed gates.
