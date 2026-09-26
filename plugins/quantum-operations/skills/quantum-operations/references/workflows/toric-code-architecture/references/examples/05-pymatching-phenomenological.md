# Example 5: repeated noisy toric syndrome measurements

For an exact repeated-measurement reference path, qecsim 1.0b9 provides a fault-tolerant/time-periodic simulator for its rotated toric code and symmetry-aware MWPM decoder.

~~~python
from qecsim import app
from qecsim.models.generic import BitPhaseFlipErrorModel
from qecsim.models.rotatedtoric import (
    RotatedToricCode,
    RotatedToricSMWPMDecoder,
)

code = RotatedToricCode(6, 6)
decoder = RotatedToricSMWPMDecoder()
error_model = BitPhaseFlipErrorModel()

result = app.run_ftp(
    code=code,
    time_steps=6,
    error_model=error_model,
    decoder=decoder,
    error_probability=0.02,
    measurement_error_probability=0.02,
    max_runs=10_000,
    max_failures=500,
    random_seed=7,
)

print(result)
~~~

This experiment belongs to the phenomenological/time-periodic evidence layer:
- data errors accumulate over rounds;
- syndrome measurements can be faulty;
- decoding uses the time dimension;
- reported performance must stay separate from perfect-measurement code capacity.

The exact API is exercised in qecsim's own test suite with `RotatedToricCode(6, 6)`, `time_steps=6`, and `RotatedToricSMWPMDecoder()`.

Sources:
https://github.com/qecsim/qecsim/blob/24d6b8a320b292461b66b68fe4fba40c9ddc2257/src/qecsim/app.py
https://github.com/qecsim/qecsim/blob/24d6b8a320b292461b66b68fe4fba40c9ddc2257/tests/core/test_app.py
