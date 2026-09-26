# Example 4: PyMatching code-capacity toric decoder

This construction follows the upstream PyMatching toric-code notebook at commit
`6f63b2b9474ba0fa7e511fe52bffdce858a06984`.

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

L = 8
p = 0.08
shots = 10_000

H = toric_code_x_stabilisers(L)
logicals = toric_code_x_logicals(L)

matching = Matching.from_check_matrix(
    H,
    weights=np.log((1 - p) / p),
    faults_matrix=logicals,
)

noise = (
    np.random.random((shots, H.shape[1])) < p
).astype(np.uint8)

syndromes = (noise @ H.T) % 2
actual = (noise @ logicals.T) % 2
predicted = matching.decode_batch(syndromes)

failures = np.sum(np.any(predicted != actual, axis=1))
p_logical = failures / shots

print("failures:", failures)
print("logical failure rate:", p_logical)
~~~

This is a code-capacity experiment: data-qubit Z errors with perfect X-check measurements. It is not a phenomenological or circuit-level threshold.

Source:
https://github.com/oscarhiggott/PyMatching/blob/6f63b2b9474ba0fa7e511fe52bffdce858a06984/docs/toric-code-example.ipynb
