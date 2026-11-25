import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
AUDIT_PY = REPO_ROOT / "scripts" / "audit.py"


def test_audit_repocraft_itself_scores_100():
    result = subprocess.run(
        [sys.executable, str(AUDIT_PY), str(REPO_ROOT), "--json", "--min-score", "95"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Audit failed: {result.stderr}\n{result.stdout}"
    data = json.loads(result.stdout)
    assert data["score"] == 100, f"Expected 100 on RepoCraft itself, got {data}"
    assert data["findings"] == []


def test_audit_detects_missing_files_broken_links_and_missing_ci_workflow():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "README.md").write_text(
            "# Demo\n\n"
            "[![CI](https://github.com/org/repo/actions/workflows/ci.yml/badge.svg)](https://github.com/org/repo/actions/workflows/ci.yml)\n"
            "This is a cutting-edge tool. See [Missing](docs/missing.md).\n",
            encoding="utf-8",
        )
        result = subprocess.run(
            [sys.executable, str(AUDIT_PY), str(root), "--json"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        data = json.loads(result.stdout)
        assert data["score"] < 70
        categories = {f["category"] for f in data["findings"]}
        assert {"governance", "ci", "links", "style"}.issubset(categories)
