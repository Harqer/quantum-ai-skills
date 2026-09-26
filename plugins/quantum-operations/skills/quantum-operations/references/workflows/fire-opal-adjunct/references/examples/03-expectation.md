# Expectation estimation

~~~python
from fireopal.types import PauliOperator

observable = PauliOperator.from_list([
    ("ZZI", 0.5),
    ("IZZ", 0.5),
])

job = fo.estimate_expectation(
    circuits=[qasm],
    observables=observable,
    shot_count=2048,
    credentials=credentials,
    backend_name=backend,
)

result = job.result()
expectation = result["expectation_values"]
uncertainty = result["standard_deviations"]
~~~
