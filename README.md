# Quantum Operations

**A hardware-agnostic fault-tolerant quantum computing knowledge layer for AI agents.**

Quantum Operations packages the engineering workflows an AI model needs to move from a logical quantum algorithm toward an implementation that can be reasoned about in fault-tolerant terms: fewer logical operations, lower non-Clifford cost, tighter ancilla use, explicit QEC assumptions, practical logical compilation, and defensible physical-resource estimates.

It is intentionally **not a hardware SDK** and **not tied to one algorithm, vendor, qubit modality, or compiler**. The repository is a curated collection of static skills and references that teach the host model how to choose and combine quantum-engineering techniques while keeping the underlying workload exact.

> **Goal:** give AI agents a compact, reusable FTQC engineering playbook without replacing the model, locking it to one framework, or adding a privileged runtime surface.

## What this plugin helps with

Quantum Operations is built around the parts of quantum engineering that become difficult when the goal is not merely to produce a circuit, but to produce one that has a credible path toward fault-tolerant execution.

It helps an agent reason about:

- semantic and reversible circuit reduction before primitive decomposition;
- width, ancilla lifetime, arithmetic structure, and nonlinear Boolean cost;
- Clifford+T and other non-Clifford resource optimization;
- QEC-code and logical-operation strategy;
- syndrome simulation, decoding, and logical error analysis;
- lattice-surgery and topological logical compilation;
- magic-state throughput and factory pressure;
- logical-to-physical resource estimation;
- equivalence, correctness, and fault-tolerance verification;
- interoperability between circuit and fault-tolerant intermediate representations.

The emphasis is **method selection and engineering judgment**. Tool-specific guidance is kept inside the skills that need it, so the top-level context stays small.

## Repository blueprint

Start with the [Quantum Operations router](plugins/quantum-operations/skills/quantum-operations/SKILL.md). It defines the shared engineering contract and selects the specialized skills needed for the current workload.

The repository is organized as a pipeline rather than a flat catalog:

### 1. Reduce the logical workload

**Question:** *Can the computation itself be made smaller before fault-tolerant compilation begins?*

Begin with [Semantic Gate Reduction](plugins/quantum-operations/skills/semantic-gate-reduction/SKILL.md). This layer looks for algebraic simplification, virtual permutations, constant propagation, cross-boundary fusion, and other reductions that generic gate optimizers often miss after decomposition.

Related skills handle reversible arithmetic, Boolean networks, and ancilla lifetime when those become the dominant cost.

### 2. Minimize fault-tolerant gate cost

**Question:** *What is the cheapest exact logical implementation once the algorithm has been structurally simplified?*

Use [Clifford+T Optimization](plugins/quantum-operations/skills/clifford-t-optimization/SKILL.md) for non-Clifford synthesis, Toffoli/T reduction, rotation synthesis tradeoffs, and the distinction between raw logical gate count and fault-tolerant cost.

Circuit-rewriting systems such as PyZX and compiler-pass systems such as pytket are treated as supporting optimization layers, not as substitutes for semantic reasoning.

### 3. Choose an error-corrected execution model

**Question:** *Under what QEC assumptions can the logical circuit actually run?*

Use [QEC Code Strategy](plugins/quantum-operations/skills/qec-code-strategy/SKILL.md) to reason about code families, logical operations, code distance, error budgets, and the assumptions that must be fixed before physical-resource estimates mean anything.

For threshold studies, syndrome generation, decoder evaluation, and logical-error experiments, continue into the QEC simulation/decoding branch selected by the router.

### 4. Compile logical operations into a fault-tolerant schedule

**Question:** *How are logical operations realized in space and time?*

Use [Lattice Surgery](plugins/quantum-operations/skills/lattice-surgery/SKILL.md) when a topological/lattice-surgery model is appropriate. The skill focuses on logical scheduling, patch movement, merges/splits, spacetime tradeoffs, and compilation boundaries rather than a specific hardware vendor.

When non-Clifford operations dominate the schedule, pair this stage with [Magic-State Factories](plugins/quantum-operations/skills/magic-state-factories/SKILL.md) to model distillation throughput and factory pressure instead of treating T gates as free logical primitives.

### 5. Convert logical cost into physical resources

**Question:** *How many physical qubits and how much runtime does the workload require under explicit assumptions?*

Use [FTQC Resource Estimation](plugins/quantum-operations/skills/ftqc-resource-estimation/SKILL.md). This stage separates logical cost from physical cost and makes error models, code parameters, factory assumptions, cycle time, and target failure probability explicit.

The result should be a resource envelope or Pareto frontier, not a single unexplained number.

### 6. Verify before believing the estimate

**Question:** *Did optimization or compilation change the computation, violate a fault-tolerance assumption, or hide a resource regression?*

Use [Fault-Tolerant Verification](plugins/quantum-operations/skills/fault-tolerant-verification/SKILL.md) for equivalence checking, simulation strategy, ancilla/phase correctness, logical validation, and independent cross-checking of resource claims.

This stage is deliberately separate from optimization: the system should be able to challenge its own candidate implementation.

## How to navigate the plugin

```text
plugins/quantum-operations/
├── plugin.json                 # portable plugin manifest
├── .codex-plugin/              # OpenAI/Codex compatibility
├── .claude-plugin/             # Claude Code compatibility
└── skills/
    ├── quantum-operations/     # start here: task router + shared contract
    ├── .../SKILL.md            # focused workflow for one engineering domain
    └── .../references/         # deeper tool/API/technical context loaded only when needed
```

A `SKILL.md` explains **how to reason about a class of quantum-engineering problems**. A skill's `references/` directory contains the more detailed framework or tool guidance needed to carry out that workflow. This keeps routing context lightweight while still allowing deep technical guidance when the task requires it.

You do not need to read every skill. Start with the router, follow the relevant stage in the blueprint above, then descend into references only when implementation details matter.

## Design principles

**Hardware agnostic by default.** Hardware enters as a model of native operations, topology, error rates, timings, QEC constraints, and resource assumptions—not as a hard-coded vendor identity.

**Optimize before lowering.** High-level semantic structure is preserved long enough to expose reductions that disappear after decomposition.

**Fault-tolerant cost is multidimensional.** Logical width, non-Clifford count/depth, ancilla pressure, logical error budget, code distance, spacetime volume, physical qubits, and runtime are kept distinct.

**Exactness first.** Approximation is never silently introduced. Any approximation, synthesis tolerance, or statistical assumption must be explicit.

**Independent verification.** Optimization and verification are separate concerns. A smaller circuit is not accepted merely because one compiler reports fewer gates.

**Progressive disclosure.** Only the relevant skills and references need to enter the model context, preventing a large quantum knowledge base from overwhelming unrelated work.

## Tooling philosophy

Quantum Operations does not try to replace established quantum software. It teaches the model **when a class of tool is appropriate, what assumptions it makes, what metric it actually optimizes, and how to validate its output**.

The plugin includes curated guidance for circuit rewriting and synthesis, QEC simulation and decoding, topological compilation, fault-tolerant resource estimation, and equivalence checking. Tool-specific details live next to the skill that uses them and can evolve without changing the repository's conceptual architecture.

Present-day error-suppression systems such as Fire Opal are kept explicitly outside the FTQC core and treated only as adjuncts when a task concerns current noisy hardware.

## Security and trust model

This repository is intentionally **skills-only**.

It ships with no MCP server, hooks, executable scripts, OAuth flow, credentials, provider bindings, or write-capable runtime integrations. The install surface is static Markdown/JSON knowledge that can be reviewed directly in GitHub.

See [SECURITY.md](SECURITY.md) for the trust model and release guidance.

## Installation

The repository is structured as a ChatGPT/Codex plugin marketplace. The marketplace manifest lives at:

```text
.agents/plugins/marketplace.json
```

For a controlled installation, pin a release tag or commit so the loaded skill set is immutable until you deliberately upgrade it.

## Scope

Quantum Operations is for **engineering and analyzing fault-tolerant quantum computations**. It is not a claim that current hardware can execute every workload described by the plugin, and it does not hide the assumptions needed to move from a logical algorithm to physical-resource estimates.

The project is intentionally broad enough to support cryptography, arithmetic, simulation, scientific algorithms, and other quantum workloads without embedding algorithm-specific rules into the core plugin.

---

**Quantum Operations turns FTQC from a collection of disconnected compiler tricks into a navigable engineering workflow for AI agents.**
