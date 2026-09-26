# Example 3: qecsim toric MWPM and logical-success test

qecsim exposes the geometry and logical-commutation test directly. This example is tied to qecsim 1.0b9.

~~~python
import numpy as np
from qecsim import paulitools as pt
from qecsim.models.generic import DepolarizingErrorModel
from qecsim.models.toric import ToricCode, ToricMWPMDecoder

code = ToricCode(5, 5)
assert code.n_k_d == (50, 2, 5)

error_model = DepolarizingErrorModel()
decoder = ToricMWPMDecoder()

rng = np.random.default_rng(59)
error = error_model.generate(code, 0.1, rng)

syndrome = pt.bsp(error, code.stabilizers.T)
recovery = decoder.decode(code, syndrome)
residual = recovery ^ error

# Returning to the codespace:
residual_syndrome = pt.bsp(residual, code.stabilizers.T)
assert not residual_syndrome.any()

# Logical success requires trivial residual homology:
logical_commutations = pt.bsp(residual, code.logicals.T)
success = not logical_commutations.any()

print("logical commutations:", logical_commutations)
print("success:", success)
~~~

The decoder resolves syndrome plaquettes, forms a weighted graph, performs minimum-weight perfect matching, and joins each matched pair along a shortest periodic path.

Source:
https://github.com/qecsim/qecsim/blob/24d6b8a320b292461b66b68fe4fba40c9ddc2257/docs/demos/demo_toric.rst
