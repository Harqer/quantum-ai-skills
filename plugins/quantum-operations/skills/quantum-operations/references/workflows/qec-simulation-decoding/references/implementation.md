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

## 8. qLDPC decoding branch

For a qLDPC candidate, obtain `Hx`, `Hz`, the exact syndrome circuit, and the physical noise model from `qldpc-architecture`.

For a code-capacity CSS experiment, decode the relevant binary parity-check problem directly. Current `ldpc` 2.1.0 documents BP+OSD:

~~~python
from ldpc import BpOsdDecoder

decoder = BpOsdDecoder(
    H,
    error_rate=physical_error_rate,
    bp_method="product_sum",
    max_iter=max_iter,
    schedule="serial",
    osd_method="osd_cs",
    osd_order=2,
)
estimate = decoder.decode(syndrome)
~~~

and BP+LSD:

~~~python
from ldpc.bplsd_decoder import BpLsdDecoder

decoder = BpLsdDecoder(
    H,
    error_rate=physical_error_rate,
    bp_method="product_sum",
    max_iter=max_iter,
    schedule="serial",
    osd_method="lsd_cs",
    osd_order=2,
)
~~~

For repeated noisy syndrome extraction or circuit-level claims, construct the space-time detector/error-mechanism matrix from the complete syndrome circuit. Treat independent X/Z decoding, correlated decoding, and any hyperedge decomposition as distinct named experiments. A single-round `Hx` or `Hz` code-capacity decoder does not represent circuit-level memory behavior.

Benchmark at least one generic baseline plus the architecture-matched decoder when available. Candidate families include BP+OSD, BP+LSD/localized statistics decoding, ambiguity clustering, graph-augmentation/min-sum methods for correlated errors, Tanner-specific decoders, small-set-flip under expander assumptions, union-find-like decoders, and machine-learned decoders with a reproducible training/evaluation split.

Record decoder configuration, convergence/fallback behavior, mean/p99/p99.9 latency, throughput, memory/bandwidth, and logical error with confidence intervals. Send live timing distributions to `real-time-qec-decoding`.

## 9. Handoff to real-time decoding

This experiment establishes offline decoder correctness and statistical performance; pass its measured latency distribution and detector rate to the real-time decoding skill for live-throughput validation.

For online execution, pass the measured latency distribution, detector rate, code-block concurrency, and logical-operation traces to real-time-qec-decoding.

Sources:
- PyMatching current example: https://pymatching.readthedocs.io/
- Stim: https://github.com/quantumlib/Stim
