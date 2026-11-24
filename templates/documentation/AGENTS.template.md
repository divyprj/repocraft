# AI Coding Agent Governance

This document establishes operational instructions for AI coding agents working inside this repository.

## 1. Project Overview

Brief description of the project, core language, framework, and architectural style.

## 2. Directory Structure

```text
src/         # Core application logic
tests/       # Automated test suite
docs/        # Architecture and design documentation
```

## 3. Mandatory Agent Rules

1. **Inspect Before Modifying**: Inspect existing source files, database models, and route definitions before proposing or making changes.
2. **Follow Established Conventions**: Match code styling, error handling patterns, and typing conventions used across the project.
3. **No Unnecessary Refactoring**: Only modify files relevant to the active prompt. Do not reformat unrelated files.
4. **Preserve Attribution**: Do not remove copyright headers, contributor credits, or license references.
5. **Update Documentation**: When code modifications alter APIs, schemas, or environment variables, update the corresponding documentation atomically.
6. **Execute Verification**: Always run the relevant test suite before reporting completion.
