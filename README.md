# V8 — Hardware-Attested AI Agent Runtime

[![Verify public showcase](https://github.com/vladislavnaidenkopro-code/hardware-attested-ai-agent-runtime/actions/workflows/verify.yml/badge.svg)](https://github.com/vladislavnaidenkopro-code/hardware-attested-ai-agent-runtime/actions/workflows/verify.yml)

Public technical showcase of a security architecture for high-trust AI-agent execution using confidential computing, measurement-bound secret access, fail-closed trust decisions, and tamper-evident audit evidence.

> **Status:** V8.0 is the frozen verified baseline represented by this showcase. V8.1 productization work continues privately and is not presented here as released functionality.

## Why this exists

Autonomous AI agents can call tools, move data and trigger external effects. For sensitive operations, application logs and text-only guardrails are not sufficient evidence of where secret-bearing code executed or which measured workload was permitted to use a key.

V8 explores a stronger trust model: bind sensitive secret access to an attested runtime measurement and preserve public-safe cryptographic commitments to the resulting evidence.

## Where the AI-agent boundary starts

The V8.0 proof is intentionally narrow: it verifies the confidential execution and secret-release substrate for a sensitive agent operation. It does **not** claim to prove the correctness of model reasoning, prompts, planning, or every higher-level tool policy.

The intended control flow is:

```text
AI agent / requested effect
        |
        v
authorization / policy boundary
        |
        v
attested confidential runtime
        |
        v
measurement-bound secret access
        |
        v
sensitive action + evidence
```

Higher-level agent governance is a separate layer. See [`docs/AI_AGENT_SECURITY_BOUNDARY.md`](docs/AI_AGENT_SECURITY_BOUNDARY.md).

## Verified V8.0 baseline

The private verification run established the following properties for the frozen V8.0 baseline:

- measured AWS Nitro Enclave execution;
- measurement-bound AWS KMS authorization;
- negative and positive attestation paths;
- enclave-only plaintext handling in the verified flow;
- provider-side CloudTrail attestation evidence;
- signed CloudTrail digest-chain validation;
- exact membership of the target event in a verified audit log;
- clean secret-print scan for the exported evidence set;
- release preflight and regression validation.

Public commitments are retained in [`evidence/HASH_COMMITMENTS.json`](evidence/HASH_COMMITMENTS.json).

## Architecture

```mermaid
flowchart LR
    A[AI Agent / Trusted Operation] --> B[Governed Runtime Boundary]
    B --> C[AWS Nitro Enclave]
    C -- signed attestation --> D[AWS KMS]
    D -- measurement-bound decrypt --> C
    C --> E[Hash-only Evidence]
    D --> F[CloudTrail Audit Events]
    F --> G[Signed Digest-Chain Validation]
    E --> H[Public-safe Commitments]
    G --> H
```

The architecture is designed around **fail-closed authorization**, **measurement-bound trust**, **secret minimization**, and **evidence preservation**.

## Attestation trust model

For AWS Nitro Enclaves, the attestation root of trust is the **AWS Nitro system / Nitro Hypervisor** and attestation documents are signed under the **AWS Nitro Attestation PKI**. "Hardware-attested" in this repository refers to that AWS Nitro attestation model; it is not a claim of a CPU-vendor root of trust such as AMD SEV-SNP or Intel TDX.

See [`docs/ATTESTATION_TRUST.md`](docs/ATTESTATION_TRUST.md).

## Public verifier

This repository includes a dependency-free verifier for the public commitment manifest:

```bash
python tools/verify_public_manifest.py evidence/HASH_COMMITMENTS.json
python -m unittest discover -s tests -v
```

The verifier checks schema shape, SHA-256 formatting, expected commit-SHA formatting, duplicate commitment values, and the required non-claim set.

**Important:** this is a commitment-manifest validator, not an independent verifier of Nitro attestation, KMS policy evaluation, or CloudTrail contents. The published hashes are cryptographic commitments to retained private evidence; by themselves they do not prove the underlying security event. They become useful when a disclosed artifact is later checked against the previously published commitment.

## Public-safe policy pattern

A generic, placeholder-only example showing the AWS KMS recipient-attestation condition pattern is included in [`docs/KMS_ATTESTATION_POLICY_PATTERN.md`](docs/KMS_ATTESTATION_POLICY_PATTERN.md). It contains no account identifiers, resource identifiers, or real PCR values.

## What is intentionally not here

This repository does not include:

- private implementation source code;
- AWS account IDs, ARNs, IP addresses or credentials;
- raw attestation documents or raw CloudTrail logs;
- internal IAM/KMS policy documents;
- recovery archives, deployment secrets or customer information;
- private V8.1 implementation details.

## Documentation

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — trust boundary and execution sequence
- [`docs/AI_AGENT_SECURITY_BOUNDARY.md`](docs/AI_AGENT_SECURITY_BOUNDARY.md) — what is AI-agent-specific versus confidential-computing substrate
- [`docs/ATTESTATION_TRUST.md`](docs/ATTESTATION_TRUST.md) — AWS Nitro root of trust and standards context
- [`docs/KMS_ATTESTATION_POLICY_PATTERN.md`](docs/KMS_ATTESTATION_POLICY_PATTERN.md) — sanitized attestation-bound KMS policy pattern
- [`docs/VERIFIED_STATUS.md`](docs/VERIFIED_STATUS.md) — what is verified versus in development
- [`docs/THREAT_MODEL.md`](docs/THREAT_MODEL.md) — threat assumptions and control boundaries
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — public-safe development direction
- [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) — what a reviewer can reproduce from this repository
- [`SECURITY.md`](SECURITY.md) — disclosure and security policy

## Public showcase release

The curated public snapshot is published as [`showcase-v8.0-20260928`](https://github.com/vladislavnaidenkopro-code/hardware-attested-ai-agent-runtime/releases/tag/showcase-v8.0-20260928). This tag identifies the public showcase, not the private V8.0 implementation repository. `main` may contain later documentation/CI hardening while the tagged V8.0 public snapshot remains unchanged.

## Non-claims

This showcase does not claim production readiness, regulatory certification, an SLA, universal attack prevention, customer security outcomes, or exactly-once external delivery semantics.

## License

Portfolio and evaluation use only. See [`LICENSE`](LICENSE).
