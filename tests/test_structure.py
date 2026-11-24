from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()


def test_required_governance_files():
    required = [
        "SKILL.md",
        "README.md",
        "LICENSE",
        "COPYRIGHT",
        "AUTHORS.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "CHANGELOG.md",
        "CODE_OF_CONDUCT.md",
        "NOTICE",
        "AGENTS.md",
    ]
    for filename in required:
        file_path = REPO_ROOT / filename
        assert file_path.is_file(), f"Missing required file: {filename}"
        assert file_path.stat().st_size > 0, f"File must not be empty: {filename}"


def test_docs_directory_completeness():
    docs = [
        "docs/compatibility.md",
        "docs/installation.md",
        "docs/usage.md",
        "docs/design-principles.md",
        "docs/troubleshooting.md",
    ]
    for doc in docs:
        doc_path = REPO_ROOT / doc
        assert doc_path.is_file(), f"Missing documentation file: {doc}"
        assert doc_path.stat().st_size > 0, f"Documentation file is empty: {doc}"


def test_no_em_dashes_in_markdown():
    em_dash = "\u2014"
    for path in REPO_ROOT.glob("**/*.md"):
        if ".git" in str(path):
            continue
        text = path.read_text(encoding="utf-8")
        assert em_dash not in text, f"Em dash found in {path.relative_to(REPO_ROOT)}"


def test_no_fabricated_domains():
    for ext in ("*.md", "*.yml", "*.yaml", "*.sh", "*.ps1"):
        for path in REPO_ROOT.glob(f"**/{ext}"):
            if ".git" in str(path):
                continue
            text = path.read_text(encoding="utf-8")
            assert "@repocraft.org" not in text, f"Fabricated domain found in {path.relative_to(REPO_ROOT)}"
            assert "@repocraft/" not in text, f"Fabricated team handle found in {path.relative_to(REPO_ROOT)}"
