# Lattice surgery: executable TQEC reference

API state checked against current TQEC documentation in September 2026.

TQEC is rapidly evolving and its documentation warns that backwards compatibility is not guaranteed. Pin the version/commit used for production examples.

## End-to-end logical CNOT example

TQEC provides a gallery CNOT that can be compiled into a detector-annotated Stim circuit.

~~~python
from tqec.gallery.cnot import cnot
from tqec import Basis

block_graph = cnot(Basis.Z)
~~~

A BlockGraph is the topological/logical computation representation.

## Find logical observables

~~~python
correlation_surfaces = block_graph.find_correlation_surfaces()

if len(correlation_surfaces) == 0:
    raise RuntimeError("No logical observable/correlation surface found")
~~~

Select the intended logical observable by meaning and record that mapping explicitly in production.

## Compile the block graph

~~~python
from tqec import compile_block_graph

compiled = compile_block_graph(
    block_graph,
    observables=[correlation_surfaces[1]],
)
~~~

The observable index above mirrors the TQEC quick-start CNOT example; for another computation select observables by their intended logical meaning.

## Generate a physical Stim circuit

~~~python
from tqec import NoiseModel

stim_circuit = compiled.generate_stim_circuit(
    k=2,
    noise_model=NoiseModel.uniform_depolarizing(0.001),
)
~~~

TQEC adds detector and observable annotations during circuit generation.

The parameter k controls the scale/code-distance-related construction in this API. Record it with the generated circuit.

## Simulate a parameter sweep

~~~python
import numpy as np
from tqec import NoiseModel
from tqec.simulation.simulation import start_simulation_using_sinter

stats = start_simulation_using_sinter(
    block_graph,
    ks=range(1, 4),
    ps=list(np.logspace(-4, -1, 10)),
    noise_model_factory=NoiseModel.uniform_depolarizing,
    manhattan_radius=2,
    observables=[correlation_surfaces[1]],
)
~~~

Consume the returned iterator and persist the exact TQEC/Stim/Sinter versions.

## What a compiler integration must track

For every logical patch/operation:

~~~text
patch identity
logical basis/orientation
space coordinates
time coordinate / code cycles
merge/split or measurement operation
required ancilla region
correlation surface / logical observable
factory/routing interface
~~~

A geometric rewrite is valid only if correlation surfaces/logical observables remain correct.

## Pauli-product semantics

A lattice-surgery compiler should lower logical operations into supported joint measurements/patch operations such as logical XX/ZZ products where the chosen architecture permits them.

Implement CNOT from a reviewed protocol or TQEC block graph and verify the resulting correlation surfaces before accepting the geometry.

## Verification

For every optimized geometry:
1. compile both baseline and candidate;
2. confirm the intended logical observables/correlation surfaces;
3. generate detector-annotated Stim circuits;
4. simulate logical failure over the same noise model and scale parameters;
5. compare physical qubit footprint and spacetime volume;
6. reject a geometry optimization that changes the logical transformation or detector correctness.

Primary tool reference:
https://tqec.github.io/tqec/user_guide/quick_start.html
