# Example: Walking Cat six-SEC sliding-window Tanner construction

Primary source: Tripier et al., *Fault-Tolerant Quantum Computing with Trapped Ions: The Walking Cat Architecture*, Sec. XVII.B–E, especially Proposition 5 and Sec. XVII.C, arXiv:2604.19481.

This file records the paper's concrete six-syndrome-extraction-cycle example without treating its architecture-specific blocks as universal.

## 1. Convert syndromes into detector outcomes

Let the measured syndrome vectors be

```text
s0, s1, s2, ...
```

The streaming decoder uses

```math
d_0 = s_0,
```

and for `i >= 1`,

```math
d_i = s_i \oplus s_{i-1}.
```

This temporal differencing localizes the detector signature of persistent faults and gives the repeated parity-check matrix its staircase structure.

## 2. Six-SEC global block matrix

For `r = 6` SECs, Proposition 5 gives an `r x (2r-1) = 6 x 11` block matrix:

```text
[ H0'  H1                                      ]
[      H2   H0   H1                            ]
[           H2   H0   H1                       ]
[                H2   H0   H1                  ]
[                     H2   H0   H1             ]
[                          H2   H0''            ]
```

The corresponding prior vector has 11 block subvectors:

```text
(p0', p1, p0, p1, p0, p1, p0, p1, p0, p1, p0'')
```

The first and final even blocks are special temporal-boundary blocks; they are not interchangeable with the repeated interior `H0` block.

## 3. Error-type interpretation

The paper derives the block pattern from four circuit-level fault classes:

| Type | Behavior in raw syndrome sequence | Detector support |
| --- | --- | --- |
| I: transient | changes `s_i` only | `d_i`, `d_{i+1}` |
| II: early persistent | same effect in every `s_j`, `j >= i` | `d_i` only |
| III: mid-cycle persistent | partial effect in `s_i`, steady effect later | `d_i`, `d_{i+1}` |
| IV: late persistent | first visible in `s_{i+1}` | `d_{i+1}` only |

Therefore:

- even block columns correspond to single-detector-time support;
- odd block columns correspond to support spanning two adjacent detector times.

This is a consequence of this repeated syndrome-extraction circuit and detector transform, not a generic Tanner-graph law.

## 4. Exact `(w,c)=(3,1)` first window

The paper chooses:

```text
window size w = 3 SECs
commit size c = 1 SEC
total SECs r = 6
```

The first active detector segment is

```text
(d0, d1, d2)
```

and the first active parity-check submatrix is

```text
H_win1 =
[ H0'  H1                 ]
[      H2   H0   H1       ]
[           H2   H0   H1  ]
```

This is a `3 x 6` block matrix.

Its prior vector is

```text
p_win1 = (p0', p1, p0, p1, p0, p1)
```

and, before boundary merging, the inner decoder is solving for error blocks

```text
(e0, e1, e2, e3, e4, e5).
```

## 5. Why the final block of a truncated window must be checked for duplicate columns

The full global matrix is assumed to have unique columns after simplification. In an interior odd block, uniqueness can depend on the vertically combined signature

```text
[ H1 ]
[ H2 ]
```

across two detector times.

When a decoding window truncates the lower `H2` support, two globally distinct columns can become identical when viewed only through the terminal `H1` block.

The paper therefore constructs

```text
H1_merge
```

by merging identical columns in the terminal `H1` block of a non-final window.

The first-window matrix becomes

```text
H_win1_merge =
[ H0'  H1                       ]
[      H2   H0   H1             ]
[           H2   H0   H1_merge  ]
```

with prior vector

```text
p_win1_merge = (p0', p1, p0, p1, p0, p1_merge).
```

### Exact prior-combination rule

For two independent error mechanisms whose active-window Tanner columns are identical, with probabilities `p_i` and `p_j`,

```math
p_{merge}
= p_i(1-p_j) + p_j(1-p_i)
= p_i + p_j - 2 p_i p_j.
```

The merged bit represents the XOR/parity of the two underlying mechanisms.

Example:

```text
p_i = 1e-4
p_j = 2e-4

p_merge = 0.0001*(0.9998) + 0.0002*(0.9999)
        = 0.00029996
```

The numeric values above are illustrative; the combination rule is the paper's.

## 6. Commit only causally complete error support

With `c = 1`, the first window does **not** commit all six decoded error blocks.

It commits only

```text
e0, e1
```

because these constitute the complete error support needed to finalize the first detector constraint `d0`.

The remaining estimates are provisional because future detector data can still affect them.

This is the essential streaming-decoder rule:

```text
decode a larger window
        ↓
commit only the oldest causally complete region
        ↓
retain look-ahead for the rest
```

## 7. Second window and detector-offset update

After committing `e0,e1`, window 2 covers

```text
(d1, d2, d3)
```

and uses

```text
H_win2 =
[ H0   H1                 ]
[ H2   H0   H1            ]
[      H2   H0   H1       ]
```

with

```text
p_win2 = (p0, p1, p0, p1, p0, p1).
```

The original block-row constraint is

```math
H_2 e_1 + H_0 e_2 + H_1 e_3 = d_1.
```

Because `e1` has already been committed and its column is no longer inside the active matrix, move its known contribution to the detector side:

```math
d'_1 = d_1 - H_2 \hat e_1.
```

Over GF(2), subtraction is XOR:

```math
d'_1 = d_1 \oplus H_2 \hat e_1.
```

The active decode is therefore performed against

```text
(d1', d2, d3)
```

and then commits

```text
e2, e3.
```

The same terminal-`H1` duplicate-column merge is performed for this non-final window.

## 8. Third and final windows

Window 3 reuses the same merged interior structure as window 2.

Its first detector is updated using the previously committed error:

```math
d'_2 = d_2 \oplus H_2 \hat e_3.
```

It commits

```text
e4, e5.
```

The final window uses the true terminal boundary block:

```text
H_win4 =
[ H0   H1            ]
[ H2   H0   H1       ]
[      H2   H0''     ]
```

with

```text
p_win4 = (p0, p1, p0, p1, p0'').
```

Its first detector is

```math
d'_3 = d_3 \oplus H_2 \hat e_5.
```

Because `H0''` is the actual terminal block from the original global matrix, the paper's example does not apply the artificial-window `H1` merge here. The final window commits all remaining error blocks.

## 9. Implementation skeleton

Architecture-neutral pseudocode extracted from the example:

```text
detectors = temporal_difference(raw_syndromes)

for each window:
    H_active, p_active = choose_first_middle_or_last_window_structure()

    if prior committed errors touch the first detector row:
        d_active[0] ^= contribution_of_committed_errors

    if this is not the true terminal window:
        H_active, p_active = merge_duplicate_terminal_columns(H_active, p_active)

    e_hat = inner_decode(H_active, p_active, d_active)

    if terminal_window:
        commit(all_remaining(e_hat))
    else:
        commit(oldest_causally_complete_region(e_hat))
```

## 10. What to generalize and what not to

Generalizable:

- transform repeated syndrome data into temporally local detector events when the circuit admits it;
- exploit sparse spacetime structure;
- use look-ahead but commit only a causally complete prefix;
- remove already-committed variables and push their known parity contribution into the next active syndrome;
- detect active-window column degeneracies created by truncation;
- account for initial and terminal temporal boundaries explicitly.

Walking-Cat-specific until proved otherwise:

- the exact `H0/H1/H2` block contents;
- the four fault classes producing exactly this staircase;
- the `H0'` and `H0''` boundary forms;
- decoder configuration values;
- any claim that changing logical operations requires only changing priors.

Source:

https://arxiv.org/pdf/2604.19481 — Sec. XVII.B–E, Eqs. (42)–(44), Proposition 5, and the illustrative `(3,1)` example.
