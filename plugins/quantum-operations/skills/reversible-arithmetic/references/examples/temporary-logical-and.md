# Exact-cost pattern: temporary logical AND

Primary reference: Craig Gidney, Halving the cost of quantum addition, arXiv:1709.06648.

## Contract

Forward temporary AND:

~~~text
|a>|b>|0> -> phase-adjusted state with ancilla carrying (a AND b)
~~~

The construction uses **4 T gates**.

The specialized erase/uncompute uses **0 T gates** by measuring the temporary and applying a classically controlled Clifford correction.

This is not the ordinary unitary adjoint of the 4-T forward circuit.

## Implementation rule

Use a library implementation whose forward and adjoint semantics explicitly implement Gidney measurement-assisted pair, or reproduce the paper circuit exactly.

In Qualtran, And has a specialized adjoint with reduced cost:

~~~python
from qualtran.bloqs.mcmt import And

forward = And()
erase = And().adjoint()

_, forward_costs = forward.call_graph()
_, erase_costs = erase.call_graph()
~~~

Qualtran documentation explicitly calls out And().adjoint() as an optimized uncompute construction.

## Safe use pattern

~~~text
tmp = AND(a,b)      # 4 T
consume tmp
erase tmp           # measurement-assisted, 0 T
~~~

Preconditions:
- the temporary is only being erased, not needed coherently afterward;
- measurement and feed-forward are legal in the selected logical/QEC ISA;
- byproduct Clifford correction is tracked/applied correctly;
- the enclosing algorithm permits that measurement-assisted gadget.

Do **not** replace arbitrary coherent U ... U^dagger pairs with measurement.

## Arithmetic implication

When a carry/borrow bit is computed as an AND-like temporary and later erased, use the specialized erase cost rather than charging the same non-Clifford cost twice.

This is the mechanism behind the 4n + O(1) T-count adder result in Gidney paper.

## Verification

For each temporary-AND use:
1. verify the forward Boolean relation on basis states;
2. simulate both measurement branches of erase;
3. apply/track the required branch correction;
4. verify that the remaining data state matches coherent uncomputation;
5. ensure the measured ancilla is no longer entangled before reset/reuse;
6. include the measurement/feed-forward latency in the runtime schedule.
