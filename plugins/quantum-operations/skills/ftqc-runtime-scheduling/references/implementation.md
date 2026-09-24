# FTQC runtime scheduling: implementation reference

The scheduler is a dependency/resource scheduler with additional streaming queues for decoders and magic-state producers.

## Event schema

Represent every scheduled operation as:

~~~text
id
kind
duration
predecessors[]
resources[]            # exclusive or capacity-limited
logical_blocks[]
magic_state_demand{}
decoder_dependency?
measurement_output?
retry_policy?
~~~

Resources can include:

~~~text
logical patch/block
routing lane
factory output port
decoder worker
measurement hardware
classical feed-forward unit
~~~

## Deterministic list scheduling

For a DAG with exclusive resources:

~~~python
finish = {}
resource_free = {}

for event in topological_order:
    pred_ready = max(
        (finish[p] for p in event.predecessors),
        default=0,
    )
    resource_ready = max(
        (resource_free.get(r, 0) for r in event.resources),
        default=0,
    )

    start = max(pred_ready, resource_ready)
    end = start + event.duration

    finish[event.id] = end
    for r in event.resources:
        resource_free[r] = end
~~~

For capacity > 1, represent each resource class by a min-heap of worker-available times.

This baseline does not yet model factory/decoder stochasticity; add those as queues below.

## Decoder queue

For c decoder workers, given arrival times and service times:

~~~python
import heapq

def decode_queue(arrivals, services, workers):
    free = [0.0] * workers
    heapq.heapify(free)
    out = []

    for arrival, service in zip(arrivals, services):
        worker_free = heapq.heappop(free)
        start = max(arrival, worker_free)
        finish = start + service
        heapq.heappush(free, finish)

        out.append({
            "arrival": arrival,
            "start": start,
            "finish": finish,
            "queue_delay": start - arrival,
        })
    return out
~~~

Necessary steady-state condition:

~~~text
arrival_rate * mean_service_time < worker_count
~~~

This is not sufficient for deadline correctness because heavy tails and bursts can still violate p99/p99.9 deadlines. Simulate/replay the measured service-time distribution.

## Decoder-induced stall

If logical event G cannot start until decoder result D:

~~~text
stall_D = max(0, decoder_finish(D) - baseline_start(G))
~~~

The schedule must shift G and all dependent events, then re-evaluate downstream resource contention.

Do not add decoder delay as one global constant.

## Magic-state buffer

For discrete factory output and demand events:

~~~python
buffer = 0

for event in time_order:
    if event.kind == "factory_success":
        buffer += event.count

    elif event.kind == "magic_request":
        if buffer >= event.count:
            buffer -= event.count
            event.stall = 0
        else:
            missing = event.count - buffer
            event waits until enough accepted output arrives
            buffer = 0
~~~

If the producer has acceptance probability < 1, model attempts and accepted outputs separately.

## Factory throughput lower bound

For requested steady output rate R and attempt acceptance p_acc:

~~~text
attempt_rate >= R / p_acc
~~~

For a factory producing b states per successful attempt:

~~~text
attempt_rate >= R / (b * p_acc)
~~~

Also satisfy burst-buffer requirements; average rate alone is not enough.

## Stretch

For schedules where classical delay inserts extra QEC cycles:

~~~text
stretch = extra_cycles / baseline_cycles
~~~

Report both absolute added cycles and the ratio.

## Full scheduling loop

~~~text
1. schedule quantum/QEC baseline
2. generate syndrome arrivals
3. replay decoder queues
4. insert decoder/feed-forward stalls
5. generate magic-state demand timeline
6. replay factory outputs/buffers
7. insert factory starvation stalls
8. recompute routing/resource contention
9. repeat until no event time changes
~~~

If retries/postselection are stochastic, run many sampled schedules or compute a conservative quantile schedule.

## Verification

- DAG remains acyclic;
- every predecessor ends before dependent start;
- no exclusive-resource overlaps;
- buffer never becomes negative;
- decoder job is never consumed before finish;
- all retries/postselection paths are represented;
- final wall-clock runtime is reproducible from event log;
- compare against a no-latency/no-starvation baseline to isolate extension sources.
