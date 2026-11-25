# Changelog

All notable changes to RepoCraft will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-11-25

### Added
- Active GitHub Actions validation workflow at `.github/workflows/validate.yml` running across Ubuntu and macOS.
- OpenCode agent support (`~/.config/opencode/skills/repocraft` and `.opencode/skills/repocraft`) and `--symlink` live-update mode in `scripts/install.sh`.
- Quick Mode Router table and Section 26 (Large Repository Scoping and Verification Hooks) in `SKILL.md`.
- Visual repository assets (`assets/hero-banner.jpg`, `assets/before-after.svg`, `assets/workflow-modes.svg`) and overhauled `README.md`.
- HTML image link verification, bash syntax validation (`bash -n`), CI workflow checks, and `--json` output mode in `scripts/validate.py`.
- Regression tests in `tests/test_installation.py` covering project-scope path deduplication, `--symlink`, and OpenCode installs.

### Fixed
- Deduplicated shared `.agents/skills/repocraft` destination in `scripts/install.sh` so `--agent all --scope project` succeeds without failing on duplicate target paths.
- Split comma-separated topics into repeated `--add-topic` arguments in `scripts/sync-github.sh` for cross-version `gh` CLI compatibility.

## [1.0.0] - 2026-11-24

### Added
- Canonical `SKILL.md` frontmatter compliant with the Agent Skills open standard (agentskills.io).
- Cross-platform installer scripts `scripts/install.sh` (Linux/macOS) and `scripts/install.ps1` (Windows).
- Cross-agent compatibility documentation and discovery paths for Claude Code, Cursor, OpenAI Codex, and Google Antigravity.
- Standalone Python repository and frontmatter validation script (`scripts/validate.py`).
- Automated pytest test suite in `tests/` covering metadata, installer simulations, and link integrity.
- Production-grade engineering templates for documentation, architecture, system design, database ER models, ADRs, and GitHub governance.
- Realistic reference examples for minimal CLI, full-stack web, and AI/ML project architectures.
- GitHub Actions CI workflow for continuous skill validation across platforms.
- Project governance documentation: README, CONTRIBUTING, SECURITY, AUTHORS, NOTICE, COPYRIGHT, and AGENTS rules.
