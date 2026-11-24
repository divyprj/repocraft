import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()


def test_skill_md_exists():
    skill_file = REPO_ROOT / "SKILL.md"
    assert skill_file.is_file(), "SKILL.md must exist at repository root"
    assert skill_file.stat().st_size > 0, "SKILL.md must not be empty"


def test_frontmatter_schema():
    skill_file = REPO_ROOT / "SKILL.md"
    content = skill_file.read_text(encoding="utf-8")
    assert content.startswith("---"), "SKILL.md must start with --- delimiter"
    parts = content.split("---", 2)
    assert len(parts) >= 3, "Frontmatter must be enclosed by --- delimiters"

    fm_text = parts[1]
    
    # Parse keys
    keys = {}
    for line in fm_text.splitlines():
        line = line.strip()
        if line and ":" in line and not line.startswith("#"):
            k, v = line.split(":", 1)
            keys[k.strip()] = v.strip().strip('"\'')

    # Verify name
    assert "name" in keys, "Frontmatter must contain 'name'"
    assert keys["name"] == "repocraft", "Skill name must be 'repocraft'"
    assert re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", keys["name"]), "Skill name violates naming regex"
    assert len(keys["name"]) <= 64, "Skill name must not exceed 64 chars"

    # Verify description
    assert "description" in keys, "Frontmatter must contain 'description'"
    assert len(keys["description"]) > 0, "Description must not be empty"
    assert len(keys["description"]) <= 1024, "Description must not exceed 1024 chars"

    # Verify compatibility
    if "compatibility" in keys:
        assert len(keys["compatibility"]) <= 500, "Compatibility must not exceed 500 chars"
