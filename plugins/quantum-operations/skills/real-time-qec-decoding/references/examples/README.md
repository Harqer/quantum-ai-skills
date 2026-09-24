# Real-time QEC decoding examples

These examples turn the research notes into implementation-oriented references. They are deliberately split by abstraction level:

1. [DEM to Tanner graph](dem-to-tanner.md) — a minimal detector-error-model example with the explicit parity-check matrix and syndrome equation.
2. [Walking Cat sliding window](walking-cat-sliding-window.md) — the exact six-SEC, `(w,c)=(3,1)` construction from the Walking Cat architecture, including window matrices, duplicate-column merging, commit semantics, and detector updates.
3. [IonQ BeamSearchDecoder code path](beam-search-code-path.md) — how the published implementation converts a Stim DEM into a sparse check matrix and priors and then drives the beam-search decoder.

## Scope rule

Use these examples to understand the mechanics. Do not copy architecture-specific assumptions into another QEC stack unless their prerequisites hold.

In particular:

- the Walking Cat staircase follows from repeated syndrome-extraction cycles and the detector transform `d_i = s_i XOR s_{i-1}`;
- its boundary blocks are architecture/circuit dependent;
- duplicate-column merging is valid when columns are identical in the active parity-check problem and the corresponding error mechanisms are treated with the stated independence assumption;
- the MegaQuOp fixed-Tanner-graph/dynamic-prior optimization is specific to the detector-signature structure proved for that architecture;
- BeamSearchDecoder is one inner decoder implementation, not a mandatory choice for sliding-window decoding.

Primary sources:

- Walking Cat architecture: https://arxiv.org/abs/2604.19481
- MegaQuOp real-time decoder: https://arxiv.org/abs/2608.25027
- BeamSearchDecoder source: https://github.com/ionq-publications/BeamSearchDecoder
- Stim DEM format: https://github.com/quantumlib/Stim/blob/main/doc/file_format_dem_detector_error_model.md
