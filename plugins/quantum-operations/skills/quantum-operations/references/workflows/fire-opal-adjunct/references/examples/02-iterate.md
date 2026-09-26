# Iterate

Keep one parameterized QASM circuit and bind values at runtime.

~~~python
jobs = []
for batch in parameter_batches:  # each <= 300 bindings
    jobs.append(
        fo.iterate(
            circuits=[parameterized_qasm],
            parameters=batch,
            shot_count=2048,
            credentials=credentials,
            backend_name=backend,
        )
    )

results = [j.result() for j in jobs]
fo.stop_iterate(credentials, backend)
~~~

Use `iterate` instead of independent `execute` calls for consecutive workloads.
