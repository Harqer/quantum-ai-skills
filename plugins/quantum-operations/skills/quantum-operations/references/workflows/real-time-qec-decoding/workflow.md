---
name: real-time-qec-decoding
description: Engineer streaming QEC decoders that keep pace with fault-tolerant computation. Use for online syndrome streams, sliding/modular windows, decoder deadlines, tail latency, backlog, convergence failures, dynamic detector error models, and classical decoder provisioning.
---

# Real-Time QEC Decoding

Treat the decoder as part of the execution system. Capture the QEC code and logical-operation protocol, syndrome-cycle duration, detector production rate, graph/model changes introduced by logical operations, critical-path decoded outputs, allowed buffering and look-ahead, decoder error contribution, concurrent code blocks, and available CPU/GPU/FPGA/ASIC compute and memory. Establish the real-time claim from sustained throughput, deadline behavior, and high-percentile latency rather than from an average-latency number.

For streaming or windowed decoding, define the window, commit region, and look-ahead region explicitly, preserve the code's required fault distance across partition boundaries, carry boundary state forward, and commit the oldest region only when the available detector context makes that region causally complete under the selected protocol. Measure logical error, mean and p99/p99.9 latency, deadline misses, backlog growth and drain behavior, convergence/restart rate, and concurrent memory/bandwidth pressure on full logical-operation traces.

Represent detector error models as error mechanisms with probabilities, detector signatures, and logical-frame effects. Reuse a static graph when the target architecture proves that only priors change, and rebuild or update the relevant structure when checks, connectivity, boundaries, or correlations change. Different runtime outputs may use different decoder configurations when the total logical-error budget and latency requirements justify that specialization.

Provision classical compute from the number of live blocks, detector arrival rate, service-time distribution, communication cost, operation bursts, memory bandwidth, and required backlog margin. Feed decoder completions and deadline misses into `ftqc-runtime-scheduling` so execution stalls and stretch emerge from explicit events.

## Implementation gate

Apply `../quantum-operations/references/implementation-contract.md`, then load `references/research.md` and the smallest relevant file under `references/examples/`. The worked examples provide the implementation layer for DEM/Tanner conversion, Walking Cat sliding windows, and the published IonQ beam-search code path. Carry each architecture-specific matrix, merge rule, or decoder setting together with the assumptions established by its source.
