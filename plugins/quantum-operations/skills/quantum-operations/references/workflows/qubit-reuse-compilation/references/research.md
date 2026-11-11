# Research basis

1. DeCross et al., "Qubit-reuse compilation with mid-circuit measurement and reset", arXiv:2210.08039: exact constraint-programming and greedy algorithms, dual circuit, and an 80-qubit QAOA circuit executed on 20-qubit Quantinuum H1-1.
2. Quantinuum Nexus "Qubit Reuse Compilation": current HyperTKET API, causal-cone ordering, documented 7->2-qubit example, ordering/DualStrat behavior.
3. Quantinuum Guppy/Helios qsystem: measure, measure_and_reset, reset, qfree, lazy variants.

Revalidate `quantinuum_schemas.models.hypertket_config` names and device configuration immediately before production code.
