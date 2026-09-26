---
name: fire-opal-adjunct
description: Run supported real quantum hardware through Q-CTRL Fire Opal for automated compilation, hardware-aware mapping, deterministic error suppression, measurement mitigation, iterative workloads, expectation estimation, QAOA, dynamics, and Monte Carlo workflows.
---

# Fire Opal

Use Fire Opal at the real-hardware execution boundary.

It accepts OpenQASM circuits or high-level solver inputs, maps them to a supported backend, suppresses hardware noise, applies measurement mitigation, submits the hardware work, and returns Fire Opal-processed results.

Choose:
- `execute`: one job, up to 300 circuits/parameter sets.
- `iterate`: consecutive/batch/variational jobs with queue/session reuse.
- `estimate_expectation`: observables instead of bitstrings.
- `iterate_expectation`: iterative observable workloads.
- `solve_qaoa`: managed QAOA optimization.
- `simulate_dynamics`: managed many-body dynamics.
- `integrate_monte_carlo`: managed Monte Carlo integration.

Authenticate Q-CTRL separately from the hardware provider. Discover backends with `show_supported_devices`. Validate circuits before paid execution. Use virtual qubits and let Fire Opal choose layout.

Preserve `job.action_id`; retrieve processed results through Fire Opal, not directly from the provider. Close iterative sessions with `stop_iterate`.

Load `references/implementation.md` for exact APIs and `references/tools.md` for current limits/provider support.
