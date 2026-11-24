# Troubleshooting Guide

This guide covers common issues encountered when discovering, installing, running, or validating RepoCraft across different agent environments.

## Common Issues and Solutions

### 1. Skill Not Detected by the Agent

#### Symptom
The AI agent does not trigger RepoCraft when you ask it to document or structure a repository, or slash commands like `/repocraft` are reported as unknown.

#### Causes and Fixes
- **Directory name mismatch:** The directory containing `SKILL.md` must be named exactly `repocraft`. If the folder is named `repocraft-main` or `RepoCraft`, rename it to lowercase `repocraft`.
- **Incorrect discovery path:** Verify that `SKILL.md` is placed inside the correct directory for your agent:
  - Claude Code: `.claude/skills/repocraft/SKILL.md` or `~/.claude/skills/repocraft/SKILL.md`
  - Cursor: `.cursor/skills/repocraft/SKILL.md` or `.agents/skills/repocraft/SKILL.md`
  - Codex: `.agents/skills/repocraft/SKILL.md` or `~/.agents/skills/repocraft/SKILL.md`
  - Antigravity: `.agents/skills/repocraft/SKILL.md` or `~/.gemini/config/skills/repocraft/SKILL.md`
- **Agent restart required:** Some agents cache skills in memory at startup. Restart your terminal session or reload your IDE window after copying the skill files.

---

### 2. Frontmatter Parsing Errors

#### Symptom
The agent reports an error parsing the skill manifest or fails to load metadata.

#### Causes and Fixes
- **Malformed YAML frontmatter:** Ensure that `SKILL.md` starts on line 1 with three hyphens `---` and closes the frontmatter with three hyphens `---`.
- **Special characters in description:** If you edit the description, ensure multi-line descriptions use proper YAML multiline folding (`>` or `|-`) or stay on a single quoted string.
- **Run the validator:** Run `python3 scripts/validate.py` in the RepoCraft repository to check for YAML syntax issues automatically.

---

### 3. Permission Denied Running Installation Scripts

#### Symptom
Executing `./scripts/install.sh` returns `Permission denied`.

#### Fix
Make the script executable:

```bash
chmod +x scripts/install.sh
./scripts/install.sh --agent all --scope global
```

On Windows PowerShell, if script execution is restricted by execution policy, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\scripts\install.ps1 -Agent all -Scope Global
```

---

### 4. Overwriting Existing Installations

#### Symptom
The installer warns that a destination directory already exists and halts.

#### Fix
By default, `scripts/install.sh` will not silently overwrite an existing skill directory. Pass the `--force` flag to confirm that you want to replace the previous installation:

```bash
./scripts/install.sh --agent claude --scope global --force
```

---

### 5. Cleaning Up After Uninstallation

#### Symptom
After uninstalling, the agent still refers to an old version of the skill.

#### Fix
Check for multiple installations in both project and global directories:
- Check your project root for `.claude/skills/repocraft`, `.cursor/skills/repocraft`, or `.agents/skills/repocraft`.
- Check your user home directory for `~/.claude/skills/repocraft`, `~/.cursor/skills/repocraft`, `~/.agents/skills/repocraft`, or `~/.gemini/config/skills/repocraft`.
- Remove any stale directories and restart the agent.

---

### 6. Validation Suite Failures

#### Symptom
`python3 scripts/validate.py` reports errors.

#### Fix
Review the output report:
- **Link check failures:** A relative Markdown link points to a file that does not exist. Ensure referenced templates or documents exist in their specified folders.
- **Forbidden em dash detected:** The validator scans for Unicode em dash characters (`\u2014`). Replace any em dashes with standard hyphens, colons, or parentheses.
- **Frontmatter constraint failures:** Check that `name` is lowercase alphanumeric with single hyphens, does not exceed 64 characters, and matches the parent directory.
