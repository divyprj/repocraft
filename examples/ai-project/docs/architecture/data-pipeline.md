# Data Pipeline and Chunking

> **Notice**: Illustrative data pipeline document.

## 1. Document Extraction and Cleaning

1. **Extraction**: Markdown and plain-text files parsed directly; HTML and PDF stripped of boilerplate headers, navigation menus, and footers.
2. **Metadata Attachment**: Every document retains source file path, git commit hash, document title, and last modified date.

## 2. Chunking Strategy

- **Strategy**: Recursive character splitting with markdown header awareness (`#`, `##`, `###`).
- **Target Chunk Size**: 400 tokens (~1600 characters).
- **Chunk Overlap**: 50 tokens (~200 characters) to preserve contextual boundaries across split points.
- **Deduplication**: SHA-256 hash computed for each chunk text to eliminate identical duplicate passages across versions.
