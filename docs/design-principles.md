# Engineering Design Principles

RepoCraft is built on ten fundamental principles. These principles govern how software repositories should be structured, documented, and maintained, particularly in an era where AI coding agents can generate vast amounts of boilerplate in seconds.

## The Ten Core Principles

### 1. Accuracy Over Appearance
A visually stunning document full of inaccurate commands, hypothetical APIs, or misstated dependencies is worse than no documentation at all. It misleads engineers, breaks onboarding pipelines, and wastes developer hours. Documentation must describe the system that exists, not the system someone wished existed.

### 2. Maintainability Over Unnecessary Complexity
Complex documentation hierarchies that require twenty separate files for a simple 200-line CLI tool quickly fall out of sync with code. Every document introduced creates ongoing maintenance overhead. Structure documentation proportionally to the actual complexity of the software.

### 3. Actual Implementation Over Assumptions
Never document an architecture based solely on high-level descriptions or previous README drafts. Inspect the models, the routes, the build scripts, and the deployment manifests. If a feature is described in an issue tracker but does not exist in the code, it must not be documented as an active feature.

### 4. Clear Documentation Over Excessive Documentation
High-density, concise documentation is read and understood. Bloated, verbose documentation is skipped. Avoid repetition across documents. If an installation process is explained in the README, link to it rather than duplicating it in three other subdirectories.

### 5. Security Over Convenience
Never paste production credentials, private keys, database connection strings, or authorization tokens into documentation or screenshots. Ensure that sensitive configuration is isolated in environment variable references and example `.env.example` templates with redacted values.

### 6. Verifiable Attribution Over Invented Credits
Attribution in open-source projects is legally and professionally binding. Never invent contributors, fake maintainers, or assume that the creator of a repository authored every bundled dependency. Credit only verifiable individuals and include proper third-party notices where required by upstream licenses.

### 7. Practical Repository Governance Over Decorative Configuration
Do not add complex GitHub Actions, issue triage bots, or multi-tiered CODEOWNERS configurations that the repository owner cannot realistically maintain. Every piece of repository governance should serve an active, manageable purpose.

### 8. Consistency Across Documentation and Source Code
Naming conventions, directory references, CLI flags, and configuration keys must match across source code, test files, and documentation. If a configuration flag changes from `--port` to `--listen-port` in the code, all documentation must be updated atomically.

### 9. Preserve Existing Project Decisions
Unless there is a verified, justified defect or explicit request from the repository owner, preserve existing architectural choices, framework decisions, and established formatting styles. Do not impose arbitrary stylistic rewrites on functional projects.

### 10. Do Not Introduce Unnecessary Tools or Files
Never create files simply to make a repository appear more comprehensive. Every file in the repository tree must serve an identifiable operational, architectural, legal, or governance role.

---

## Combating AI Documentation Slop

AI coding agents often fall into destructive documentation patterns:
- Using inflated marketing clichés ("seamlessly empowers next-generation workflows").
- Generating dozens of placeholder files with `TODO` markers or empty sections.
- Fabricating imaginary database tables or backend endpoints.
- Inventing historical decisions in Architecture Decision Records.

RepoCraft acts as a strict counterweight. It forbids placeholder documents, bans promotional language, mandates source code verification before writing, and enforces direct, factual engineering prose.

---

## Progressive Disclosure in Agent Architecture

RepoCraft respects AI agent context budgets:
- **Discovery Phase**: During repository indexing, agents only ingest the skill's lightweight YAML frontmatter (`name` and `description`). This consumes minimal context.
- **Execution Phase**: The full `SKILL.md` instructions and relevant templates are pulled into context only when a repository task is initiated.
- **Modular References**: Supporting templates and deep architectural guides remain separate from the canonical skill body, preventing unnecessary token consumption during routine tasks.
