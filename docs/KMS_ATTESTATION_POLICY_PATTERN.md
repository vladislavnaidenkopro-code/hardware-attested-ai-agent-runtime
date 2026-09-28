# Sanitized KMS Recipient-Attestation Policy Pattern

This file shows the **shape** of an AWS KMS attestation-bound authorization rule. It is intentionally not copied from the private V8.0 environment.

It contains:

- no AWS account ID;
- no role or key ARN;
- no resource identifier;
- no real enclave measurement;
- no production permissions.

## Pattern

```json
{
  "Sid": "AllowExpectedAttestedEnclave",
  "Effect": "Allow",
  "Principal": {
    "AWS": "<AUTHORIZED_ROLE_ARN>"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEqualsIgnoreCase": {
      "kms:RecipientAttestation:PCR0": "<EXPECTED_PCR0_SHA384>"
    }
  }
}
```

AWS also documents `kms:RecipientAttestation:ImageSha384` and PCR-specific condition keys. The exact policy should be designed around the workload, operation set and deployment threat model.

## Security meaning

The important property is not the placeholder JSON itself. The property is that the KMS authorization decision can require a signed Nitro Enclave attestation document containing an expected measurement. If the request lacks a valid matching attestation document, the recipient-attestation condition is not satisfied.

## Boundary

This example is documentation only. It is not a deployable private V8.0 policy, does not disclose the verified V8.0 PCR values, and does not grant access to any real AWS resource.

Primary AWS reference:
https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclave.html
