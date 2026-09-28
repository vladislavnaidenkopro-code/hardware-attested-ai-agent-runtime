# Public Evidence Summary

## Release claim

**Hardware-backed live proof:** AWS Nitro Enclaves + KMS attestation + CloudTrail integrity evidence.

## Public-safe commitments

- Release binding SHA-256: `ec89d359be50c1016012aebe6142cbaf97cb809e44066b0238924f37afef2048`
- Verified code SHA: `c3b57fcedca3793ffed0b624c501f3ac1ba1b656`
- CloudTrail digest-chain commitment: `27411e5ab8bd5b11ccf844457ceea0630197e395619b3e692d4f47b1055b506c`
- Event membership commitment: `702c6565210bd2c5354568711217047a017dafef62efd625419bba41342d3c8f`

## What was verified privately

- A real enclave measurement was produced.
- KMS denied an invalid authorization path.
- KMS accepted the expected attested measurement.
- The successful decrypt event contained provider-side attestation metadata.
- The target decrypt event was found exactly once inside a digest-verified CloudTrail log file.
- The signed CloudTrail digest chain validated successfully.
- The exported secret-print scan was empty.
- The full local regression and V8 release preflight passed.

## What is not public

Raw evidence files, account identifiers, resource identifiers, IAM/KMS policies, internal runbooks and private implementation code are retained only in the private evidence and recovery archive.
