# RepoCraft

**Universal Repository Engineering Skill**

A universal AI coding agent skill for professional repository engineering, technical documentation, architecture, governance, and intellectual property protection.

[![Validate Skill](https://github.com/divyprj/repocraft/actions/workflows/validate.yml/badge.svg)](https://github.com/divyprj/repocraft/actions/workflows/validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Specification: Agent Skills](https://img.shields.io/badge/Standard-Agent_Skills-green.svg)](https://agentskills.io)

---

## Why RepoCraft Exists

Modern AI coding agents can generate hundreds of lines of code and documentation in seconds. However, without strict engineering standards, agents frequently produce:

- Fabricated APIs and non-existent configuration options.
- Generic marketing boilerplate ("cutting-edge revolutionary solution").
- Unmaintainable, disconnected documentation trees with empty placeholder files.
- Misleading or non-existent developer attribution and licensing records.
- Deceptive attempts to protect intellectual property via prompt injection or hidden comments.

RepoCraft solves this by transforming AI coding agents into rigorous repository maintainers. It enforces human-grade engineering standards: source code inspection before writing, factual accuracy over appearance, practical repository governance, verifiable attribution, and context-efficient documentation architecture.

---

## Core Capabilities

- **Factual Codebase Inspection**: Enforces thorough examination of actual source files, dependency manifests, database schemas, and CI/CD pipelines before any documentation is generated.
- **Progressive Architecture Documentation**: Generates readable Mermaid architecture diagrams, system design specs, database ER models, and Architecture Decision Records (ADRs).
- **Practical Repository Governance**: Scaffolds manageable pull request templates, issue templates, CODEOWNERS rules, and branch protection recommendations.
- **Intellectual Property and Legal Clarity**: Provides clear copyright notices, attribution manifests (AUTHORS.md, NOTICE), and responsible open-source license evaluations.
- **AI Coding Agent Rules (`AGENTS.md`)**: Configures root governance instructions that guide future coding agents to respect codebase architecture and boundaries.
- **Universal Cross-Platform Standard**: Adheres strictly to the open Agent Skills specification (agentskills.io), operating seamlessly across Anthropic Claude Code, Cursor, OpenAI Codex, and Google Antigravity.

---

## Supported AI Agents

| Agent Ecosystem | Discovery Path | Scope | Verification Status |
| :--- | :--- | :--- | :--- |
| **Anthropic Claude Code** | `.claude/skills/repocraft/` or `~/.claude/skills/repocraft/` | Project / Global | Path & Packaging Verified |
| **Cursor** | `.cursor/skills/repocraft/` or `.agents/skills/repocraft/` | Project / Global | Path & Packaging Verified |
| **OpenAI Codex / ChatGPT** | `.agents/skills/repocraft/` or `~/.agents/skills/repocraft/` | Project / Global / Web | Specification Aligned |
| **Google Antigravity** | `.agents/skills/repocraft/` or `~/.gemini/config/skills/repocraft/` | Workspace / Global | Discovered in Workspace |

For complete compatibility notes and discovery paths, see [docs/compatibility.md](docs/compatibility.md).

---

## Installation

RepoCraft can be installed using automated scripts, standard git clone, or manual file placement.

### Automated Installation (Linux / macOS)

```bash
git clone https://github.com/divyprj/repocraft.git
cd repocraft
chmod +x scripts/install.sh
./scripts/install.sh --agent all --scope global
```

### Automated Installation (Windows PowerShell)

```powershell
git clone https://github.com/divyprj/repocraft.git
cd repocraft
.\scripts\install.ps1 -Agent all -Scope Global
```

### Manual Installation (Quick Copy)

To install for a specific agent in your current project:

- **Claude Code**: Copy the repository folder into `.claude/skills/repocraft/`
- **Cursor**: Copy the repository folder into `.cursor/skills/repocraft/`
- **OpenAI Codex**: Copy the repository folder into `.agents/skills/repocraft/`
- **Google Antigravity**: Copy the repository folder into `.agents/skills/repocraft/`

For detailed step-by-step instructions, global setup, updates, and uninstallation, see [docs/installation.md](docs/installation.md).

---

## Usage

Once installed, your AI agent automatically recognizes RepoCraft during repository planning. You can also trigger it directly.

### The 5 Execution Modes

1. **Mode A (New Repository)**: Scaffolds initial structure, baseline documentation, and governance for a new project.
2. **Mode B (Existing Repository)**: Inspects source code and brings documentation, architecture diagrams, and records up to date.
3. **Mode C (Documentation-Only)**: Modifies documentation and metadata files only; prohibits altering application code.
4. **Mode D (Documentation Maintenance)**: Surgically updates docs and changelogs affected by recent code or schema changes.
5. **Mode E (Repository Audit)**: Reviews existing repository structure, security, and attribution, delivering a prioritized gap analysis.

### Example Invocations

- **Claude Code**: `/repocraft Audit our current codebase and generate missing architecture documentation.`
- **Cursor**: `Apply the RepoCraft skill to inspect our database models and produce an accurate database-design.md with Mermaid ER diagrams.`
- **OpenAI Codex**: `Apply RepoCraft Mode A to initialize repository governance and AGENTS.md for this project.`
- **Google Antigravity**: `Under the RepoCraft skill, review our API routes and write docs/architecture/api-reference.md.`

For in-depth usage patterns, workflows, and prompts, see [docs/usage.md](docs/usage.md).

---

## Repository Structure

```text
repocraft/
|-- SKILL.md                 # Canonical, authoritative skill instructions
|-- README.md                # Project landing documentation
|-- LICENSE                  # Active repository license evaluation
|-- COPYRIGHT                # Formal copyright notice
|-- AUTHORS.md               # Authorship and maintainer manifest
|-- NOTICE                   # Third-party standard and spec attribution
|-- CONTRIBUTING.md          # Contribution guidelines
|-- SECURITY.md              # Vulnerability reporting and security standards
|-- CHANGELOG.md             # Semantic version release history
|-- CODE_OF_CONDUCT.md       # Code of Conduct
|-- AGENTS.md                # AI coding agent instructions for RepoCraft
|
|-- docs/                    # Detailed technical manuals
|   |-- compatibility.md     # Cross-agent compatibility matrix
|   |-- installation.md      # Platform-specific installation instructions
|   |-- usage.md             # Execution modes, workflows, and prompts
|   |-- design-principles.md # Core engineering principles and philosophy
|   |-- troubleshooting.md   # Diagnostic and resolution steps
|
|-- templates/               # Reusable, production-ready engineering templates
|   |-- documentation/       # README, CONTRIBUTING, SECURITY, AGENTS templates
|   |-- architecture/        # Architecture, system design, database templates
|   |-- adr/                 # Architecture Decision Record templates
|   |-- github/              # CODEOWNERS, PR, and issue templates
|
|-- examples/                # Realistic illustrative reference implementations
|   |-- minimal-project/     # Lightweight utility/CLI documentation setup
|   |-- full-stack-project/  # Multi-tier web app architecture documentation
|   |-- ai-project/          # AI/ML pipeline and model documentation
|
|-- scripts/                 # Maintenance, installation, and validation tools
|   |-- install.sh           # Shell installer for Linux and macOS
|   |-- install.ps1          # PowerShell installer for Windows
|   |-- validate.py          # Standalone metadata and repository validator
|   |-- sync-github.sh       # GitHub metadata and release synchronizer
|
|-- tests/                   # Automated pytest verification test suite
|-- .github/                 # Workflows and issue/PR templates
```

---

## Validation and Quality Assurance

RepoCraft includes an automated Python validator that verifies frontmatter compliance, standard link integrity, character constraints, and installation mechanics without external runtime dependencies:

```bash
python3 scripts/validate.py
```

Run the automated test suite with pytest:

```bash
pytest
```

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code style, validation requirements, and pull request procedures. All participants are expected to adhere to our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

## Licensing and Intellectual Property

RepoCraft is open-source software created by Divyansh Prajapati. The project evaluates and supports standard permissive licenses (Apache-2.0 and MIT).

See [LICENSE](LICENSE) for terms and [COPYRIGHT](COPYRIGHT) for legal notices.
Third-party standards and specifications are acknowledged in [NOTICE](NOTICE).

---

## Known Limitations

- **Instruction, Not Hard Sandbox**: Like all agent skills, RepoCraft instructs the agent's reasoning. It does not enforce OS-level sandbox permissions or network firewalls.
- **Model Capability Dependence**: The quality of architecture extraction depends on the underlying model's reasoning capabilities. RepoCraft maximizes rigor through explicit inspection prompts, but does not replace human code review.
- **Context Window Limits**: Extremely large monorepos with hundreds of packages should be inspected module-by-module rather than in a single monolithic prompt.
