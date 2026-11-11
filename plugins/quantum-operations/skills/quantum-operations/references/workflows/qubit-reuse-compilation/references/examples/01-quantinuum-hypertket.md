# Example: Quantinuum HyperTKET qubit reuse

```python
import qnexus
from quantinuum_schemas.models.hypertket_config import (
    HyperTketConfig, QubitReuseConfig, DefaultOrderConfig, DualStrat,
)

backend = qnexus.QuantinuumConfig(device_name="H2-Emulator")
hypertket = HyperTketConfig(
    qubit_reuse_config=QubitReuseConfig(
        enable_qubit_reuse=True,
        ordering_config=DefaultOrderConfig(),
        dual_circuit_strategy=DualStrat.AUTO,
    )
)

circuit_ref = qnexus.circuits.upload(circuit, name="reuse-input")
job = qnexus.start_compile_job(
    programs=[circuit_ref],
    name="reuse-compile",
    hypertket_config=hypertket,
    backend_config=backend,
    optimisation_level=0,
)
qnexus.jobs.wait_for(job)
compiled = qnexus.jobs.results(job)[0].get_output().download_circuit()
print(circuit.n_qubits, "->", compiled.n_qubits)
```

For small instances needing exact minimum width, use current `ConstrainedOptOrderConfig` or `BruteForceOrderConfig` according to documented scale.
