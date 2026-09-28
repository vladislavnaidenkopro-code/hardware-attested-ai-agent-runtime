# Threat Model

## Assets

The design protects or accounts for:

- secret material used by sensitive agent operations;
- runtime identity and measured workload state;
- policy and trust configuration;
- audit evidence and release provenance;
- replay/lease state used by higher-level execution controls.

## Relevant threat classes

The architecture is intended to reduce exposure to selected classes of risk, including:

- secret access from an unapproved workload;
- host-level attempts to obtain plaintext that should remain inside the confidential boundary;
- configuration or trust drift that is not reflected in evidence;
- audit-log tampering or selective event removal;
- silent substitution of an expected runtime/provider identity.

## Trust assumptions

The verified V8.0 proof relies on the security properties of the relevant AWS Nitro Enclave, KMS and CloudTrail mechanisms, plus the correctness of the measured workload and its verification logic.

## Out of scope / not eliminated

Hardware attestation is not a universal security guarantee. It does not by itself eliminate:

- application logic vulnerabilities;
- compromised upstream dependencies or build systems;
- incorrect policy authoring;
- stolen credentials outside the protected path;
- control-plane misconfiguration;
- side-channel classes not covered by the verified proof;
- unsafe actions explicitly authorized by a valid policy.

## Design principle

A failed, missing or mismatched trust proof must not silently increase authority. Sensitive paths are designed to fail closed.
