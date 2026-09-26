---
name: fire-opal-adjunct
description: Optimize execution on supported QPUs with Q-CTRL Fire Opal: hardware-aware compilation, optimal physical-qubit layout/routing, gate resynthesis, scheduling, error suppression, measurement mitigation, and managed execution workflows.
---

# Fire Opal

Use Fire Opal as the hardware-execution optimizer. Submit virtual-qubit circuits; Fire Opal selects the physical-qubit layout, routes against device connectivity and calibration/error data, optimizes/resynthesizes gates and scheduling, then applies error suppression and measurement mitigation before execution.

Choose:
- `execute`: one job, up to 300 circuits/parameter sets.
- `iterate`: consecutive/batch/variational jobs with queue/session reuse.
- `estimate_expectation`: observables instead of bitstrings.
- `iterate_expectation`: iterative observable workloads.
- `solve_qaoa`: managed QAOA optimization.
- `simulate_dynamics`: managed many-body dynamics.
- `integrate_monte_carlo`: managed Monte Carlo integration.

Authenticate Q-CTRL separately from the hardware provider. Discover backends with `show_supported_devices`. Validate before paid execution. Keep circuits on virtual qubits: Fire Opal's transpiler chooses the physical layout; supplying physical qubits bypasses the optimization model and is rejected.

Preserve `job.action_id`; retrieve processed results through Fire Opal, not directly from the provider. Close iterative sessions with `stop_iterate`.

Load `references/implementation.md` for exact APIs and `references/tools.md` for current limits/provider support.
