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

## Root of trust

The V8.0 proof uses **AWS Nitro Enclaves**. In this model, the attestation root of trust resides in the **AWS Nitro system**, with the Nitro Hypervisor producing enclave measurements and attestation documents. Attestation documents are signed under the **AWS Nitro Attestation PKI**.

This means V8.0 relies on AWS Nitro's attestation mechanisms and AWS's published attestation PKI. "Hardware-attested" here does not mean that V8 independently establishes a CPU-vendor trust root, nor does it claim equivalence to AMD SEV-SNP, Intel TDX, or another confidential-computing technology with a different trust model.

## Trust assumptions

The verified V8.0 proof relies on:

- the security properties of the relevant AWS Nitro Enclave mechanisms;
- AWS KMS recipient-attestation policy evaluation;
- AWS CloudTrail integrity mechanisms used by the verified evidence path;
- correctness of the measured workload;
- correctness of the verification and evidence-processing logic;
- continued protection of private evidence and release material retained outside this public repository.

## Out of scope / not eliminated

Hardware attestation is not a universal security guarantee. It does not by itself eliminate:

- application logic vulnerabilities;
- model or prompt errors;
- malicious or unsafe actions that a valid policy explicitly authorizes;
- compromised upstream dependencies or build systems;
- incorrect policy authoring;
- stolen credentials outside the protected path;
- control-plane misconfiguration;
- side-channel classes not covered by the verified proof;
- compromise of the attestation provider or its trust infrastructure.

## Evidence boundary

The public repository does not expose the raw attestation document, private KMS/IAM policy, raw CloudTrail files, resource identifiers, or private source. Public hashes are commitments to retained private evidence, not standalone proof of the underlying event.

## Design principle

A failed, missing or mismatched trust proof must not silently increase authority. Sensitive paths are designed to fail closed.
