# Example 5: 25-level 137Ba+ preparation and readout

The 2026 25-level experiment encodes states across S_1/2 and D_5/2.

Single-shot measurement procedure:

1. Test fluorescence for the encoded S_1/2 state.
2. If dark, sequentially de-shelve one D_5/2 basis state to S_1/2.
3. Test fluorescence.
4. Continue through the candidate states.
5. Assign the first bright outcome to the corresponding qudit basis state.
6. Treat no-bright outcomes as preparation/readout failure or leakage according to the experiment protocol.

The reported average SPAM fidelity across all 25 levels was 99.51 +/- 0.05%.

For a production candidate retain the full confusion matrix:

~~~text
P(measured=j | prepared=i)
~~~

rather than only the average SPAM fidelity. The compiler should penalize dimensions whose added levels have poor distinguishability or coherence.
