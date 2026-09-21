---
name: fire-opal-adjunct
description: Use Q-CTRL Fire Opal only as an optional present-day hardware execution/error-suppression adjunct. Do not use it as a substitute for FTQC QEC, logical synthesis, or resource estimation.
---

# Fire Opal Adjunct

Fire Opal is useful for supported present-day hardware workflows, but it is **not a fault-tolerance layer**.

- Use it only when executing on a currently supported real-hardware path and when error suppression/mitigation is relevant.
- Do not use Fire Opal to claim that an over-wide circuit fits a QPU, that QEC is unnecessary, or that an FTQC physical resource estimate has improved.
- Keep Fire Opal result quality metrics separate from logical/FTQC metrics.
- Verify current provider/backend support from Q-CTRL documentation at use time.
- Prefer its validation path before metered execution when available.

This skill exists because practical development may span pre-FT and FT systems; it should not activate for purely fault-tolerant resource analysis.
