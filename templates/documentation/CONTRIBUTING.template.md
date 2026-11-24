# Contributing to Project Name

Thank you for your interest in contributing. Please review the following standards before opening a pull request.

## Development Setup

1. Fork and clone the repository.
2. Install dependencies:
   ```bash
   # Add setup commands here
   npm install
   ```
3. Copy environment configuration:
   ```bash
   cp .env.example .env
   ```

## Commit and Branching Conventions

- Use feature branches branched from `main`: `feat/short-description` or `fix/issue-description`.
- Follow Conventional Commits:
  - `feat: add user session revocation`
  - `fix: handle database reconnection on socket timeout`
  - `docs: update deployment environment variables`

## Testing Standards

- All new code must be accompanied by relevant unit or integration tests.
- Verify that the full test suite passes before submitting:
  ```bash
  npm test
  ```

## Pull Request Checklist

- [ ] Code follows project linting and formatting conventions.
- [ ] Tests pass locally.
- [ ] Documentation has been updated to reflect any API, schema, or configuration changes.
- [ ] No secrets or sensitive configuration are included in the diff.
