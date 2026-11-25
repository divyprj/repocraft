# Cross-Agent Compatibility Matrix

RepoCraft adheres to the open Agent Skills specification (agentskills.io). It is built as a single canonical skill package that can be discovered, loaded, and executed across multiple AI coding agent ecosystems.

## Universal Compatibility Overview

| AI Agent / Platform | Canonical Discovery Paths | Scope Supported | Invocation Methods | Verification Status |
| :--- | :--- | :--- | :--- | :--- |
| **Anthropic Claude Code** | `.claude/skills/repocraft/`<br>`~/.claude/skills/repocraft/` | Project & Global | Prompt auto-trigger<br>`/repocraft` CLI command | Path & Packaging Verified |
| **Cursor** | `.cursor/skills/repocraft/`<br>`.agents/skills/repocraft/`<br>`~/.cursor/skills/repocraft/` | Project & Global | Semantic intent matching<br>Prompt instructions | Path & Packaging Verified |
| **OpenAI Codex / ChatGPT** | `.agents/skills/repocraft/`<br>`.codex/skills/repocraft/`<br>`~/.agents/skills/repocraft/` | Project, Global & Web Upload | Semantic intent matching<br>`$skill-installer`<br>ZIP bundle upload | Specification Aligned |
| **Google Antigravity** | `.agents/skills/repocraft/`<br>`~/.gemini/config/skills/repocraft/` | Workspace & Global | Progressive disclosure on matching prompt | Discovered in Workspace |
| **OpenCode** | `.opencode/skills/repocraft/`<br>`~/.config/opencode/skills/repocraft/` | Project & Global | Skill discovery on matching prompt | Path & Packaging Verified |

## Verification Classification

- **Path & Packaging Verified**: Filesystem scan paths, directory packaging, and automated installer mechanics have been validated against published agent specifications and automated test suites.
- **Specification Aligned**: Packaging format adheres strictly to the documented Agent Skills open standard schema (agentskills.io) and published platform developer documentation.
- **Discovered in Workspace**: Tested and discovered within the active Antigravity workspace runtime.

## Agent-Specific Implementation Details

### 1. Anthropic Claude Code

Claude Code scans both project-root and user-home configuration directories for skills:

- **Project scope:** `.claude/skills/repocraft/SKILL.md`
- **Global scope:** `~/.claude/skills/repocraft/SKILL.md`
- **Discovery model:** Reads YAML frontmatter at session start. The directory name (`repocraft`) becomes an executable slash command (`/repocraft`).
- **Triggering:** The agent reads the `description` field during conversation turns. When a user asks to document, audit, structure, or prepare a repository for GitHub, Claude Code pulls in the body of `SKILL.md`.

### 2. Cursor

Cursor supports the Agent Skills standard natively and supports fallbacks for multiple folder conventions:

- **Primary project path:** `.cursor/skills/repocraft/SKILL.md`
- **Universal project path:** `.agents/skills/repocraft/SKILL.md`
- **Primary global path:** `~/.cursor/skills/repocraft/SKILL.md`
- **Universal global path:** `~/.agents/skills/repocraft/SKILL.md`
- **Discovery model:** Scans skill folders on workspace index. Enables semantic matching based on skill description when prompts involve repository engineering.

### 3. OpenAI Codex and ChatGPT

OpenAI environments that implement the Agent Skills specification scan the `.agents` root or support direct archive deployment:

- **Repository path:** `$CWD/.agents/skills/repocraft/SKILL.md`
- **Global configuration path:** `~/.agents/skills/repocraft/SKILL.md`
- **CLI installation:** Supported via `$skill-installer repocraft` or ecosystem tooling (`npx skills add divyprj/repocraft --skill repocraft`).
- **ChatGPT Workspace:** For enterprise workspaces supporting skills, zip the `repocraft/` folder and upload through the workspace settings panel.

### 4. Google Antigravity

Google Antigravity utilizes progressive disclosure to inject skill instructions without bloating the model context:

- **Workspace path:** `.agents/skills/repocraft/SKILL.md`
- **Global machine path:** `~/.gemini/config/skills/repocraft/SKILL.md`
- **Discovery model:** The agent loads the `name` and `description` from the YAML frontmatter into its system registry at startup. The complete instructions in `SKILL.md` are loaded into active context when the user request matches repository engineering tasks.

### 5. OpenCode

OpenCode discovers Agent Skills from both repository and XDG user configuration paths:

- **Project path:** `.opencode/skills/repocraft/SKILL.md`
- **Global path:** `~/.config/opencode/skills/repocraft/SKILL.md`
- **Discovery model:** Loads YAML frontmatter metadata and activates `SKILL.md` when repository engineering, documentation, or audit tasks are requested.

## Canonical Architecture Principle

RepoCraft maintains a single authoritative `SKILL.md` file at the repository root. When installing into an agent directory, the skill directory is linked or copied without modifying the internal instructions.

This avoids divergence across agent implementations. All target platforms receive identical repository engineering rules without fork divergence.
