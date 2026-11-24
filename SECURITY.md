# Security Policy

Security and the integrity of repository automation are treated with high priority in RepoCraft.

## Supported Versions

| Version | Supported |
| :--- | :--- |
| 1.0.x | Yes |
| < 1.0 | No |

---

## Reporting a Security Vulnerability

If you discover a security vulnerability or security defect in RepoCraft, please report it responsibly.

**Do NOT report security vulnerabilities via public GitHub issues.**

Please report vulnerabilities privately through GitHub Private Vulnerability Reporting:

1. Navigate to the repository on GitHub (`https://github.com/divyprj/repocraft`).
2. Click the **Security** tab.
3. Under **Reporting**, click **Advisories** and select **Report a vulnerability**.

### What to Include
1. Description of the vulnerability and its potential impact.
2. Step-by-step reproduction instructions or a minimal proof of concept.
3. Affected versions, agent ecosystems, and environments.
4. Proposed remediation or patch if available.

### Response Timeline
- An acknowledgment will be sent within 48 hours of receipt.
- A status update and triage verdict will be provided within 5 business days.
- A public security advisory and patched release will be coordinated once remediation is validated.

---

## Security Considerations for AI Agent Skills

RepoCraft provides instructions and guidelines for AI coding agents. Users should keep in mind:

1. **Instruction vs Sandbox**: Skill instructions guide model reasoning and prompt composition. They do not enforce operating system-level process sandboxing, credential masking, or network restrictions.
2. **Secrets Protection**: RepoCraft strictly prohibits embedding production credentials, API tokens, or secrets in repository documentation, examples, or test fixtures.
3. **Execution Safety**: When running agent commands, always ensure the agent is operating within a sanctioned workspace with appropriate permission boundaries.
