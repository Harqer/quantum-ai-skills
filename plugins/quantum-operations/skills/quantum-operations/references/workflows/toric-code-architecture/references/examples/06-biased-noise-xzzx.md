# Example 6: biased-noise toric candidate with XZZX deformation

PanQEC exposes Clifford deformations directly on Toric2DCode. Compare the undeformed and deformed candidates under the same physical error probability and bias.

~~~python
import numpy as np

from panqec.codes import Toric2DCode
from panqec.error_models import PauliErrorModel
from panqec.decoders import MatchingDecoder

L = 8
p = 0.02
seed = 11

code = Toric2DCode(L)

# Strong Z bias: probabilities are conditional on an error.
biased = (0.01, 0.01, 0.98)

plain_model = PauliErrorModel(*biased)
xzzx_model = PauliErrorModel(
    *biased,
    deformation_name="XZZX",
    deformation_kwargs={"deformation_axis": "y"},
)

def trial(error_model):
    rng = np.random.default_rng(seed)
    decoder = MatchingDecoder(code, error_model, p)
    error = error_model.generate(code, p, rng=rng)
    syndrome = code.measure_syndrome(error)
    correction = decoder.decode(syndrome)
    residual = (error + correction) % 2
    return (
        code.in_codespace(residual)
        and not code.is_logical_error(residual)
    )

print("plain:", trial(plain_model))
print("XZZX:", trial(xzzx_model))
~~~

A single shot does not establish an advantage. Sweep lattice size and physical error rate, use independent samples, and compare logical failure with confidence intervals. The deformation is useful only when the decoder and effective distance exploit the actual bias.

The Toric2DCode source declares `XZZX` and `XY` deformations; the XZZX map exchanges X and Z on qubits belonging to the selected deformation axis.

Source:
https://github.com/panqec/panqec/blob/13886d8f598579f6971707bccdf1f4e2be4607a3/panqec/codes/surface_2d/_toric_2d_code.py
