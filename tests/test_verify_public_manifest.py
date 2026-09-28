import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify_public_manifest", ROOT / "tools" / "verify_public_manifest.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class PublicManifestTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "evidence" / "HASH_COMMITMENTS.json").read_text(encoding="utf-8"))

    def test_repository_manifest_is_valid(self):
        self.assertEqual([], MOD.validate_manifest(self.data))

    def test_rejects_invalid_sha256(self):
        bad = dict(self.data)
        bad["release_binding_sha256"] = "not-a-hash"
        self.assertTrue(MOD.validate_manifest(bad))

    def test_requires_non_claims(self):
        bad = dict(self.data)
        bad["non_claims"] = []
        self.assertTrue(MOD.validate_manifest(bad))


if __name__ == "__main__":
    unittest.main()
