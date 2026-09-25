# Quantum Operations Plugin

Quantum Operations is a hardware-agnostic skill collection for designing, optimizing, validating, and costing **fault-tolerant quantum computations**.

The plugin is intentionally a knowledge layer rather than a runtime integration. It gives the host model reusable engineering workflows while leaving hardware selection, provider access, and execution to the surrounding environment.

## Technical scope

The router coordinates seven broad domains:

1. **Logical reduction** — semantic simplification, reversible arithmetic, Boolean fusion, and ancilla lifetime.
2. **Fault-tolerant synthesis** — Clifford+T / non-Clifford optimization plus supporting circuit-rewrite and compiler passes.
3. **Quantum error correction** — code strategy, syndrome simulation, detector models, decoder accuracy, and logical error analysis.
4. **Logical FT compilation** — topological/lattice-surgery operations and magic-state production where applicable.
5. **Runtime control and real-time decoding** — logical frames, measurement/feed-forward dependencies, decoder deadlines, tail latency, buffering, and backlog.
6. **Whole-machine scheduling** — QEC cycles, factory supply, routing, decoding, controller dependencies, stalls, and retries.
7. **Resource validation** — logical/physical/classical resource estimation, equivalence checks, and independent verification.

Start with [`skills/quantum-operations/SKILL.md`](skills/quantum-operations/SKILL.md). It is the plugin's single cataloged skill and routes each request to the smallest required set of specialist workflow documents.

## Context architecture

The plugin exposes one concise router `SKILL.md`. Specialist workflows, framework/tool notes, research, and worked examples live under `skills/quantum-operations/references/workflows/` and are loaded only when the router selects them. This progressive-disclosure structure preserves the skills metadata budget and avoids injecting the entire quantum catalog into every session.

## Hardware neutrality

The plugin does not encode one vendor, qubit technology, QEC code, compiler, or algorithm as the default answer. Hardware is represented through explicit capabilities and assumptions such as native logical operations, topology, physical error model, cycle time, decoder behavior, code parameters, and target failure probability.

## Implementation quality

Quantum Operations uses an **implementation-complete contract**. The router `SKILL.md` is the routing and decision layer; production implementation loads the selected workflow's `workflow.md`, its `references/implementation.md`, and relevant worked examples before coding. When inputs, outputs, preconditions, algorithm or circuit steps, API details, verification, or failure boundaries need more detail, the agent completes the reference from the primary specification, paper, or current tool documentation first.

See [IMPLEMENTATION_QUALITY.md](IMPLEMENTATION_QUALITY.md) for the coverage matrix and acceptance test.

## Security design

Static knowledge only. No MCP server, hooks, executable scripts, credentials, provider bindings, or write-capable runtime integration are bundled in this release.
