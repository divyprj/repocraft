# AI Coding Agent Governance: DocRetriever

> **Notice**: Illustrative agent governance document.

## 1. Operating Rules for Coding Agents

1. **Deterministic Seeds**: All embedding extraction, evaluation sampling, and data splits must declare explicit random seeds for reproducibility.
2. **Benchmark Verification**: Any proposed change to chunking strategy or embedding models must be validated by running `python3 scripts/evaluate.py`. No pull request may degrade MRR@10.
3. **No Unquantized Checkpoints**: Do not commit unquantized multi-gigabyte PyTorch weights to git. Weights must be stored in external artifact repositories (S3 / Hugging Face Hub).
