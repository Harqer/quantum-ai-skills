# QEC code strategy: implementation reference

This skill chooses an **executable code + logical-operation architecture**, not a code family name in isolation.

## Required machine model

Represent the target as:

~~~text
physical_error_model:
  one_qubit
  two_qubit
  measurement
  reset
  leakage
  bias/correlations

timing:
  one_qubit_time
  two_qubit_time
  measurement_time
  reset_time
  transport/communication_time
  syndrome_cycle_time

topology:
  graph/locality/dimensionality
  movement/teleportation capabilities

classical:
  decoder_compute
  memory
  network
  feedforward latency
~~~

Every unknown field must remain explicit rather than replaced by a vendor-default guess.

## Candidate record

For each candidate logical architecture store:

~~~text
code_family
code_parameters
logical_qubits_per_block
physical_qubits_per_block
distance
syndrome_circuit
detector_rate
logical_error_model
logical_operations:
  operation -> protocol/cycles/ancilla/measurement requirements
decoder:
  algorithm
  latency distribution
  throughput
factory interface
routing/communication model
~~~

## Selection algorithm

1. Enumerate code/logical-operation candidates compatible with target connectivity and measurement/reset behavior.
2. Generate or obtain the actual syndrome-extraction circuit.
3. Simulate/measure logical failure under the physical noise model using qec-simulation-decoding.
4. For each code parameter/distance candidate, compute workload logical-failure contribution.
5. Reject candidates exceeding the assigned error budget.
6. Reject candidates whose decoder service capacity cannot keep up with detector production.
7. Compile the workload logical operations and estimate runtime/physical footprint.
8. Keep the Pareto frontier rather than selecting by threshold or encoding rate alone.

## Distance selection from measured data

Do not hard-code a universal surface-code scaling law.

Given measured/simulated per-round logical failure estimates:

~~~text
samples = [
  (distance=d1, p_logical=p1),
  (distance=d2, p_logical=p2),
  ...
]
~~~

and an allowed logical-memory failure budget epsilon_mem across N protected rounds/locations, use a conservative union bound:

~~~text
N * p_logical(d) <= epsilon_mem
~~~

and choose the smallest distance satisfying it.

~~~python
def choose_distance(samples, n_locations, epsilon):
    valid = [
        d for d, p in samples
        if n_locations * p <= epsilon
    ]
    if not valid:
        raise ValueError("No tested distance satisfies the error budget")
    return min(valid)
~~~

If an analytical scaling law is fitted, record the source/model, fit range, uncertainty, and physical-noise regime. Do not extrapolate across threshold without evidence.

## Detector-rate calculation

From the concrete syndrome circuit determine:

~~~text
detectors_per_cycle = number of new detector outcomes produced per SEC
blocks = simultaneously active code blocks

detector_events_per_second =
    detectors_per_cycle * blocks / syndrome_cycle_time
~~~

If decoder input is compressed/partitioned, use actual transmitted bytes/events as a second throughput metric.

Pass this rate to real-time-qec-decoding.

## Logical-operation inventory

For each operation required by the workload, answer explicitly:

~~~text
logical X/Z/H/S/CNOT?
arbitrary Pauli-product measurement?
T / CCZ / arbitrary rotation?
state preparation?
logical measurement?
inter-block communication?
~~~

Then map it to one supported mechanism:
- transversal;
- lattice surgery;
- code deformation;
- teleportation;
- code switching;
- magic-state injection;
- software frame update.

If no mechanism is documented for the candidate code, the candidate does not yet have a complete logical ISA.

## Worked comparison skeleton

Do not compare:

~~~text
surface code vs qLDPC
~~~

as abstract labels.

Compare:

~~~text
Candidate A:
  rotated surface-code blocks
  lattice-surgery CNOT
  T-state injection
  MWPM decoder
  measured p_L(d)
  concrete patch/factory layout

Candidate B:
  specific BB/qLDPC block
  named transversal/measurement logical protocol
  named decoder
  measured p_L(parameters)
  concrete inter-block protocol
~~~

Only after both records are complete may physical qubits/runtime be compared.

## Acceptance checks

A selected QEC architecture must have:
- full logical operation coverage for the workload;
- code parameters and state-preparation/measurement protocol;
- circuit-level noise experiment or justified error model;
- decoder feasibility;
- runtime-control semantics;
- physical-resource estimate;
- explicit unsupported operations.

Tools:
- Stim/Sinter/PyMatching/Fusion Blossom for compatible decoding experiments;
- MQT QECC for QEC/logical-compilation workflows;
- TQEC for surface-code/topological computation construction.
