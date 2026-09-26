# Example 9: finite-size threshold sweep

Use the vectorized PyMatching construction from Example 4 and retain raw counts rather than only a crossing plot.

~~~python
import numpy as np
from pymatching import Matching

def run_point(H, logicals, p, shots, seed):
    rng = np.random.default_rng(seed)

    matching = Matching.from_check_matrix(
        H,
        weights=np.log((1 - p) / p),
        faults_matrix=logicals,
    )

    noise = (
        rng.random((shots, H.shape[1])) < p
    ).astype(np.uint8)

    syndromes = (noise @ H.T) % 2
    actual = (noise @ logicals.T) % 2
    predicted = matching.decode_batch(syndromes)

    failures = int(np.sum(np.any(predicted != actual, axis=1)))
    return {
        "shots": shots,
        "failures": failures,
        "p_logical": failures / shots,
    }

Ls = [4, 8, 12]
ps = np.linspace(0.06, 0.14, 17)
shots = 20_000

records = []
for L in Ls:
    H = toric_code_x_stabilisers(L)
    logicals = toric_code_x_logicals(L)
    for i, p in enumerate(ps):
        record = run_point(H, logicals, float(p), shots, seed=1000 + 100*L + i)
        records.append({"L": L, "p": float(p), **record})
~~~

Add a binomial confidence interval to every point. A threshold estimate requires finite-size scaling or at least a controlled crossing analysis; a visual crossing alone is exploratory.

The upstream PyMatching toric example reports an expected threshold around 10.3% for its independent perfect-syndrome setup. Carry that number only with that noise model and decoder.

Source:
https://github.com/oscarhiggott/PyMatching/blob/6f63b2b9474ba0fa7e511fe52bffdce858a06984/docs/toric-code-example.ipynb
