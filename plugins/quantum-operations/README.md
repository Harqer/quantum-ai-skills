# Quantum Operations Plugin

Quantum Operations is a hardware-agnostic skill collection for designing, optimizing, validating, and costing **fault-tolerant quantum computations**.

The plugin is intentionally a knowledge layer rather than a runtime integration. It gives the host model reusable engineering workflows while leaving hardware selection, provider access, and execution to the surrounding environment.

## Technical scope

The router coordinates five broad domains:

1. **Logical reduction** — semantic simplification, reversible arithmetic, Boolean fusion, and ancilla lifetime.
2. **Fault-tolerant synthesis** — Clifford+T / non-Clifford optimization plus supporting circuit-rewrite and compiler passes.
3. **Quantum error correction** — code strategy, logical operation models, syndrome simulation, decoding, and logical error analysis.
4. **Logical FT compilation** — topological/lattice-surgery scheduling and magic-state production where applicable.
5. **Resource validation** — logical-to-physical resource estimation, equivalence checks, and independent verification.

Start with [`skills/quantum-operations/SKILL.md`](skills/quantum-operations/SKILL.md). It selects the minimum set of specialized skills needed for the current task.

## Context architecture

Each skill has a concise `SKILL.md`. Deeper framework/tool notes are stored under `references/` and are loaded only when implementation detail is relevant. This progressive-disclosure structure is designed to preserve model context rather than inject the entire knowledge base into every quantum task.

## Hardware neutrality

The plugin does not encode one vendor, qubit technology, QEC code, compiler, or algorithm as the default answer. Hardware is represented through explicit capabilities and assumptions such as native logical operations, topology, physical error model, cycle time, decoder behavior, code parameters, and target failure probability.

## Security design

Static knowledge only. No MCP server, hooks, executable scripts, credentials, provider bindings, or write-capable runtime integration are bundled in this release.
