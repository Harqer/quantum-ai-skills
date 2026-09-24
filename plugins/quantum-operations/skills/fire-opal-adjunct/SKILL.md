---
name: fire-opal-adjunct
description: Use Q-CTRL Fire Opal as an optional present-day hardware execution and error-suppression adjunct while keeping FTQC QEC, logical synthesis, and resource estimation as separate layers.
---

# Fire Opal Adjunct

Use Fire Opal for supported present-day real-hardware execution when error suppression or mitigation is part of the experiment. Keep Fire Opal validation and result-quality metrics in a present-day hardware layer, while logical fault tolerance, code distance, logical width, magic-state factories, and FTQC resource estimates continue to come from the dedicated FTQC skills. This separation keeps hardware-error-suppression evidence and fault-tolerant architectural evidence comparable without conflating their meanings.

Resolve the current supported providers and backends from Q-CTRL documentation at execution time, run the validation path before metered hardware submission, and preserve the backend, shots, validation output, Fire Opal version, provider metadata, and result metrics with the experiment. Pure FTQC resource-analysis tasks route directly through the QEC, scheduling, and resource-estimation skills, while present-day hardware experiments can add this adjunct at the execution boundary.

## Implementation gate

Load `references/implementation.md` before writing a Fire Opal integration. It defines environment-based authentication, supported-device discovery, validation-before-execution, execution/result handling, and the boundary between error suppression and FTQC claims. Apply `../quantum-operations/references/implementation-contract.md` and verify the current Fire Opal API and provider support immediately before use.
