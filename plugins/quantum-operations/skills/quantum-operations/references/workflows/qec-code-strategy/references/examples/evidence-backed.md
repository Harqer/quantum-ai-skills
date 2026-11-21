# Executable example: select distance from sampled logical failure

**Definition.** Measure logical failure under one specified noise model and decoder, compute a confidence bound, and choose the smallest candidate meeting a workload error budget. This is a reproducible selection procedure, not a universal distance formula.

Run: `pip install stim pymatching numpy`.

~~~python
from math import sqrt
import numpy as np
import stim
import pymatching

shots, error_budget, logical_locations = 10000, 0.05, 100

def wilson_upper(errors, trials, z=1.959963984540054):
    p = errors / trials
    d = 1 + z*z/trials
    center = (p + z*z/(2*trials))/d
    half = z*sqrt((p*(1-p) + z*z/(4*trials))/trials)/d
    return min(1.0, center + half)

candidates = []
for d in (3, 5, 7):
    circuit = stim.Circuit.generated(
        "surface_code:rotated_memory_x",
        distance=d, rounds=d,
        after_clifford_depolarization=0.001,
    )
    dem = circuit.detector_error_model(decompose_errors=True)
    decoder = pymatching.Matching.from_detector_error_model(dem)
    detections, truth = circuit.compile_detector_sampler().sample(
        shots=shots, separate_observables=True
    )
    prediction = decoder.decode_batch(detections)
    errors = int(np.count_nonzero(np.any(prediction != truth, axis=1)))
    upper = wilson_upper(errors, shots)
    candidates.append((d, upper))
    print(d, "failures:", errors, "95% upper bound:", upper)

accepted = [d for d, upper in candidates if logical_locations * upper <= error_budget]
print("distance satisfying sampled conservative budget:", min(accepted) if accepted else None)
assert all(0 <= upper <= 1 for _, upper in candidates)
~~~

**Primary APIs:** https://pymatching.readthedocs.io/en/stable/api.html and https://github.com/quantumlib/Stim

**Verification:** Re-run with the exact decoder configuration, rounds, circuit-level noise, workload length and shot count recorded. Select using the upper confidence bound; if no candidate qualifies, enlarge the candidate set or shot budget.
