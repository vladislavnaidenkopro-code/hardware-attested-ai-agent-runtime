# Architecture

## Trust objective

A sensitive agent operation should not receive secret material merely because it runs on a named server. In the verified V8.0 proof, secret access is conditioned on an expected confidential-runtime measurement.

## AI-agent control boundary

The AI-specific security objective is not "put the whole model in an enclave." The V8.0 proof focuses on the **sensitive-effect boundary**: an AI-assisted workflow may request an operation, but secret-bearing execution is routed through an authorization boundary and then through an attested confidential runtime.

```text
AI agent / workflow
        |
        | request to perform a sensitive effect
        v
authorization / policy boundary
        |
        | only an approved request proceeds
        v
attested confidential runtime
        |
        | measurement-bound secret release
        v
external action / cryptographic operation
        |
        v
evidence and audit trail
```

The public V8.0 materials do not claim that model reasoning, planning, prompts, or every tool call are hardware-attested.

## Verified sequence

```text
1. A governed operation reaches the confidential-computing path.
2. The measured enclave workload presents attestation evidence.
3. The key service evaluates the expected measurement condition.
4. An invalid path is denied; the expected attested path is accepted.
5. Plaintext is handled inside the enclave boundary in the verified flow.
6. Provider-side audit evidence records the relevant operation metadata.
7. Signed CloudTrail digest-chain validation establishes log integrity.
8. Public output exposes commitments, not raw evidence or secret material.
```

## Attestation trust

For AWS Nitro Enclaves, the root of trust is the AWS Nitro system / Nitro Hypervisor and the attestation document is signed under the AWS Nitro Attestation PKI. V8 relies on that provider trust model; it does not replace or independently re-establish it.

## Control principles

- fail closed on missing or mismatched trust evidence;
- keep plaintext out of the public evidence path;
- bind release claims to immutable identifiers;
- make trust/configuration changes observable rather than silently mutable;
- separate private source of truth from irreversible public disclosure.

## Public/private boundary

This repository documents the architecture and preserves hash-only commitments. Private implementation code, infrastructure policy, raw attestation/provider evidence and recovery material remain outside the public repository.
