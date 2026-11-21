# Executable example: dependency- and resource-aware FTQC schedule

**Definition.** Schedule logical operations, syndrome decoding and magic-state generation with explicit dependencies and resource contention. Decode must finish before conditioned gates begin; a magic-state consumer must wait for a produced state.

The example is pure Python 3.10+:

~~~python
tasks = [
    ("entangle", 3, (), "qpu"),
    ("measure", 1, ("entangle",), "qpu"),
    ("decode", 2, ("measure",), "decoder"),
    ("factory", 3, (), "factory"),
    ("consume_T", 1, ("decode", "factory"), "qpu"),
]
finish = {}
schedule = {}
available = {}
for name, cycles, dependencies, resource in tasks:
    assert all(dep in finish for dep in dependencies), ("missing dependency or cycle", name)
    start = max([finish[d] for d in dependencies] + [available.get(resource, 0)])
    finish[name] = available[resource] = start + cycles
    schedule[name] = (start, finish[name])
assert schedule["decode"][1] <= schedule["consume_T"][0]
assert schedule["factory"][1] <= schedule["consume_T"][0]
assert schedule["consume_T"] == (6, 7)
print("scheduled makespan:", max(finish.values()), "cycles")
~~~

**Source algorithm:** Resource-constrained project scheduling (precedence and mutually exclusive capacity constraints); the plugin's `ftqc-runtime-scheduling/references/implementation.md` defines the FTQC-specific decoder and factory semantics.

**Verification:** Every prerequisite finishes before its consumer starts; every single-capacity resource's intervals are disjoint; a schedule with a dependency cycle is rejected. Feed-forward and factory supply appear as explicit constraints rather than implicit estimates. Extend the resource model to measured controller latencies and factory acceptance probabilities before physical-runtime estimation.
