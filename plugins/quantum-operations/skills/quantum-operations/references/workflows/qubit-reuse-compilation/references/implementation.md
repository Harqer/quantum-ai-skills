# Qubit reuse compilation: implementation reference

## Input/output

Input: circuit DAG, preparations, outputs/measurements, classical dependencies, target MCMR support, measurement/reset latency/error. Output: observationally equivalent dynamic circuit plus logical->physical lifetime map.

## Causal-cone algorithm

For each measured output, compute its backward causal cone. Repeatedly choose an executable cone:
1. schedule newly required gates in dependency order;
2. measure outputs whose semantic measurement point is reached;
3. reset physical qubits with zero remaining coherent dependencies;
4. return reset carriers to the free pool;
5. allocate later logical qubits from that pool.

Use exact search/constraint programming for small instances and greedy ordering for large instances. Score by incremental live-qubit demand and tie-break on depth/gates.

Evaluate the dual circuit when supported: exchange preparations/measurements and reverse time, optimize reuse, reverse the resulting construction, and compare exact candidates.

## Quantinuum HyperTKET API

Current Nexus exposes `HyperTketConfig` / `QubitReuseConfig` with BruteForce, ConstrainedOpt (CP-SAT), LocalGreedy, LocalGreedyFirstNodeSearch, Default, and Custom ordering configs. `DualStrat.AUTO` evaluates original/dual behavior.

## Verification

Compare output semantics against the original; assert no use-after-measure/reset; require reset before reuse; preserve classical labels/output ordering; compare width, 2Q count, measurements, resets, and depth.

## Failure boundaries

Do not reuse across unresolved quantum dependencies, entanglement with live data, unsupported dynamic-control boundaries, or targets lacking compatible MCMR.
