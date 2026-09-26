# Example 1: square-lattice toric CSS construction

Build the standard square toric code directly instead of relying on a library's naming convention.

~~~python
import numpy as np

def gf2_rank(matrix):
    a = (matrix.copy() & 1).astype(np.uint8)
    rows, cols = a.shape
    rank = 0
    for col in range(cols):
        pivots = np.flatnonzero(a[rank:, col])
        if len(pivots) == 0:
            continue
        pivot = rank + int(pivots[0])
        a[[rank, pivot]] = a[[pivot, rank]]
        for row in range(rows):
            if row != rank and a[row, col]:
                a[row] ^= a[rank]
        rank += 1
        if rank == rows:
            break
    return rank

def toric_css(L):
    n = 2 * L * L

    # h(x,y): horizontal edge from (x,y) to (x+1,y)
    # v(x,y): vertical edge from (x,y) to (x,y+1)
    def h(x, y):
        return (x % L) * L + (y % L)

    def v(x, y):
        return L * L + (x % L) * L + (y % L)

    def check(x, y):
        return (x % L) * L + (y % L)

    Hx = np.zeros((L * L, n), dtype=np.uint8)
    Hz = np.zeros((L * L, n), dtype=np.uint8)

    for x in range(L):
        for y in range(L):
            # Star at vertex (x,y).
            Hx[check(x, y), [
                h(x, y), h(x - 1, y),
                v(x, y), v(x, y - 1),
            ]] = 1

            # Plaquette whose southwest corner is (x,y).
            Hz[check(x, y), [
                h(x, y), h(x, y + 1),
                v(x, y), v(x + 1, y),
            ]] = 1

    assert not np.any((Hx @ Hz.T) % 2)

    rank_x = gf2_rank(Hx)
    rank_z = gf2_rank(Hz)
    k = n - rank_x - rank_z

    assert rank_x == L * L - 1
    assert rank_z == L * L - 1
    assert k == 2
    assert np.all(Hx.sum(axis=1) == 4)
    assert np.all(Hz.sum(axis=1) == 4)

    return Hx, Hz

Hx, Hz = toric_css(3)
assert Hx.shape == (9, 18)
assert Hz.shape == (9, 18)
~~~

For an L by L square torus this verifies the finite code structure
`[[2 L^2, 2, L]]`. The distance claim additionally follows from the shortest noncontractible loop length; Example 8 constructs those loops explicitly.

The two parity-check matrices have one dependency each: the product of all star checks is identity and the product of all plaquette checks is identity.

Verification:
- CSS commutation is exact over GF(2);
- rank establishes two encoded qubits;
- each check has weight four;
- periodic indexing implements the torus rather than an open planar patch.
