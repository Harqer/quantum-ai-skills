# Example 10: 3D toric Sweep + Matching decoding

PanQEC's periodic cubic Toric3DCode places qubits on edges. Its implementation uses weight-six vertex checks and weight-four face checks. SweepMatchDecoder intentionally uses different mechanisms for the two Pauli sectors.

~~~python
import numpy as np

from panqec.codes import Toric3DCode
from panqec.error_models import PauliErrorModel
from panqec.decoders import SweepMatchDecoder

L = 4
p = 0.02

code = Toric3DCode(L)
error_model = PauliErrorModel(1/3, 1/3, 1/3)
decoder = SweepMatchDecoder(code, error_model, p)

rng = np.random.default_rng(5)
error = error_model.generate(code, p, rng=rng)
syndrome = code.measure_syndrome(error)
correction = decoder.decode(syndrome)

residual = (error + correction) % 2
success = (
    code.in_codespace(residual)
    and not code.is_logical_error(residual)
)

print("success:", success)
~~~

The source implementation composes:
- `SweepDecoder3D` for the Z-correction sector;
- `MatchingDecoder(..., error_type="X")` for the X-correction sector.

This asymmetry reflects different excitation geometry in the 3D toric code. It is not evidence that the same decoder split applies to 2D toric code.

Sources:
https://github.com/panqec/panqec/blob/13886d8f598579f6971707bccdf1f4e2be4607a3/panqec/codes/surface_3d/_toric_3d_code.py
https://github.com/panqec/panqec/blob/13886d8f598579f6971707bccdf1f4e2be4607a3/panqec/decoders/sweepmatch/_sweep_match_decoder.py
