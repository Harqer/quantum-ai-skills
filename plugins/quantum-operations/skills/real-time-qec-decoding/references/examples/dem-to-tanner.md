# Example: detector error model to Tanner graph

This example shows the exact data relationship a decoder operates on:

```text
error mechanisms e  --H-->  detector outcomes d
```

over GF(2):

```math
H e = d \pmod 2.
```

A Tanner graph is the bipartite graph of the binary matrix `H`:

- one node set = detector/check rows;
- the other node set = candidate error-mechanism columns;
- an edge exists wherever `H[row, column] = 1`.

## Minimal Stim-style DEM

Consider the detector error model

```text
error(0.125) D0
error(0.125) D0 D1
```

This is the small example produced in Stim's command-line documentation from a two-qubit circuit.

Define two error variables:

```text
e0 = first error mechanism
e1 = second error mechanism
```

and detector vector

```text
d = [D0, D1]^T.
```

The corresponding parity-check matrix is

```math
H =
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}.
```

The Tanner graph is therefore

```text
e0 ───── D0

e1 ───── D0
 └────── D1
```

with error priors

```math
p = [0.125, 0.125].
```

## Exact syndrome checks

If only `e0` occurs,

```math
e =
\begin{bmatrix}
1\\
0
\end{bmatrix},
\qquad
H e =
\begin{bmatrix}
1\\
0
\end{bmatrix}.
```

So the detector pattern is

```text
D0 = 1
D1 = 0
```

If only `e1` occurs,

```math
e =
\begin{bmatrix}
0\\
1
\end{bmatrix},
\qquad
H e =
\begin{bmatrix}
1\\
1
\end{bmatrix}.
```

So both detectors fire.

If both occur,

```math
H
\begin{bmatrix}
1\\
1
\end{bmatrix}
=
\begin{bmatrix}
0\\
1
\end{bmatrix}
\pmod 2.
```

This is why a decoder is not selecting a correction from detector nodes alone. It searches over error variables whose parity under `H` reproduces the observed detector vector, while using the prior probabilities and a decoding objective to choose among compatible explanations.

## DEM versus code parity-check matrix

Do not conflate these two objects:

1. A stabilizer/QEC-code parity-check matrix describes the code's checks on qubits.
2. A detector-error-model matrix maps **circuit-level error mechanisms to detector events in spacetime**.

For repeated noisy syndrome extraction, the latter can include time as well as space and can be much larger than the static code-check matrix.

Source:

- Stim detector error model documentation: https://github.com/quantumlib/Stim/blob/main/doc/file_format_dem_detector_error_model.md
- Stim command-line examples: https://github.com/quantumlib/Stim/blob/main/doc/usage_command_line.md
