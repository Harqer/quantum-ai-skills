# Example 7: PanQEC union-find decoding

PanQEC includes a UnionFindDecoder whose allowed code is Toric2DCode.

~~~python
import numpy as np

from panqec.codes import Toric2DCode
from panqec.decoders import UnionFindDecoder
from panqec.error_models import PauliErrorModel

code = Toric2DCode(20)
error_model = PauliErrorModel(1/3, 1/3, 1/3)
p = 0.10

decoder = UnionFindDecoder(code, error_model, p)

rng = np.random.default_rng(42)
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

Use this path when decoder runtime/parallel structure matters enough to compare against MWPM. Benchmark both on identical generated errors rather than comparing headline thresholds from different noise models.

Source:
https://github.com/panqec/panqec/blob/13886d8f598579f6971707bccdf1f4e2be4607a3/panqec/decoders/union_find/uf_decoder.py
