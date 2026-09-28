#!/usr/bin/env python3
"""Validate the public-safe V8 commitment manifest without external dependencies."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
EXPECTED_SCHEMA = "v8-public-hash-commitments-1"
REQUIRED_NON_CLAIMS = {
    "production readiness",
    "certification",
    "SLA",
    "universal attack prevention",
    "customer security outcomes",
    "exactly-once external delivery",
}


def validate_manifest(data: dict) -> list[str]:
    errors: list[str] = []
    if data.get("schema") != EXPECTED_SCHEMA:
        errors.append(f"unexpected schema: {data.get('schema')!r}")

    sha256_fields = (
        "release_binding_sha256",
        "cloudtrail_digest_chain_sha256",
        "event_membership_sha256",
    )
    values: list[str] = []
    for field in sha256_fields:
        value = data.get(field)
        if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
            errors.append(f"{field} must be a lowercase 64-character SHA-256 hex digest")
        else:
            values.append(value)

    code_sha = data.get("verified_code_sha")
    if not isinstance(code_sha, str) or not COMMIT_RE.fullmatch(code_sha):
        errors.append("verified_code_sha must be a lowercase 40-character Git commit SHA")

    if len(values) != len(set(values)):
        errors.append("public SHA-256 commitment values must be distinct")

    non_claims = data.get("non_claims")
    if not isinstance(non_claims, list):
        errors.append("non_claims must be a list")
    else:
        missing = REQUIRED_NON_CLAIMS.difference(non_claims)
        if missing:
            errors.append("missing required non-claims: " + ", ".join(sorted(missing)))

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_public_manifest.py <manifest.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2

    errors = validate_manifest(data)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"PASS: {path} is a valid {EXPECTED_SCHEMA} manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
