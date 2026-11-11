# Example: finite-step Floquet Max-Cut

```python
def floquet_schedule(edges, n_vertices, dt, T):
    m = round(T / dt)
    for k in range(1, m + 1):
        s = k / m
        for u, v in edges:
            yield ("RZZ", u, v, -2.0 * s * dt)
        for q in range(n_vertices):
            yield ("RX", q, 2.0 * (1.0 - s) * dt)
```

The exact signs/factors depend on the target library's exponential convention. Derive and unit-test them from that library's gate definition before execution.

Prepare `|+>^L`, apply the complete schedule, measure in Z, score Max-Cut, and repeat for the declared shots/stopping rule. This is objective-equivalent/heuristic, not an exact rewrite of continuous adiabatic evolution.
