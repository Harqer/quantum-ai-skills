# Example: Quantinuum native parameterized entanglers

## Helios Guppy RZZ

```python
from guppylang import guppy
from guppylang.std.angles import angle
from guppylang.std.quantum import qubit
from guppylang.std.qsystem.helios import zz_phase, measure

@guppy
def program() -> None:
    q0 = qubit()
    q1 = qubit()
    zz_phase(q0, q1, angle(-0.125))
    measure(q0)
    measure(q1)

hugr = program.compile()
```

Revalidate imports against the installed Guppy version.

## H2 target gate

```python
import qnexus
cfg = qnexus.QuantinuumConfig(
    device_name="H2-Emulator",
    target_2qb_gate="TK2",
)
```

Use `"ZZPhase"` for parameterized RZZ. Do not request TK2 on Helios unless current Helios documentation explicitly exposes it.
