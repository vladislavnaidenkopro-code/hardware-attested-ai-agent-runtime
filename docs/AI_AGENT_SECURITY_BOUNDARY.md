# AI-Agent Security Boundary

## Why the project is an AI-agent runtime, not only a KMS/Nitro example

The confidential-computing primitive solves only one part of the problem: **where and under which measured workload a secret-bearing operation is allowed to execute**.

AI agents introduce a separate question: **which requested effects should be permitted at all?**

V8 keeps those concerns distinct.

```text
model / agent reasoning
        |
        v
requested tool or external effect
        |
        v
authorization / policy decision
        |
        v
attested execution boundary
        |
        v
measurement-bound secret access
        |
        v
external effect + audit evidence
```

## V8.0 public claim

The frozen V8.0 proof covers the attested execution / secret-release / provider-evidence portion of this chain.

It does not claim to hardware-attest:

- the language model itself;
- prompts or chain-of-thought;
- all orchestration logic;
- every tool invocation;
- the semantic correctness of an agent's decision.

## Higher-level governance

Higher-level agent controls can include scoped tool authority, replay protection, idempotency, approval boundaries, budgets and evidence lifecycle management. Those controls belong to the broader productization layer and are not presented by the V8.0 public showcase as released functionality.

This separation is deliberate: hardware attestation should not be used as a marketing substitute for application-level authorization.
