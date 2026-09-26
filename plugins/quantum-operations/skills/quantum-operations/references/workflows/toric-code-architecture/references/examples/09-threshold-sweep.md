# Example 9: finite-size threshold sweep

This example is self-contained and follows the PyMatching toric-code construction used upstream.

~~~python
import numpy as np
from scipy.sparse import hstack, kron, eye, csc_matrix, block_diag
from pymatching import Matching

def repetition_code(n):
    row_ind, col_ind = zip(*(
        (i, j)
        for i in range(n)
        for j in (i, (i + 1) % n)
    ))
    data = np.ones(2 * n, dtype=np.uint8)
    return csc_matrix((data, (row_ind, col_ind)))

def toric_code_x_stabilisers(L):
    Hr = repetition_code(L)
    H = hstack(
        [
            kron(Hr, eye(Hr.shape[1])),
            kron(eye(Hr.shape[0]), Hr.T),
        ],
        dtype=np.uint8,
    )
    H.data %= 2
    H.eliminate_zeros()
    return csc_matrix(H)

def toric_code_x_logicals(L):
    H1 = csc_matrix(([1], ([0], [0])), shape=(1, L), dtype=np.uint8)
    H0 = csc_matrix(np.ones((1, L), dtype=np.uint8))
    logicals = block_diag([kron(H1, H0), kron(H0, H1)])
    logicals.data %= 2
    logicals.eliminate_zeros()
    return csc_matrix(logicals)

def wilson_interval(k, n, z=1.959963984540054):
    p = k / n
    denom = 1 + z*z/n
    center = (p + z*z/(2*n)) / denom
    half = z * np.sqrt(p*(1-p)/n + z*z/(4*n*n)) / denom
    return center - half, center + half

def run_point(H, logicals, p, shots, seed):
    rng = np.random.default_rng(seed)
    matching = Matching.from_check_matrix(
        H,
        weights=np.log((1 - p) / p),
        faults_matrix=logicals,
    )

    noise = (rng.random((shots, H.shape[1])) < p).astype(np.uint8)
    syndromes = (noise @ H.T) % 2
    actual = (noise @ logicals.T) % 2
    predicted = matching.decode_batch(syndromes)

    failures = int(np.sum(np.any(predicted != actual, axis=1)))
    lo, hi = wilson_interval(failures, shots)
    return {
        "shots": shots,
        "failures": failures,
        "p_logical": failures / shots,
        "ci95": (lo, hi),
    }

Ls = [4, 8, 12]
ps = np.linspace(0.06, 0.14, 17)
shots = 20_000

records = []
for L in Ls:
    H = toric_code_x_stabilisers(L)
    logicals = toric_code_x_logicals(L)
    for i, p in enumerate(ps):
        records.append({
            "L": L,
            "p": float(p),
            **run_point(H, logicals, float(p), shots, 1000 + 100*L + i),
        })
~~~

A threshold estimate requires finite-size scaling or a controlled crossing analysis. The upstream PyMatching toric example reports an expected threshold around 10.3% for this independent perfect-syndrome setup. Carry that value only with this noise model and decoder.

Source:
https://github.com/oscarhiggott/PyMatching/blob/6f63b2b9474ba0fa7e511fe52bffdce858a06984/docs/toric-code-example.ipynb
