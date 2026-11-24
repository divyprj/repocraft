# Usage Guide

RepoCraft equips AI coding agents with strict, professional repository engineering and technical documentation standards. Once installed, the skill can be invoked explicitly or triggered automatically when performing repository-related tasks.

## How Agents Discover RepoCraft

AI coding agents that implement the Agent Skills specification inspect the `description` field in `SKILL.md` during conversation planning. 

When your prompt mentions tasks such as:
- Initializing or structuring a new GitHub repository
- Documenting an existing software project
- Auditing existing documentation for technical accuracy
- Writing architecture records, system design, or ADRs
- Setting up contributor attribution, license, or security policies
- Establishing `AGENTS.md` rules for coding agents

The agent activates RepoCraft and follows its 25 core engineering rules and verification procedures.

---

## The 5 Execution Modes

RepoCraft operates in five distinct modes depending on your specific goal.

### Mode A: New Repository Creation
Use this mode when starting a new software project or structuring a codebase for the first time.

**What the agent does:**
- Inspects project type, languages, and dependencies.
- Establishes a clean directory layout.
- Prepares essential root documentation (`README.md`, `LICENSE`, `COPYRIGHT`, `AUTHORS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`).
- Creates root `AGENTS.md` with repository-specific coding rules.
- Prepares `.github/` templates for pull requests and issue tracking.

**Example Prompts:**
- "Initialize a complete GitHub repository structure for this new Python service using RepoCraft standards."
- "Apply RepoCraft Mode A to scaffold our documentation and GitHub configuration."

---

### Mode B: Documenting an Existing Repository
Use this mode when bringing an existing codebase up to professional engineering standards.

**What the agent does:**
- Conducts a thorough source code inspection (models, routes, database migrations, CI configs).
- Extracts actual implementations rather than relying on previous descriptions.
- Rewrites or updates `README.md` to match reality.
- Generates detailed architecture documentation with Mermaid diagrams in `docs/architecture/`.
- Documents system design and database ER relationships if applicable.
- Identifies missing governance or attribution files.

**Example Prompts:**
- "Inspect this repository and generate complete, accurate architecture and system design documentation following RepoCraft."
- "Audit and rewrite the project README to match what the code actually does."

---

### Mode C: Documentation-Only Task
Use this mode when you need documentation improvements without touching application code.

**What the agent does:**
- Restricts all changes strictly to Markdown, documentation assets, and metadata files.
- Refrains from refactoring application logic, installing dependencies, or changing build scripts.
- Verifies that all commands and references in documentation point to existing code.

**Example Prompts:**
- "Create an Architecture Decision Record (ADR) for our switch to PostgreSQL. Do not modify any application code."
- "Generate API reference documentation based on our existing FastAPI routes without altering source files."

---

### Mode D: Documentation Maintenance After Code Changes
Use this mode after landing a feature, schema change, or major refactor.

**What the agent does:**
- Inspects the git diff or recent commits.
- Identifies which sections of `README.md`, `docs/architecture/`, or `docs/deployment/` are outdated.
- Updates only the affected documentation sections without touching unrelated content.
- Appends entries to `CHANGELOG.md` under the correct category (Added, Changed, Fixed, etc.).

**Example Prompts:**
- "We just migrated our user authentication to OAuth2. Update the architecture and development documentation to reflect these changes."
- "Update CHANGELOG.md and our README deployment guide for the latest v1.2 release."

---

### Mode E: Repository Audit
Use this mode to review a repository before making it public or submitting it for compliance.

**What the agent does:**
- Audits repository structure, documentation completeness, and security posture.
- Checks for exposed secrets, missing license notices, and unverified contributor claims.
- Evaluates whether documentation contains prohibited AI marketing language or unverified claims.
- Delivers a prioritized findings report with actionable recommendations.

**Example Prompts:**
- "Run a RepoCraft Mode E audit on this repository and tell me what is missing before we make it public on GitHub."
- "Review our documentation and repository governance for security, attribution, and technical accuracy."

---

## Practical Invocation Across Agents

### In Claude Code
You can invoke the skill via slash command:
```text
/repocraft Audit our current docs and generate an ADR for the caching layer.
```
Or prompt naturally:
```text
Use RepoCraft to structure our repository governance and write CONTRIBUTING.md and SECURITY.md.
```

### In Cursor
In Cursor Chat (Cmd+L / Ctrl+L) or Composer (Cmd+I / Ctrl+I):
```text
Apply the RepoCraft skill to review our system architecture and create docs/architecture/architecture.md with Mermaid diagrams.
```

### In OpenAI Codex / ChatGPT
In Codex CLI or ChatGPT Workspace:
```text
According to the repocraft skill, review our repository source code and produce an accurate system design document.
```

### In Google Antigravity
In the Antigravity conversation:
```text
Act under the RepoCraft skill. Inspect our database migrations and produce docs/architecture/database-design.md with an ER diagram.
```

---

## Quality Control Checklist

Before accepting documentation generated by an agent under RepoCraft, verify:

1. **Accuracy**: Did the agent verify source code before writing? Are commands copy-paste runnable?
2. **Restraint**: Did the agent avoid creating unnecessary files just to fill space?
3. **No Fluff**: Is the tone direct, factual, and free of AI marketing clichés?
4. **Attribution**: Are copyright and author credits accurate and confirmed?
5. **Security**: Are environment variables, API keys, and sensitive tokens omitted from all docs?
