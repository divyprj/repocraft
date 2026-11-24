from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()


def test_minimal_project_example():
    base = REPO_ROOT / "examples" / "minimal-project"
    assert (base / "README.md").is_file()
    assert (base / "LICENSE").is_file()
    assert (base / "COPYRIGHT").is_file()
    assert (base / "AUTHORS.md").is_file()
    assert (base / "docs" / "architecture" / "architecture.md").is_file()


def test_full_stack_project_example():
    base = REPO_ROOT / "examples" / "full-stack-project"
    assert (base / "README.md").is_file()
    assert (base / "docs" / "architecture" / "architecture.md").is_file()
    assert (base / "docs" / "architecture" / "system-design.md").is_file()
    assert (base / "docs" / "architecture" / "database-design.md").is_file()
    assert (base / "docs" / "architecture" / "api-reference.md").is_file()
    assert (base / "docs" / "architecture" / "decisions" / "ADR-001-postgresql-and-redis.md").is_file()
    assert (base / "docs" / "design" / "ui-guidelines.md").is_file()
    assert (base / "docs" / "deployment" / "deployment.md").is_file()
    assert (base / "AGENTS.md").is_file()


def test_ai_project_example():
    base = REPO_ROOT / "examples" / "ai-project"
    assert (base / "README.md").is_file()
    assert (base / "docs" / "architecture" / "architecture.md").is_file()
    assert (base / "docs" / "architecture" / "model-architecture.md").is_file()
    assert (base / "docs" / "architecture" / "data-pipeline.md").is_file()
    assert (base / "docs" / "architecture" / "evaluation.md").is_file()
    assert (base / "docs" / "architecture" / "inference-deployment.md").is_file()
    assert (base / "AGENTS.md").is_file()
