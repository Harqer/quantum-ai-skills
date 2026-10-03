# Example: Circuit-to-Tensor end-to-end

```bash
cargo install --git https://github.com/tlaakkonen/circuit-to-tensor.git
circuit-to-tensor compile out original.qasm -z -v
```

Retain each non-Clifford block's `*.tensor.npy`, `*.matrix.npy`, `*.mapping.txt`, and `*.cnotphase.qasm`. Produce a lower-rank compatible factorization, then resynthesize with the original matrix and mapping:

```bash
circuit-to-tensor resynth resynth optimized.npy \
  -O out/original.block1.matrix.npy \
  -m out/original.block1.mapping.txt \
  -g
circuit-to-tensor verify original.qasm optimized.qasm
```

Do not omit the original matrix/mapping when exact correspondence to the compiled block is required.
