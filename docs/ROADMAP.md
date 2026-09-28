# Public-Safe Roadmap

This roadmap communicates direction, not release commitments.

## V8.1 — productization gates

1. **Confidential runtime state recovery**
   - preserve consumed lease/replay state;
   - preserve configuration and trust history;
   - persist hash-only resolver evidence;
   - never persist secret plaintext.

2. **Operator evidence/status surface**
   - expose health, evidence freshness and trust state without leaking sensitive data.

3. **Deployment packaging**
   - repeatable deployment, rollback and proof collection;
   - provider/secret-manager abstraction;
   - explicit fail-closed configuration boundaries.

4. **Enterprise identity**
   - controlled integration with enterprise identity and authorization systems.

5. **Exposure intelligence normalization**
   - versioned schemas for customer-owned cloud/CI/Kubernetes exports;
   - canonical asset-alias reconciliation;
   - evidence lifecycle: SIGNAL → UNCONFIRMED → CONFIRMED → REMEDIATED / ACCEPTED_RISK / FALSE_POSITIVE.

## Later research candidates

These are evaluation items, not current capabilities:

- Agentic Software Bill of Materials (A-SBOM) and security-drift control;
- deterministic forensic replay for agent incidents;
- short-lived post-attestation session credentials;
- threshold/quorum authorization for selected critical effects;
- activation-level controls for compatible self-hosted models.

Research candidates are promoted only after architectural fit, threat-model value and verification cost are demonstrated.
