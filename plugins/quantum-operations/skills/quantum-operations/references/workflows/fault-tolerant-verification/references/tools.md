# Tool references

Use [implementation.md](implementation.md) for executable verification workflows and acceptance rules. This file is only a source/version index.

- MQT QCEC: https://mqt.readthedocs.io/projects/qcec/en/stable/
  - Verify the installed QCEC version before copying API syntax.
  - Use exact equivalence by default; approximate or partial/dynamic semantics require the corresponding documented mode.
- Stim: https://github.com/quantumlib/Stim
  - Use for detector/observable and stabilizer/QEC checks, not as a substitute for full non-Clifford equivalence.
- MQT QECC: https://mqt.readthedocs.io/projects/qecc/en/latest/
  - Use when its code/gadget/logical-compilation model matches the target.

Declare verification successful after the invariants in implementation.md pass under the selected tool and equivalence relation.
