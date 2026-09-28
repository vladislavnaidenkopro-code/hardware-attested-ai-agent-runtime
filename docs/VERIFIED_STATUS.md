# Verified Status

## V8.0 — frozen verified baseline

This public showcase is bound to the V8.0 verification state represented by the following public-safe identifiers:

- verified code SHA: `c3b57fcedca3793ffed0b624c501f3ac1ba1b656`
- release binding SHA-256: `ec89d359be50c1016012aebe6142cbaf97cb809e44066b0238924f37afef2048`

Verified properties are limited to the specific private verification run summarized in `evidence/EVIDENCE_SUMMARY.md`.

## V8.1 — private productization work

V8.1 work is intentionally separated from the V8.0 baseline. Public roadmap items may describe design direction, but they are not V8.0 release claims.

Current productization themes include:

- confidential-runtime state recovery without secret plaintext persistence;
- configuration and trust-history preservation;
- operator evidence/status surfaces;
- deployment packaging and provider abstraction;
- enterprise identity integration;
- stronger exposure-intelligence data normalization.

## Evidence boundary

The public repository contains hash commitments and verification logic only. Raw provider evidence, private source, recovery material and infrastructure identifiers remain private.
