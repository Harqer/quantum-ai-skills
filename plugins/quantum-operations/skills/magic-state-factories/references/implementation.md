# Magic-state factories: implementation reference

Distillation, catalysis, and cultivation are different protocols. Model them as different producer types with different inputs, postselection, failure modes, and resource models.

## Common producer interface

Every magic-state producer must expose:

~~~text
resource_type          # T, CCZ, rotation state, catalyst, ...
input_resources[]
output_resources[]
acceptance_probability
output_error_model
cycles_per_attempt
physical/logical footprint
measurement/feedforward dependencies
routing ports
restart/retry semantics
~~~

## 15-to-1 T-state distillation

Under the ideal-Clifford approximation, the standard 15-to-1 Reed-Muller protocol consumes 15 noisy T-type inputs and, conditioned on passing checks, outputs one improved state.

Leading-order output error:

~~~text
p_out ~= 35 * p_in^3
~~~

This approximation assumes the distillation Clifford layer itself is sufficiently reliable. Add logical-circuit failure separately in a physical factory model.

A leading-order acceptance approximation is:

~~~text
p_accept ~= 1 - 15*p_in + O(p_in^2)
~~~

Use these approximations inside their stated low-error regime and switch to the exact protocol/error model when the operating point falls outside that regime.

## Current executable protocol example: CUDA-Q Logical preview

Current CUDA-Q Logical documentation publishes a 15-to-1 protocol definition:

~~~python
import cudaq.logical as cql

@cql.protocol(implements=cql.logical.produce(cql.logical.T_STATE))
def distill_15to1() -> cql.types.resource[cql.logical.T_STATE]:
    raw_states = cql.request_many(
        cql.logical.RAW_T_STATE,
        count=15,
    )
    output = cql.prepare_plus(
        cql.allocate_patch(
            cql.codes.BareQubit,
            region="t_state_factory",
        )
    )

    checks = []
    for state in raw_states[:4]:
        output, check = cql.unpack_resource(
            state,
            like=output,
            encoding=cql.codes.BareQubit,
        )
        checks.append(check)

    rows = [*checks, output]

    for state, rotation in zip(
        raw_states[4:],
        cql.protocols.FIFTEEN_TO_ONE_ROTATION_STEPS,
    ):
        rows = list(rotation(*rows, state))

    rows[4] = cql.protocols.bare_s(rows[4])

    for check in rows[:4]:
        cql.postselect(
            cql.protocols.bare_measure_x(check),
            expected=False,
        )

    return cql.pack_resource(
        rows[4],
        kind=cql.logical.T_STATE,
    )
~~~

Static estimate:

~~~python
resources = cql.estimate(
    distill_15to1,
    tier=cql.estimate.Tier.STATIC,
)

assert resources.operation_counts["resource_request"] == 15
assert resources.operation_counts["resource_rotate_product"] == 11
assert resources.operation_counts["selection"] == 4
assert resources.operation_counts["pack_resource"] == 1
~~~

This API is a 2026 preview surface. Pin CUDA-Q and re-check documentation before using it as production code.

Source:
https://nvidia.github.io/cuda-quantum/latest/preview/logical/use-cases/examples/distillation.html

## Multi-level distillation

For each level, propagate accepted-output rate, rejection probability, and retry demand recursively through the factory stack.

For demanded output rate R_out:

~~~text
attempt_rate >= R_out / p_accept
raw_input_rate >= 15 * attempt_rate
~~~

At multiple levels, propagate rate and acceptance recursively.

## Buffer simulation

At every schedule tick/cycle:

~~~python
buffer += accepted_factory_outputs
consume = min(buffer, requested_magic_states)
buffer -= consume
stall = requested_magic_states - consume
~~~

Use a stochastic or conservative acceptance model so the scheduler represents unsuccessful attempts and the resulting buffer demand.

## Cultivation

Magic-state cultivation is **not 15-to-1 distillation**. It grows/protects a state using a code-based protocol and postselection/expansion stages.

When cultivation is selected:
- use the cultivation paper/reproduction circuits for that protocol;
- model its acceptance, expansion, and output infidelity separately;
- use the cultivation-specific acceptance and output-error model from the selected protocol.

Primary cultivation reference:
https://arxiv.org/abs/2409.17595

## Factory selection

For each producer candidate calculate:
- output error versus required per-state budget;
- mean and high-confidence throughput;
- peak footprint;
- routing distance to consumers;
- buffer requirement;
- restart cost.

Feed the producer model to ftqc-runtime-scheduling.

## Verification

- reproduce static resource counts from the protocol definition;
- Monte Carlo or exact-enumerate acceptance/error behavior where supported;
- ensure every postselection condition is represented;
- verify injection byproducts through fault-tolerant-runtime-control;
- distinguish producer logical failure from input-state infidelity.
