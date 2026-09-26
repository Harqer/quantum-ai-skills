# Example 2: PanQEC 2D toric MWPM decode

This follows the current PanQEC tutorial/API at repository commit
`13886d8f598579f6971707bccdf1f4e2be4607a3`.

~~~python
from panqec.codes import Toric2DCode
from panqec.error_models import PauliErrorModel
from panqec.decoders import MatchingDecoder

code = Toric2DCode(4)
assert (code.n, code.k, code.d) == (32, 2, 4)
assert code.is_css

# Conditional X/Y/Z distribution given that an error occurs.
error_model = PauliErrorModel(0.2, 0.3, 0.5)
p = 0.1

decoder = MatchingDecoder(code, error_model, p)

errors = error_model.generate(code, p)
syndrome = code.measure_syndrome(errors)
correction = decoder.decode(syndrome)

residual = (correction + errors) % 2

in_codespace = code.in_codespace(residual)
logical_errors = code.logical_errors(residual)
success = in_codespace and not code.is_logical_error(residual)

print("syndrome:", syndrome)
print("in_codespace:", in_codespace)
print("logical_errors:", logical_errors)
print("success:", success)
~~~

PanQEC stores Pauli operators in binary symplectic form. Its Toric2DCode convention assigns Z to vertex checks and X to face checks, which is globally Hadamard-equivalent to the common textbook convention used in this workflow. Keep one convention throughout a calculation.

The critical success condition is the final pair:

~~~text
in_codespace == True
is_logical_error(residual) == False
~~~

A correction can clear every syndrome bit and still fail logically.

Source:
https://github.com/panqec/panqec/blob/13886d8f598579f6971707bccdf1f4e2be4607a3/docs/tutorials/Panqec%20basics.ipynb
