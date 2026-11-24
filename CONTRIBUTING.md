# Contributing to RepoCraft

Thank you for your interest in contributing to RepoCraft. As a developer tool that establishes repository standards, RepoCraft adheres strictly to its own engineering principles.

## Core Principles for Contributions

1. **Factual and Verifiable**: Every claim, command, and guideline must be tested and accurate.
2. **Universal Standard**: Maintain one canonical skill (`SKILL.md`) at root. Do not create divergent skill forks per agent.
3. **No Fluff**: Documentation must be concise, direct, and free of generic AI-generated hype.
4. **No Em Dashes**: In accordance with project style guidelines, do not use Unicode em dash characters. Use standard hyphens, colons, or parentheses.
5. **No Broken Links**: All internal relative links must resolve cleanly.

---

## Local Development Workflow

### 1. Prerequisites
- Git 2.20+
- Python 3.8+
- pytest (`pip install pytest`)
- Bash or PowerShell

### 2. Setup
Clone the repository:

```bash
git clone https://github.com/divyprj/repocraft.git
cd repocraft
```

### 3. Making Changes
- If modifying `SKILL.md`, ensure frontmatter remains strictly valid under the Agent Skills specification.
- If introducing templates, place them in the appropriate subfolder under `templates/` and provide concise, non-empty examples.
- If modifying installers (`scripts/install.sh` or `scripts/install.ps1`), test them in a temporary sandboxed directory.

---

## Testing and Verification

Before submitting a pull request, run the local validation suite:

```bash
python3 scripts/validate.py
pytest
```

All validation checks must pass with zero errors and zero warnings:
- Frontmatter schema validation
- Character length limits
- Relative link integrity
- Character scanning (no em dashes)
- Installation and uninstallation simulation

---

## Pull Request Guidelines

1. **Branch Naming**: Use descriptive prefixes such as `feat/`, `fix/`, `docs/`, or `refactor/`.
2. **Commit Messages**: Write clear, imperative commit messages (for example: `fix: correct Cursor global scan path in installation guide`).
3. **Scope Discipline**: Keep pull requests focused. Do not combine unrelated documentation changes with script refactoring.
4. **PR Description**: Fill out the pull request template completely, detailing what was tested and which agent ecosystems were verified.
