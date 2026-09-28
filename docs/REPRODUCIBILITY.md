# Reproducibility

The public repository is intentionally a verification-oriented showcase rather than the private implementation.

## Reproducible here

A reviewer can:

1. inspect the public commitment manifest;
2. run the dependency-free manifest verifier;
3. run the unit tests;
4. inspect the documented trust model, evidence boundary and non-claims;
5. independently verify that no private cloud identifiers or raw provider evidence are required by the public verifier.

## Not reproducible from this repository alone

The original hardware-backed proof cannot be reproduced from this public repository because the private implementation, infrastructure configuration, raw CloudTrail evidence and recovery material are deliberately excluded.

That limitation is intentional: public verifiability is provided through stable commitments and explicit claims, without publishing sensitive infrastructure details.
