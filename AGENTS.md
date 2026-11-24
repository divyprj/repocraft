# AI Coding Agent Governance: RepoCraft

This document governs any AI coding agent operating inside the RepoCraft repository.

## 1. Project Overview

RepoCraft is a universal AI coding agent skill for professional repository engineering, technical documentation, architecture, governance, and intellectual property protection. It is distributed as an open Agent Skills package compatible with Claude Code, Cursor, OpenAI Codex, and Google Antigravity.

---

## 2. Directory Structure and Boundaries

```text
repocraft/
|-- SKILL.md                 # Read-only canonical skill (architectural changes require maintainer signoff)
|-- docs/                    # Technical documentation and guides
|-- templates/               # Reusable documentation and architecture templates
|-- examples/                # Realistic illustrative project implementations
|-- scripts/                 # Bash, PowerShell, and Python automation utilities
|-- tests/                   # Automated pytest verification suite
|-- .github/                 # Workflows and issue/PR templates
```

---

## 3. Agent Operating Rules

1. **Canonical Source of Truth**:
   The root `SKILL.md` is the authoritative skill implementation. Never create divergent, agent-specific copies of the core instructions.
2. **Frontmatter Integrity**:
   The YAML frontmatter in `SKILL.md` must strictly adhere to the Agent Skills open standard schema (`name`, `description`, `license`, `compatibility`, `metadata`). The `name` field must remain `repocraft`.
3. **No Em Dashes**:
   Do not use Unicode em dash characters (U+2014). Use standard hyphens, colons, or parentheses.
4. **No AI Marketing Fluff**:
   Never introduce generic promotional claims ("cutting-edge", "revolutionary", "seamless"). Maintain concise, direct, factual developer documentation.
5. **Validation Gate**:
   After making any change to `SKILL.md`, `templates/`, `scripts/`, or `docs/`, you must execute the automated validation suite:
   ```bash
   python3 scripts/validate.py
   pytest
   ```
   All checks must pass with exit code 0 before concluding.
6. **No Breaking Modifications**:
   Preserve existing templates and documentation structures unless an explicit improvement is requested by the maintainer.
