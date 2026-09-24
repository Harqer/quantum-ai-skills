# Example: IonQ BeamSearchDecoder code path

Primary implementation:

https://github.com/ionq-publications/BeamSearchDecoder

The published Python wrapper makes the DEM → Tanner/check-matrix boundary explicit.

## 1. Input is a Stim detector error model

The public class is initialized with

```python
model: stim.DetectorErrorModel
```

IonQ's wrapper calls the `stimbposd` conversion utility:

```python
detector_error_model_to_check_matrices(
    model,
    allow_undecomposed_hyperedges=True,
)
```

The returned structure contains at least:

```text
check_matrix
priors
observables_matrix
```

The decoder therefore does not receive the original quantum circuit directly. The noisy circuit has already been reduced to an error-mechanism/check representation.

Source file:

https://github.com/ionq-publications/BeamSearchDecoder/blob/main/beamsearch.py

## 2. Sparse parity-check matrix plus priors drive the C++ decoder

The Python wrapper constructs the decoder using

```text
pcm    = check_matrix
priors = per-error-mechanism probabilities
```

and passes those to `BeamSearchDecoder`.

The conceptual input is therefore

```math
(H, p, d)
```

where:

- `H` = sparse Tanner/parity-check matrix;
- `p` = prior probability for each error-variable column;
- `d` = observed detector vector for one shot/window.

## 3. Initial belief-propagation likelihoods

In the C++ implementation, each error variable is initialized with a log-likelihood ratio

```math
\lambda_i^{(0)}
=
\log\left(\frac{1-p_i}{p_i}\right).
```

This is written onto Tanner edges as the initial variable-to-check message.

Source:

```text
decoder/src_cpp/beam_search.hpp
initialise_log_domain_bp()
```

## 4. Check-to-variable and variable-to-check message passing

The implementation iterates over rows of the sparse matrix for check-to-variable updates and over columns for variable-to-check updates.

A hard decision for error variable `i` is made from the sign of its posterior LLR.

When an error variable is decided active, the candidate syndrome is updated by XORing all detector rows connected to that column.

The decoder tests convergence by comparing

```text
candidate_syndrome == observed_syndrome
```

which is the operational form of

```math
H \hat e = d \pmod 2.
```

## 5. What beam search adds when ordinary BP is uncertain

The implementation accumulates LLR information and selects uncertain error variables for branching.

It maintains multiple candidate paths up to a configured beam width. A path fixes selected error variables to 0 or 1, reruns message passing with those fixed assignments, scores the remaining uncertainty, and keeps only the strongest candidate paths.

Important implementation detail from the source:

```text
columns with Tanner degree <= 2 are skipped when choosing the initial branch variable
```

in the current beam-search implementation.

Treat that branch-selection rule as an implementation-specific choice and validate its effect explicitly before using it with another decoder or code family.

## 6. Published configurations

The accompanying simulation code defines concrete configurations including:

```text
beam8_230iters
beam32_340iters
beam64_640iters
beam64_32res_640iters
```

For example, `beam32_340iters` is configured with:

```text
beam_width      = 32
initial_iters   = 40
iters_per_round = 30
```

The names/configurations are benchmark points, not universally optimal settings.

Source:

https://github.com/ionq-publications/BeamSearchDecoder/blob/main/simulation_functions.py

## 7. Observable prediction after decoding

The C++ decoder returns a binary error-mechanism correction vector `corr`.

The Python wrapper converts that into logical-observable predictions using

```math
\text{prediction}
=
O \cdot \text{corr}
\pmod 2,
```

where `O` is the DEM-derived observable matrix.

So the full public path is:

```text
Stim circuit / DEM
      ↓
detector_error_model_to_check_matrices
      ↓
H = check_matrix
p = priors
O = observables_matrix
      ↓
BeamSearchDecoder(H, p)
      ↓
decode detector vector d
      ↓
correction vector e_hat
      ↓
O @ e_hat mod 2
      ↓
logical observable prediction
```

## 8. Relationship to a streaming decoder

The public BeamSearchDecoder repository demonstrates the **inner decoder** mechanics.

A real-time sliding-window system still needs an outer layer that:

- constructs/selects the active window matrix;
- handles first/middle/last temporal boundaries;
- merges window-induced duplicate columns when appropriate;
- adjusts active detector data for already committed errors;
- commits only the safe region;
- manages latency/backlog and feed-forward deadlines.

For the concrete outer-loop construction, see [walking-cat-sliding-window.md](walking-cat-sliding-window.md).

## 9. Reproduction checklist

When reproducing this flow in another stack:

1. Confirm how the DEM-to-matrix converter handles hyperedges/correlations.
2. Inspect matrix dimensions and sparsity.
3. Verify each column's detector signature on a small known circuit.
4. Confirm priors line up one-to-one with error-variable columns.
5. Check `H @ e_hat mod 2 == d` for every successful decode.
6. Independently verify observable predictions.
7. Benchmark tail latency, not only logical error rate.
8. Keep the outer streaming/windowing semantics separate from the inner decoder.
