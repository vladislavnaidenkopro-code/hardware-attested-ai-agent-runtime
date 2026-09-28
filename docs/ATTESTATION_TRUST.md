# AWS Nitro Attestation Trust Model

## Root of trust

AWS documents the Nitro Enclaves attestation root of trust as residing in the **AWS Nitro system**. The Nitro Hypervisor produces attestation documents containing enclave measurements and related claims.

Those attestation documents are encoded with CBOR / COSE and are signed under the **AWS Nitro Attestation PKI**, whose certificate authority can be used by a verifier to validate the chain and signature.

This public showcase therefore treats AWS Nitro and its attestation PKI as a trusted provider dependency.

## What "hardware-attested" means here

In this repository, **hardware-attested** means that an authorization decision is bound to measurements carried in an AWS Nitro Enclaves attestation document and evaluated through the AWS Nitro/KMS attestation mechanism.

It does not mean:

- V8 replaces AWS's trust root;
- V8 independently proves the physical CPU or cloud operator;
- V8 provides the same trust model as AMD SEV-SNP, Intel TDX, TPM-based attestation, or another TEE;
- hardware attestation proves application correctness.

## KMS binding

AWS KMS exposes recipient-attestation condition keys such as:

- `kms:RecipientAttestation:ImageSha384`
- `kms:RecipientAttestation:PCR0` (and other PCR-specific keys)

When used in a KMS key or IAM policy, these conditions can restrict supported cryptographic operations to a request that carries a signed Nitro Enclave attestation document with matching measurements.

A sanitized pattern is provided in [`KMS_ATTESTATION_POLICY_PATTERN.md`](KMS_ATTESTATION_POLICY_PATTERN.md).

## Standards context

The following standards are useful conceptual references for remote attestation:

- **RFC 9334 — Remote ATtestation procedureS (RATS) Architecture**
- **RFC 9711 — Entity Attestation Token (EAT)**

The Nitro attestation document is AWS-defined. This repository does **not** claim that a Nitro attestation document is an EAT or that V8 implements an RFC 9711 profile. RATS/EAT are referenced to make the roles and terminology of attestation easier to compare with broader industry work.

## Primary references

- AWS Nitro Enclaves — *Verifying the root of trust*: https://docs.aws.amazon.com/enclaves/latest/user/verify-root.html
- AWS KMS — *Condition keys for Nitro Enclaves*: https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclave.html
- RFC 9334: https://www.rfc-editor.org/rfc/rfc9334
- RFC 9711: https://www.rfc-editor.org/rfc/rfc9711
