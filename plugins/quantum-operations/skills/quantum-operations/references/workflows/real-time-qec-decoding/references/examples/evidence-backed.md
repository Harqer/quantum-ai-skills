# Executable example: decoder latency, deadline and backlog baseline

**Definition.** Run a published detector-error-model decoder on sampled syndromes, verify its predictions against the batch implementation, and measure per-shot decoding latency. Then model cycle-time arrival/backlog with the measured service times.

Run: `pip install stim pymatching numpy`. Execute on the intended decoder hardware to obtain deployment-specific timing.

~~~python
from time import perf_counter_ns
import numpy as np
import stim
import pymatching

circuit = stim.Circuit.generated(
    "surface_code:rotated_memory_x", distance=3, rounds=3,
    after_clifford_depolarization=0.001,
)
dem = circuit.detector_error_model(decompose_errors=True)
decoder = pymatching.Matching.from_detector_error_model(dem)
detection, truth = circuit.compile_detector_sampler().sample(
    shots=200, separate_observables=True,
)
batch = decoder.decode_batch(detection)
individual = []
latency_ns = []
for shot in detection:
    start = perf_counter_ns()
    individual.append(decoder.decode(shot))
    latency_ns.append(perf_counter_ns() - start)
assert np.array_equal(np.asarray(individual), batch)
assert batch.shape == truth.shape
print("decode p99 ns:", int(np.percentile(latency_ns, 99)))

# Synthetic arrival interval; replace with the target SEC timing.
cycle_ns = 1_000_000
end = 0
backlog = 0
for idx, duration in enumerate(latency_ns):
    arrival = idx * cycle_ns
    start = max(arrival, end)
    backlog = max(backlog, max(0, start - arrival))
    end = start + duration
print("maximum simulated queue delay ns:", backlog)
~~~

**Upstream API and runnable decoder source:** https://pymatching.readthedocs.io/en/stable/api.html and https://github.com/quantumlib/Stim

**Verification:** Correctness is cross-checked against batch decoding. Deadline feasibility is evaluated from the distribution (especially p99 and worst-case backlog), not just average throughput. For a hardware experiment, collect measurement-readout, transport, controller and feed-forward latencies separately.
