from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_publication.py"


class PublicationCheckTest(unittest.TestCase):
    def run_check(self, files: dict[str, str]) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for relative_path, content in files.items():
                path = root / relative_path
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), "--root", str(root)],
                text=True,
                capture_output=True,
                check=False,
            )

    def test_clean_documentation_passes(self) -> None:
        result = self.run_check({"index.md": "# Documentation publique\n"})

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("publication scan: PASS", result.stdout)

    def test_secret_assignment_fails_without_echoing_value(self) -> None:
        secret = "super-secret-value-123456"
        result = self.run_check({"config.md": f"api_key = {secret}\n"})

        self.assertEqual(result.returncode, 1)
        self.assertIn("secret_assignment", result.stdout)
        self.assertNotIn(secret, result.stdout + result.stderr)

    def test_private_key_header_fails(self) -> None:
        result = self.run_check(
            {"private.md": "-----BEGIN PRIVATE KEY-----\nredacted\n"}
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("private_key", result.stdout)

    def test_explicit_public_file_is_scanned(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            docs.mkdir()
            (docs / "index.md").write_text("# Clean\n", encoding="utf-8")
            public_file = root / "README.md"
            public_file.write_text("email: person@example.test\n", encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--root",
                    str(docs),
                    "--file",
                    str(public_file),
                ],
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("email", result.stdout)
        self.assertNotIn("person@example.test", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
