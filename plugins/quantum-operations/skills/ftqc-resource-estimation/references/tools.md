# Tool references

Use [implementation.md](implementation.md) for executable estimator calls, canonical resource records, and reconciliation rules.

- Microsoft Quantum Resource Estimator / QDK QRE:
  https://learn.microsoft.com/azure/quantum/overview-resources-estimator
  - Current Python package path is documented under `qdk.qre`.
  - Install from current docs, e.g. `pip install --upgrade "qdk[qre]"`, then pin the tested environment.
- Qualtran:
  - source: https://github.com/quantumlib/Qualtran
  - docs: https://qualtran.readthedocs.io/
  - use for compositional logical/FT resource costing where its decomposition model matches the workload.
- TQEC: https://tqec.github.io/tqec/
- MQT QECC: https://mqt.readthedocs.io/projects/qecc/en/latest/

Reconcile each estimator result with this repository's decoder queues, control-plane latency, factory buffering, and whole-machine scheduling through the runtime skills.
