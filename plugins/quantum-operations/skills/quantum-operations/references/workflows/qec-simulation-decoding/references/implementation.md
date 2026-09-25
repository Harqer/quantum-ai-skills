# QEC simulation and decoding: executable reference

This is the minimum runnable experiment shape for a graphlike surface-code decoding study.

## 1. Generate a detector-annotated noisy circuit

~~~python
import stim

circuit = stim.Circuit.generated(
    "surface_code:rotated_memory_x",
    distance=5,
    rounds=5,
    after_clifford_depolarization=0.005,
)
~~~

Use Stim generated circuits as starter/reference circuits, and substitute the actual syndrome-extraction circuit when evaluating a production architecture.

## 2. Build the detector error model

For PyMatching graphlike decoding:

~~~python
model = circuit.detector_error_model(
    decompose_errors=True,
)
~~~

decompose_errors=True asks Stim to decompose suitable mechanisms so they can be represented as graphlike matching edges.

Record this as an experimental assumption and label the graphlike-decomposed experiment separately from an undecomposed correlated-model experiment.

## 3. Construct the decoder

~~~python
import pymatching

matching = pymatching.Matching.from_detector_error_model(model)
~~~

For correlated matching:

~~~python
matching_corr = pymatching.Matching.from_detector_error_model(
    model,
    enable_correlations=True,
)
~~~

and use the same setting during decode.

## 4. Sample and decode

~~~python
import numpy as np

sampler = circuit.compile_detector_sampler()

syndrome, actual_observables = sampler.sample(
    shots=10_000,
    separate_observables=True,
)

pred = matching.decode_batch(syndrome)

failures = np.any(pred != actual_observables, axis=1)
logical_error_rate = failures.mean()
num_failures = failures.sum()
~~~

For correlated matching:

~~~python
pred_corr = matching_corr.decode_batch(
    syndrome,
    enable_correlations=True,
)
~~~

## 5. Confidence interval

Report every Monte Carlo proportion together with an uncertainty interval and the corresponding sample counts.

For k failures in n independent shots, use a binomial confidence interval such as Wilson.

~~~python
from math import sqrt

def wilson_interval(k, n, z=1.959963984540054):
    if n == 0:
        raise ValueError("n must be positive")
    p = k / n
    denom = 1 + z*z/n
    center = (p + z*z/(2*n)) / denom
    half = z * sqrt(p*(1-p)/n + z*z/(4*n*n)) / denom
    return center - half, center + half
~~~

State the confidence level and stopping rule.

## 6. Distance / error-rate sweep

For each tuple:

~~~text
(code family, distance, rounds, physical error rate, decoder config)
~~~

store:
- shots;
- failures;
- logical failure estimate;
- interval;
- decoder runtime distribution;
- DEM generation settings;
- git/package versions.

Maintain separate labeled threshold datasets for code-capacity, phenomenological, and circuit-level noise models.

## 7. Detector/observable sanity

Before decoding:
- ensure circuit.num_detectors > 0;
- ensure intended logical observables are annotated;
- inspect a small DEM;
- use Stim error explanation tooling for suspicious detector mechanisms;
- verify expected determined-measurement count where applicable.

## 8. Handoff to real-time decoding

This experiment establishes offline decoder correctness and statistical performance; pass its measured latency distribution and detector rate to the real-time decoding skill for live-throughput validation.

For online execution, pass the measured latency distribution, detector rate, code-block concurrency, and logical-operation traces to real-time-qec-decoding.

Sources:
- PyMatching current example: https://pymatching.readthedocs.io/
- Stim: https://github.com/quantumlib/Stim
