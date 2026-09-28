# Reproducibility

The public repository is intentionally a verification-oriented showcase rather than the private implementation.

## Reproducible here

A reviewer can:

1. inspect the public commitment manifest;
2. run the dependency-free manifest validator;
3. run the unit tests;
4. inspect the documented trust model, evidence boundary and non-claims;
5. inspect a sanitized AWS KMS recipient-attestation policy pattern;
6. independently verify that no private cloud identifiers or raw provider evidence are required by the public validator.

## What the manifest validator proves

`tools/verify_public_manifest.py` validates the **structure and internal consistency of the public commitment manifest**. It checks expected digest formats, commit-SHA formatting, duplicate commitment values and required non-claims.

It does **not** independently verify:

- an AWS Nitro attestation document;
- a certificate chain to the AWS Nitro attestation root;
- actual KMS policy evaluation;
- the contents of the retained CloudTrail evidence;
- private implementation behavior.

## Commitment semantics

The values in `evidence/HASH_COMMITMENTS.json` are cryptographic commitments to retained private release evidence.

A hash commitment is useful for later disclosure: if a private artifact is selectively disclosed to a reviewer, the reviewer can hash that artifact and compare it with the commitment that was already published. The hash alone does not establish that the private artifact had a particular security meaning or that a claimed event occurred.

## Not reproducible from this repository alone

The original hardware-backed proof cannot be reproduced from this public repository because the private implementation, infrastructure configuration, raw attestation/CloudTrail evidence and recovery material are deliberately excluded.

That limitation is intentional. The public repository is designed to make claims precise and commitments stable without publishing sensitive infrastructure details.
