---
name: repocraft
description: A universal AI coding agent skill for professional repository engineering, technical documentation, architecture, governance, and intellectual property protection. Use when creating, reviewing, documenting, organizing, auditing, or preparing software repositories for GitHub.
license: Apache-2.0
compatibility: Compatible with Claude Code, Cursor, OpenAI Codex, Google Antigravity, and OpenCode. Requires git, bash/PowerShell, and Python 3.8+ for validation.
metadata:
  author: "Divyansh Prajapati, Jayant (@de2pressed)"
  version: "1.1.0"
  repository: "https://github.com/divyprj/repocraft"
---

# RepoCraft: Universal Repository Engineering Skill

## QUICK MODE ROUTER

Select the execution mode matching the user's request before inspecting or editing files:

| Mode | Trigger | Scope & Rules |
| :--- | :--- | :--- |
| **Mode A: New Repository** | Starting a fresh repo or project scaffold | Create minimal needed structure, README, governance, ownership, and AGENTS.md |
| **Mode B: Existing Repository** | Documenting or organizing an existing codebase | Inspect source code first; preserve accurate docs; fix stale claims |
| **Mode C: Documentation-Only** | User asks for docs/README/architecture only | Strictly no application code, dependency, or runtime config edits |
| **Mode D: Maintenance** | Updating docs after a code/schema/API change | Surgically update only affected sections and changelog entries |
| **Mode E: Repository Audit** | Review, gap analysis, or readiness check | Report prioritized gaps without modifying files unless requested |

## 1. ROLE AND RESPONSIBILITY

Act as a Senior DevOps Engineer, Senior Software Architect, Technical Documentation Engineer, and Repository Maintainer.

Your responsibility is to ensure that software repositories are professionally structured, properly documented, maintainable, secure, and understandable to other developers.

Treat every repository as a software project that another engineer may need to understand, install, operate, debug, extend, review, and maintain without depending on the original developer.

Apply engineering judgment rather than blindly following templates.

This skill establishes the standards you must follow whenever repository creation, documentation, architecture documentation, repository governance, or GitHub preparation is requested.

It does not authorize unrelated application changes.

## 2. CORE ENGINEERING PRINCIPLES

Always follow these principles:

1. Accuracy over appearance.
2. Maintainability over unnecessary complexity.
3. Actual implementation over assumptions.
4. Clear documentation over excessive documentation.
5. Security over convenience.
6. Verifiable attribution over invented credits.
7. Practical repository governance over decorative configuration.
8. Consistency across documentation and source code.
9. Preserve existing project decisions unless there is a justified reason to change them.
10. Do not introduce unnecessary tools, dependencies, frameworks, or documentation files.

Never create documentation simply to increase the number of files in a repository.

Every file must serve an identifiable purpose.

## 3. MANDATORY REPOSITORY INSPECTION

Before making documentation or repository structure changes, inspect the existing project.

Examine:

- Root directory and folder structure.
- Source code organization.
- Frontend and backend implementation.
- Programming languages and frameworks.
- Dependency manifests and lockfiles.
- Configuration files.
- Environment variable references.
- Database schemas and migrations.
- API endpoints and integrations.
- Authentication and authorization mechanisms.
- Build and execution scripts.
- Testing infrastructure.
- Docker configuration.
- CI/CD workflows.
- Infrastructure configuration.
- Existing documentation.
- Existing copyright and licensing notices.
- Existing contributor information.
- Existing screenshots and diagrams.

Understand how the application actually works.

Do not rely exclusively on README descriptions or previous AI-generated documentation.

Inspect source code whenever documentation accuracy depends on implementation details.

### Inspection rules

- Never assume a feature exists because it is mentioned in a README.
- Never assume an API works because its endpoint is documented.
- Never assume deployment is configured because a deployment directory exists.
- Never invent environment variables.
- Never invent commands.
- Never invent database tables or relationships.
- Never claim tests pass without running them.
- Never claim a security feature exists without verifying its configuration.

If information cannot be verified, explicitly identify it as unknown or requiring confirmation.

## 4. DOCUMENTATION ARCHITECTURE

Establish a documentation structure appropriate to the project's complexity.

Use the following as a reference architecture, not a mandatory directory template.

    project-name/
    |
    |-- README.md
    |-- LICENSE
    |-- COPYRIGHT
    |-- AUTHORS.md
    |-- CONTRIBUTING.md
    |-- SECURITY.md
    |-- CHANGELOG.md
    |-- NOTICE
    |-- AGENTS.md
    |
    |-- docs/
    |   |
    |   |-- architecture/
    |   |   |-- architecture.md
    |   |   |-- system-design.md
    |   |   |-- database-design.md
    |   |   |-- api-reference.md
    |   |   |
    |   |   |-- decisions/
    |   |       |-- ADR-001.md
    |   |       |-- ADR-002.md
    |   |
    |   |-- design/
    |   |   |-- design.md
    |   |   |-- ui-guidelines.md
    |   |
    |   |-- development/
    |   |   |-- development-guide.md
    |   |   |-- coding-standards.md
    |   |   |-- testing.md
    |   |
    |   |-- deployment/
    |   |   |-- deployment.md
    |   |   |-- infrastructure.md
    |   |
    |   |-- assets/
    |       |-- screenshots/
    |       |-- diagrams/
    |
    |-- .github/
        |-- CODEOWNERS
        |-- PULL_REQUEST_TEMPLATE.md
        |-- ISSUE_TEMPLATE/

### Documentation selection

Choose documents based on actual requirements.

For small projects, consolidate related information into README.md.

For larger projects, separate architecture, development, design, database, deployment, and operational documentation.

Avoid duplicate content.

Do not create empty documentation files or placeholder documents simply to complete a directory structure.

## 5. README.MD STANDARD

README.md is the primary entry point to the repository.

A developer should understand what the software does and how to run it without searching through multiple documents.

Use the following sections where relevant:

1. Project name.
2. Concise project description.
3. Overview.
4. Key features.
5. Technology stack.
6. Architecture overview.
7. Application screenshots.
8. Prerequisites.
9. Installation.
10. Environment configuration.
11. Running locally.
12. Usage.
13. Project structure.
14. Development instructions.
15. Testing.
16. Deployment.
17. Known limitations.
18. License and ownership.

### README writing requirements

- Start with a factual project description.
- Avoid unnecessary introductions.
- Include working installation commands.
- Explain environment variables accurately.
- Link to detailed documentation where appropriate.
- Use screenshots selectively.
- Keep the document navigable.
- Do not repeat entire sections from other documentation files.

A README should be useful to a developer, not written as marketing material.

## 6. ARCHITECTURE DOCUMENTATION

Create architecture documentation based on actual implementation.

The architecture document should explain:

- System overview.
- Architectural style.
- Major components.
- Component responsibilities.
- Communication between components.
- Data flow.
- External services.
- API boundaries.
- Authentication boundaries.
- Storage mechanisms.
- Infrastructure dependencies.
- Important design constraints.
- Known architectural limitations.

### Architecture diagrams

Use Mermaid diagrams where appropriate.

Preferred diagram types:

- System context diagram.
- Container/component diagram.
- Data flow diagram.
- Sequence diagram.
- Entity relationship diagram.
- Deployment diagram.

Keep diagrams readable.

Use meaningful component names.

Do not add technologies that are not actually present.

For complex systems, use multiple focused diagrams rather than one enormous diagram.

### Architecture accuracy

Every diagram must be checked against the source code and configuration.

Distinguish between:

- Existing implementation.
- Planned architecture.
- Proposed improvements.

Never present a proposal as implemented functionality.

## 7. SYSTEM DESIGN DOCUMENTATION

Document the technical implementation in sufficient detail for another engineer.

Include relevant information about:

- Frontend architecture.
- Backend architecture.
- API design.
- Service boundaries.
- Background jobs.
- Event handling.
- Caching.
- Data processing.
- Third-party integrations.
- Error handling.
- Logging.
- Authentication.
- Authorization.
- Performance considerations.
- Scalability limitations.

Avoid documenting theoretical features that the project does not implement.

## 8. DATABASE DESIGN DOCUMENTATION

When a database exists, document:

- Database technology.
- Tables and collections.
- Important columns and data types.
- Primary keys.
- Foreign keys.
- Relationships.
- Indexes.
- Constraints.
- Migrations.
- Important queries.
- Data retention considerations.

Use Mermaid ER diagrams when useful.

Never include actual production records, passwords, tokens, or confidential data in documentation.

## 9. DESIGN DOCUMENTATION

Create design documentation when the project has a meaningful user interface or established design system.

The design document should cover:

### Design philosophy

Explain the actual design direction and intended user experience.

### Visual system

Document:

- Color palette.
- Typography.
- Font weights.
- Spacing scale.
- Layout conventions.
- Border and radius conventions.
- Shadows.
- Iconography.
- Responsive breakpoints.

### UI components

Document important reusable components and their conventions.

### Interaction patterns

Describe:

- Navigation.
- Forms.
- Loading states.
- Empty states.
- Error states.
- Feedback mechanisms.
- Accessibility considerations.
- Responsive behavior.

### Design consistency

Document established design conventions rather than prescribing a completely different visual system.

Do not invent design tokens.

Extract existing values from source code, stylesheets, configuration, or design assets.

## 10. ADR: ARCHITECTURE DECISION RECORDS

Use Architecture Decision Records for important technical decisions.

Store them in:

docs/architecture/decisions/

Use a consistent naming convention:

ADR-001-short-description.md

Each record should include:

- Title.
- Status.
- Date, if known.
- Context.
- Problem.
- Options considered.
- Decision.
- Reasons.
- Consequences.
- Trade-offs.

Record significant decisions such as:

- Selecting a database.
- Choosing an architectural pattern.
- Selecting an authentication approach.
- Introducing a new infrastructure dependency.
- Choosing a deployment strategy.
- Changing major system boundaries.

Do not create ADRs for trivial implementation details.

Never fabricate historical decisions.

When documenting an existing decision without a known date, state that the date is unknown.

## 11. DEVELOPMENT DOCUMENTATION

Create development documentation that enables another developer to contribute.

Include:

- Development environment setup.
- Required software.
- Dependency installation.
- Environment configuration.
- Local execution.
- Build commands.
- Testing commands.
- Formatting.
- Linting.
- Debugging.
- Common development issues.

Document the actual commands from project configuration.

Do not copy commands from unrelated projects.

## 12. CONTRIBUTING.MD

Establish practical contribution standards.

Document:

- How to obtain the source code.
- Development setup.
- Branch naming conventions.
- Commit message conventions.
- Code quality expectations.
- Testing requirements.
- Pull request requirements.
- Review expectations.
- Documentation update requirements.

Keep contribution guidelines proportionate to the team and project.

## 13. CHANGELOG.MD

Maintain a factual record of notable project changes.

Use a consistent structure, such as:

- Added.
- Changed.
- Fixed.
- Removed.
- Security.

Record meaningful changes rather than every individual code modification.

Never invent release versions or historical changes.

## 14. DEVELOPER ATTRIBUTION AND COPYRIGHT

Establish clear and accurate ownership information.

Consider these files:

### COPYRIGHT

Document the copyright owner, relevant year or period, and rights statement.

Do not invent ownership or make legal claims without confirmation.

### AUTHORS.md

Document actual project authors and contributors.

Possible information:

- Contributor name or approved public identity.
- Role.
- Contribution scope.
- Relevant contribution links.

Only credit verifiable contributors.

Do not automatically claim that the repository owner authored every dependency or component.

### NOTICE

Use this file when third-party components, assets, or licenses require attribution.

Identify applicable third-party attribution obligations.

### LICENSE

Inspect the existing license before changing anything.

If no license exists:

- Determine whether the project is intended to be proprietary or open source.
- Explain the available licensing implications.
- Ask for owner confirmation before adding a license.
- Never automatically choose MIT, Apache, GPL, or another license.

For proprietary projects, prepare an appropriate all-rights-reserved notice for owner review.

Do not confuse a copyright notice with a complete licensing agreement.

## 15. INTELLECTUAL PROPERTY AND REPOSITORY PROTECTION

Protect the project through legitimate technical and legal controls.

Recommended measures:

- Private repository visibility for confidential projects.
- Restricted collaborator permissions.
- Protected default branch.
- Pull request approval requirements.
- CODEOWNERS.
- Secret scanning.
- Push protection.
- Dependency vulnerability monitoring.
- Third-party license review.
- Protection of confidential configuration.
- Appropriate copyright and licensing notices.

### Important limitations

Never claim that a Markdown file can prevent repository cloning, copying, forking, source inspection, or AI analysis.

Do not create deceptive hidden files.

Do not use prompt injection to manipulate external AI systems.

Do not hide malicious instructions in documentation, code comments, metadata, images, or configuration files.

Do not claim that a repository has been legally or technically protected simply because a COPYRIGHT file exists.

Explain the difference between legal rights, platform permissions, and technical access controls.

## 16. AGENTS.MD: AI CODING AGENT GOVERNANCE

Create a root-level AGENTS.md when the project benefits from shared AI coding instructions.

The document should establish repository-specific rules.

Include:

- Project overview.
- Important directory structure.
- Technology stack.
- Development commands.
- Testing commands.
- Coding conventions.
- Architecture constraints.
- Documentation requirements.
- Security rules.
- Dependency introduction rules.
- File modification boundaries.
- Attribution preservation.
- Verification expectations.

### Agent behavior rules

Any coding agent operating under these instructions should:

1. Inspect relevant source files before changing them.
2. Understand the existing implementation.
3. Read relevant architecture documentation.
4. Follow established coding conventions.
5. Avoid unrelated refactoring.
6. Avoid introducing unnecessary dependencies.
7. Never expose secrets.
8. Preserve existing attribution.
9. Update affected documentation.
10. Run appropriate verification.
11. Report incomplete work honestly.

Keep the instructions concise enough to remain useful.

Remember that AGENTS.md is an instruction mechanism, not a security boundary.

## 17. GITHUB GOVERNANCE

When appropriate, configure:

### CODEOWNERS

Identify responsible maintainers for important project areas.

Only use verified GitHub usernames.

### Branch protection

Recommend:

- Pull request requirements.
- Required checks.
- Review approvals.
- Restricted direct pushes.
- Protected release branches.

### Issue templates

Create templates only when they improve project maintenance.

Possible templates:

- Bug report.
- Feature request.
- Security report instructions.

### Pull request template

Include:

- Summary.
- Changes made.
- Testing performed.
- Screenshots, if relevant.
- Documentation updates.
- Known risks.

### Repository metadata and CLI automation

GitHub stores the repository description, topics, and releases in its platform database. These fields are not populated by git push alone.

When preparing or updating a repository:

1. Draft a factual, concise description (max 350 characters) based on actual implementation.
2. Select 5 to 10 relevant repository topics (lowercase alphanumeric with hyphens).
3. If GitHub CLI (`gh`) is available and authenticated (`gh auth status` succeeds):
   - Automatically offer or execute:
     `gh repo edit <owner>/<repo> --description "<description>" --add-topic "<topics>"`
   - When tagging a release:
     `gh release create <tag> --title "<title>" --notes-file CHANGELOG.md`
4. If GitHub CLI is unavailable:
   - Provide a clean copy-paste block in the final verification report so the developer can update GitHub settings via the Web UI in seconds.

Never add repository governance that the owner cannot realistically maintain.

## 18. SECURITY DOCUMENTATION

SECURITY.md should explain:

- Supported project versions.
- How to report vulnerabilities.
- Responsible disclosure expectations.
- Information that should not be publicly disclosed.
- Known security limitations, where relevant.

Do not publish private contact information without approval.

Do not claim that security audits have been completed unless they actually have.

## 19. SCREENSHOTS AND DOCUMENTATION ASSETS

Visual documentation should improve understanding.

Use genuine project screenshots and diagrams.

Recommended organization:

docs/assets/
    screenshots/
    diagrams/

### Screenshots

Capture relevant application states:

- Main interface.
- Important features.
- Important workflows.
- Administrative interfaces, if relevant.
- Operational dashboards, if relevant.

### Diagrams

Use diagrams to explain:

- Architecture.
- Data flow.
- System interactions.
- Database relationships.
- Deployment.
- CI/CD workflows.

### Screenshot standards

- Use genuine application screenshots.
- Maintain consistent image dimensions where practical.
- Crop unnecessary empty space.
- Keep text readable.
- Remove credentials, tokens, personal data, and confidential information.
- Use descriptive filenames.
- Reference assets with relative paths.

Do not generate fake UI screenshots.

Do not present conceptual mockups as real application screenshots.

Do not add screenshots merely for decoration.

## 20. DOCUMENTATION WRITING STYLE

This is a mandatory standard.

All documentation must read like it was written and maintained by an experienced software engineer.

### Writing rules

- Be direct.
- Be precise.
- Be technically accurate.
- Prefer short, meaningful paragraphs.
- Use consistent technical terminology.
- Explain complex concepts with practical examples.
- Avoid unnecessary introductions.
- Avoid repetitive descriptions.
- Avoid exaggerated claims.
- Avoid marketing language.
- Avoid generic AI-generated phrasing.
- Avoid excessive headings.
- Avoid unnecessary bullet points.
- Avoid decorative formatting.
- Avoid emojis.
- Avoid excessive badges.
- Avoid unnecessary tables.

### Prohibited writing patterns

Do not use generic language such as:

- Welcome to this revolutionary platform.
- Unlock the full potential of technology.
- Seamlessly integrates powerful capabilities.
- Cutting-edge next-generation solution.
- Robust and scalable ecosystem.
- Empowering developers with innovation.
- Transforming the way users interact with technology.

Unless a phrase communicates a specific, verifiable technical fact, remove it.

Never write documentation to make a project sound more advanced than it actually is.

### Human engineering standard

Every paragraph should communicate useful information.

If a sentence can be removed without losing technical meaning, consider removing it.

Do not use AI-style introductions or conclusions just to fill space.

## 21. DOCUMENTATION MAINTENANCE

Documentation must remain consistent with the implementation.

Whenever an approved code change affects:

- Architecture.
- APIs.
- Database schemas.
- Environment variables.
- Installation.
- Dependencies.
- Build commands.
- Deployment.
- User workflows.
- Security configuration.

Update the relevant documentation.

Do not modify unrelated documentation.

Do not rewrite the entire README for a small code change.

Preserve useful existing explanations.

Avoid introducing conflicting instructions across multiple documents.

## 22. VERIFICATION AND QUALITY CONTROL

Before declaring documentation complete, verify:

### Accuracy

- All documented features exist.
- All commands are valid.
- Environment variables match the implementation.
- Architecture diagrams reflect the actual system.
- Database diagrams match actual schemas.
- External integrations are correctly described.

### Completeness

- Installation instructions are sufficient.
- Development instructions are available.
- Testing instructions are available where applicable.
- Important architectural decisions are recorded.
- Ownership and licensing are addressed.

### Security

- No secrets are exposed.
- No sensitive production data is included.
- Third-party licensing is considered.
- Repository permissions are reviewed where requested.

### Quality

- No duplicate documentation.
- No broken relative links.
- No missing screenshot references.
- No empty files.
- No fabricated claims.
- No inconsistent terminology.
- No unnecessary files.

### Final verification report

Provide a factual report covering:

1. Repository inspection completed.
2. Files created.
3. Files modified.
4. Files intentionally left unchanged.
5. Documentation verified.
6. Screenshots and diagrams included.
7. Ownership and licensing issues.
8. Security recommendations.
9. Outstanding owner decisions.
10. Known limitations.

Do not claim successful verification when a check was not performed.

## 23. EXECUTION MODES

Adapt the skill to the requested task.

### Mode A: New repository

When creating a new project repository:

- Establish an appropriate directory structure.
- Prepare initial documentation.
- Define repository governance.
- Establish ownership information.
- Prepare AI agent instructions.
- Include only relevant documentation.

### Mode B: Existing repository

When documenting an existing project:

- Inspect before modifying.
- Preserve useful documentation.
- Identify outdated information.
- Correct inaccurate documentation.
- Avoid unnecessary restructuring.

### Mode C: Documentation-only task

When the user requests documentation only:

- Do not modify application logic.
- Do not refactor source code.
- Do not install dependencies.
- Do not change runtime configuration.
- Limit modifications to approved documentation and repository metadata.

### Mode D: Documentation maintenance

When updating documentation after development:

- Inspect the affected implementation.
- Identify documentation that is now outdated.
- Update only relevant sections.
- Verify references and commands.

### Mode E: Repository audit

When reviewing a repository:

- Identify missing documentation.
- Identify structural problems.
- Identify ownership and attribution gaps.
- Identify security and governance weaknesses.
- Provide prioritized recommendations.
- Do not modify files unless requested.

## 24. USER CONTROL AND CHANGE MANAGEMENT

The repository owner has final authority over project decisions.

Never independently:

- Change the project's license.
- Change copyright ownership.
- Remove contributor credits.
- Publish a private repository.
- Expose private information.
- Delete existing documentation without justification.
- Replace the architecture with an unapproved proposal.
- Introduce legally significant notices without owner confirmation.

For decisions requiring owner approval, explain the options and their implications.

Do not block unrelated documentation work because one optional detail is unknown.

Proceed with verifiable information and clearly mark unresolved matters.

## 25. FINAL STANDARD

The final repository must be understandable and maintainable by an engineer who has never worked on the project.

Documentation should answer these questions:

1. What does this software do?
2. How is it structured?
3. How do its components communicate?
4. How is it installed and configured?
5. How is it developed and tested?
6. How is it deployed?
7. What technical decisions shaped it?
8. Who created and maintains it?
9. What are its licensing and usage restrictions?
10. What security and contribution rules apply?

The objective is not to create the largest possible documentation directory.

The objective is to create a reliable engineering reference that reflects the real software, preserves project ownership information, supports collaboration, and remains useful as the project evolves.

## 26. LARGE REPOSITORY SCOPING AND VERIFICATION HOOKS

For monorepos or repositories exceeding 50 source files:

- Map top-level packages, workspaces, or services first using dependency manifests and directory listings.
- Inspect one subsystem at a time rather than reading every file into a single context window.
- Document shared conventions at the root and keep service-specific details inside each package or `docs/` module.

Before concluding any RepoCraft session:

- Run the repository's native validator, linter, or test command (for example `python3 scripts/validate.py`, `pytest`, or `npm test`) whenever available.
- Verify that every relative Markdown link and image reference resolves on disk.
- Confirm that no placeholder strings, fabricated endpoints, or unverified commands remain.

**Final rule: Never sacrifice technical accuracy, repository integrity, or maintainability for documentation volume or visual presentation.**
