---
name: transversal-teleportation
description: Compile fault-tolerant circuits around transversal logical gates, logical teleportation, fresh-block reset/reuse, frame tracking, correlated decoding, and code-specific permutation gates.
---

# Transversal Teleportation

Use this workflow when the selected code/hardware supports transversal logical operations or logical teleportation between encoded blocks.

Treat teleportation as both a logical-operation primitive and an entropy-removal boundary. The compiler may move logical information onto a fresh encoded block while leaving physical errors, leakage, loss, and motional entropy on the old block, which is then measured, reset/re-cooled/reinitialized, and reused.

Optimize the joint system rather than gate count alone: peak encoded blocks/physical carriers, fresh-block pool size, transversal 2Q layers, permutation/re-indexing operations, syndrome/QEC rounds, logical failure budget, decoder load, feed-forward latency, movement, non-Clifford resources, reset/reuse cycle time, and wall-clock runtime.

## Compiler contract

Represent each logical operation or block transition with:

~~~text
code
code_parameters
block_ids[]
logical_operation
transversal_protocol?
permutation_protocol?
teleportable
requires_fresh_block
measurement_basis[]
decoder_window
frame_byproduct
resettable_after
entropy/error increment
physical_gate_layer
movement/routing requirement
~~~

A candidate is transversal only when the selected code has a documented physical transversal action implementing the required logical map. A gate network becomes a block permutation/re-indexing only when the code automorphism and induced logical map are verified.

## Required optimization passes

1. Identify maximal regions supported by transversal logical gates.
2. Detect code automorphisms/permutations that realize required logical Clifford maps without entangling gates.
3. Group compatible operations into transversal layers.
4. Place logical-teleportation boundaries where they simultaneously perform useful logic, bound physical-error propagation, and release old blocks for reset/reuse.
5. Track Pauli/Clifford byproducts in software when the protocol permits.
6. Build correlated-decoding windows across transversal layers when the chosen decoder supports this.
7. Schedule fresh encoded blocks, measurement, reset/re-cooling, and reuse explicitly.
8. Preserve the Pareto frontier over physical width, QEC cycles, decoder load, movement, non-Clifford resources, and runtime.

## Implementation gate

Load references/implementation.md, references/research.md, the smallest matching example under references/examples/, and the runtime-control and runtime-scheduling implementation references. Also load the selected code-family workflow.

Never infer transversal or permutation gates from code parameters alone. Verify every rewrite at the logical-map level and every reset/reuse boundary against the measurement/byproduct protocol.