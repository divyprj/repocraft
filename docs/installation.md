# Installation Guide

RepoCraft can be installed locally for a single project or globally for all projects on your machine across Claude Code, Cursor, OpenAI Codex, and Google Antigravity.

## Prerequisites

- Git 2.20 or newer
- Bash (Linux / macOS) or PowerShell 5.1+ (Windows)
- Python 3.8+ (optional, only needed for running the validation suite)

## Quick Start (Automated Installer)

The repository provides an automated installation script that detects your agent environment, verifies skill files, and places them into the correct discovery directory.

### Linux and macOS

Clone the repository and run `scripts/install.sh`:

```bash
git clone https://github.com/divyprj/repocraft.git
cd repocraft
chmod +x scripts/install.sh
./scripts/install.sh --agent all --scope global
```

### Windows (PowerShell)

```powershell
git clone https://github.com/divyprj/repocraft.git
cd repocraft
.\scripts\install.ps1 -Agent all -Scope Global
```

The installer supports targeting individual agents (`--agent claude`, `--agent cursor`, `--agent codex`, `--agent antigravity`, or `--agent all`) and scopes (`--scope project` or `--scope global`).

---

## Agent-Specific Manual Installation

If you prefer manual setup without scripts, follow the copyable steps below for your target environment.

### 1. Anthropic Claude Code

#### Project-Level Installation (Current Repository Only)
Run from the root of your project:

```bash
mkdir -p .claude/skills/repocraft
cp -r /path/to/repocraft/* .claude/skills/repocraft/
```

#### Global Installation (All Projects on Machine)

```bash
mkdir -p ~/.claude/skills/repocraft
cp -r /path/to/repocraft/* ~/.claude/skills/repocraft/
```

#### Verification
Start Claude Code in your terminal:

```bash
claude skills list
```

You should see `repocraft` listed. You can also invoke it directly using `/repocraft`.

---

### 2. Cursor

#### Project-Level Installation
Run from your project root:

```bash
mkdir -p .cursor/skills/repocraft
cp -r /path/to/repocraft/* .cursor/skills/repocraft/
```

Cursor also natively recognizes the universal `.agents/skills/` directory:

```bash
mkdir -p .agents/skills/repocraft
cp -r /path/to/repocraft/* .agents/skills/repocraft/
```

#### Global Installation

```bash
mkdir -p ~/.cursor/skills/repocraft
cp -r /path/to/repocraft/* ~/.cursor/skills/repocraft/
```

#### Verification
Open Cursor Settings, navigate to Skills or Rules, and confirm that `repocraft` appears in the discovered skills list.

---

### 3. OpenAI Codex and ChatGPT

#### Repository-Level Installation

```bash
mkdir -p .agents/skills/repocraft
cp -r /path/to/repocraft/* .agents/skills/repocraft/
```

#### Global User-Level Installation

```bash
mkdir -p ~/.agents/skills/repocraft
cp -r /path/to/repocraft/* ~/.agents/skills/repocraft/
```

#### Verification
In your Codex session or CLI prompt, ask: "Which skills are available in this repository?" Codex will report `repocraft` with its description.

---

### 4. Google Antigravity

#### Workspace-Level Installation

```bash
mkdir -p .agents/skills/repocraft
cp -r /path/to/repocraft/* .agents/skills/repocraft/
```

#### Global Machine-Level Installation

```bash
mkdir -p ~/.gemini/config/skills/repocraft
cp -r /path/to/repocraft/* ~/.gemini/config/skills/repocraft/
```

#### Verification
Launch Antigravity in the project workspace. In the conversation, ask: "What skills do you have for repository engineering?" Antigravity will detect RepoCraft and list its capabilities.

---

## Updating RepoCraft

To update an existing installation to the latest version:

### Automated Update
Pull the latest commits from the RepoCraft repository and rerun the installer with `--force`:

```bash
cd /path/to/repocraft
git pull origin main
./scripts/install.sh --agent all --scope global --force
```

### Manual Update
Simply overwrite the existing skill folder in your target agent's skill directory with the updated contents of the RepoCraft repository.

---

## Uninstallation

To remove RepoCraft without affecting any other skills or user files:

### Automated Uninstallation

```bash
./scripts/install.sh --agent all --scope global --uninstall
```

### Manual Uninstallation
Delete the specific `repocraft` folder from the respective skills directory:

- Claude Code: `rm -rf ~/.claude/skills/repocraft` or `rm -rf .claude/skills/repocraft`
- Cursor: `rm -rf ~/.cursor/skills/repocraft` or `rm -rf .cursor/skills/repocraft`
- Codex: `rm -rf ~/.agents/skills/repocraft` or `rm -rf .agents/skills/repocraft`
- Antigravity: `rm -rf ~/.gemini/config/skills/repocraft` or `rm -rf .agents/skills/repocraft`
