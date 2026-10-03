# Quantum Operations Plugin

Quantum Operations is a hardware-agnostic skill collection for designing, optimizing, validating, and costing fault-tolerant and present-day quantum computations.

The plugin is intentionally a knowledge layer rather than a runtime integration. It gives the host model reusable engineering workflows while leaving hardware selection, provider access, and execution to the surrounding environment.

## Technical scope

The router covers:
1. **Logical and algorithmic reduction** — semantic simplification, algorithmic gate compression, reversible arithmetic, Boolean fusion, ancilla lifetime, and MCMR qubit reuse.
2. **Non-Clifford and native-gate synthesis** — Clifford+T optimization, tensor/signature T-count optimization, parameterized native entanglers, ZX reasoning, and compiler passes.
3. **Quantum error correction** — code strategy, qLDPC/toric/qudit architectures, syndrome simulation, decoding, and logical error analysis.
4. **Logical FT compilation** — transversal/teleportation methods, lattice surgery, and magic-state systems.
5. **Runtime control and real-time decoding** — logical frames, measurement/feed-forward dependencies, decoder deadlines, reset/reuse, and backlog.
6. **Whole-machine scheduling and costing** — gates, transport, factories, QEC cycles, decoder/controller resources, wall-clock runtime, and physical resources.
7. **Verification and interoperability** — exact/approximate equivalence, resource regressions, OpenQASM/QIR interchange, and provider-adjacent execution layers.

Start with `skills/quantum-operations/SKILL.md`. It is the plugin's single cataloged skill and routes each request to the smallest required specialist workflow documents.

## Context architecture

The plugin exposes one concise router `SKILL.md`. Specialist workflows, implementation references, research, tool notes, and worked examples live under `skills/quantum-operations/references/workflows/` and are loaded only when selected.

## Hardware neutrality

Hardware is represented through explicit capabilities: native operations, angle ranges, connectivity, measurement/reset semantics, dynamic allocation, timing, calibration/error behavior, QEC support, and execution APIs. Provider-specific examples are evidence-backed adapters, not global assumptions.

## Implementation quality

Every production technique must provide explicit inputs/outputs, legality conditions, exact transformation or API steps, a worked example, independent verification, and unsupported/failure cases. Version-sensitive APIs are revalidated before use.

See [IMPLEMENTATION_QUALITY.md](IMPLEMENTATION_QUALITY.md).

## Security design

Static knowledge only. No MCP server, hooks, executable scripts, credentials, provider bindings, or write-capable runtime integration are bundled in this release.
