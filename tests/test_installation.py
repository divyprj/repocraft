import subprocess
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
INSTALL_SH = REPO_ROOT / "scripts" / "install.sh"


def test_install_script_dry_run():
    result = subprocess.run(
        [str(INSTALL_SH), "--agent", "all", "--scope", "global", "--dry-run"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Dry-run failed: {result.stderr}"
    assert "Would create directory:" in result.stdout
    assert "Installer completed successfully." in result.stdout


def test_install_script_custom_target():
    with tempfile.TemporaryDirectory() as temp_dir:
        target = Path(temp_dir) / "custom_repocraft"
        result = subprocess.run(
            [str(INSTALL_SH), "--agent", "claude", "--target-dir", str(target)],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"Custom target install failed: {result.stderr}"
        assert (target / "SKILL.md").is_file()
        assert (target / "README.md").is_file()
        assert (target / "docs" / "compatibility.md").is_file()

        un_result = subprocess.run(
            [str(INSTALL_SH), "--agent", "claude", "--target-dir", str(target), "--uninstall"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        assert un_result.returncode == 0
        assert not target.exists(), "Target directory should be removed after uninstall"


def test_install_all_project_scope_deduplicates_shared_paths():
    with tempfile.TemporaryDirectory() as temp_dir:
        project_dir = Path(temp_dir)
        result = subprocess.run(
            [str(INSTALL_SH), "--agent", "all", "--scope", "project"],
            cwd=str(project_dir),
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"Project scope install failed: {result.stderr}\n{result.stdout}"
        assert (project_dir / ".claude" / "skills" / "repocraft" / "SKILL.md").is_file()
        assert (project_dir / ".cursor" / "skills" / "repocraft" / "SKILL.md").is_file()
        assert (project_dir / ".agents" / "skills" / "repocraft" / "SKILL.md").is_file()
        assert (project_dir / ".opencode" / "skills" / "repocraft" / "SKILL.md").is_file()


def test_install_symlink_mode_and_uninstall():
    with tempfile.TemporaryDirectory() as temp_dir:
        target = Path(temp_dir) / "repocraft"
        result = subprocess.run(
            [str(INSTALL_SH), "--agent", "opencode", "--target-dir", str(target), "--symlink"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"Symlink install failed: {result.stderr}"
        assert target.is_symlink()
        assert (target / "SKILL.md").is_file()

        un_result = subprocess.run(
            [str(INSTALL_SH), "--agent", "opencode", "--target-dir", str(target), "--uninstall"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        assert un_result.returncode == 0
        assert not target.exists() and not target.is_symlink()
