# Ancilla lifetime: implementation reference

## Ancilla contracts

Every temporary must have one explicit contract.

### Clean ancilla

Precondition:

~~~text
state = |0>
not entangled with live data
~~~

Postcondition before release:

~~~text
state = |0>
not entangled with live data
~~~

### Dirty / borrowed ancilla

Precondition: arbitrary unknown state |psi>, possibly entangled with an external system.

Postcondition: **the exact same state** |psi> and the same external correlations must be restored.

Never assume a dirty ancilla is a classical unknown bit.

### Measured temporary

May be measured only when a proven protocol allows its quantum information to leave the coherent state.

After measurement, the pre-measurement quantum state is destroyed. The qubit cannot be treated as coherently borrowed.

### Resettable temporary

Reset is permitted only after measurement/discard is semantically legal.

Reset establishes |0> but is non-unitary and therefore cannot replace coherent uncomputation in an oracle merely to save width.

## SSA liveness analysis

Use versioned values.

For each produced temporary v:

~~~text
birth(v)    = instruction index that creates v
last_use(v) = maximum instruction index of any consumer
~~~

For a coherent temporary requiring inverse cleanup, extend its interval through the uncompute operation.

Two clean temporaries may share one physical/logical ancilla slot only when their required live intervals do not overlap and both cleanup contracts hold.

## Linear-scan allocator

~~~python
active = []
free_pool = []

for temp in temps_by_birth:
    expire every item in active with last_use < temp.birth
    return expired compatible slots to free_pool

    slot = first compatible slot in free_pool
    if slot is None:
        slot = allocate_new_slot(temp.contract)

    assign(temp, slot)
    active.add(temp)
~~~

Compatibility is contract-sensitive: do not reuse a dirty slot as a clean |0> slot unless a protocol has restored it to clean zero.

## Compute -> consume -> uncompute

Default pattern:

~~~text
U_compute
    use temporary result
U_compute^dagger
release ancilla
~~~

Move U_compute^dagger immediately after the last consumer whenever dependencies permit.

Verification invariant for a clean temporary:

~~~text
released ancilla = |0>
and is unentangled from the remaining data
~~~

## Reversible pebbling model

For a dependency DAG:
- permanent input nodes start pebbled;
- placing a pebble on node v is legal only if all predecessors are pebbled;
- removing a computed pebble is legal only if the predecessors needed to reverse its computation are available;
- a pebble corresponds to stored reversible intermediate state.

Track:

~~~text
peak_pebbles       -> logical width proxy
forward_evaluations
reverse_evaluations
critical_path
~~~

### Exact small-DAG search

For a small DAG, represent the pebble configuration as a bitset and run BFS/Dijkstra over legal place/remove moves.

State:

~~~text
(config_bitset, outputs_reached)
~~~

Cost may be lexicographic:

~~~text
(peak_pebbles, total_moves)
~~~

or weighted by the FT resource model.

For large DAGs use heuristics, but label them as heuristics and preserve a baseline schedule.

## Storage versus recomputation

For a candidate temporary v, compare:

~~~text
store:
  + 1 logical-qubit lifetime from birth to last use
  + routing/idling/QEC exposure

recompute:
  + repeated forward cost
  + repeated cleanup cost
  + added schedule depth/factory demand
~~~

Do not choose based on qubit count alone.

## Tests

- clean ancilla returns to |0>;
- dirty ancilla round-trips arbitrary basis states and random statevectors on small cases;
- full data output unchanged by allocation strategy;
- no use-after-release;
- peak live-slot count equals allocator report;
- recomputation schedule remains exactly equivalent.
