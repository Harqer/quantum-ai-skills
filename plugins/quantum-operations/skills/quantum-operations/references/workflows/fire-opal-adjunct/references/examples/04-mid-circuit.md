# Mid-circuit measurements

Give intermediate and final measurements separate classical registers.

~~~python
job = fo.execute(
    circuits=[qasm],
    shot_count=2048,
    credentials=credentials,
    backend_name=backend,
)

registers = job.result()["execution_results"][0]
mid = registers["mcm"]
final = registers["final"]
~~~

Reusing classical bits overwrites earlier measurements.
