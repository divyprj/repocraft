# Evaluation Methodology and Benchmarks

> **Notice**: Illustrative evaluation document.

## 1. Primary Metrics

- **MRR@10 (Mean Reciprocal Rank)**: Measures how early the first truly relevant documentation passage appears.
- **NDCG@10 (Normalized Discounted Cumulative Gain)**: Evaluates graded relevance ranking quality across top-10 retrieved chunks.
- **Recall@50**: Measures candidate coverage from first-stage retrieval feeding the reranker.

## 2. Benchmark Datasets

- **TechQA-v1**: 1,200 curated questions paired with technical manuals and verified ground-truth answer passages.
- **Synthetic Hard Negatives**: Generated via lexical BM25 high-overlap distractors.

## 3. Baseline vs Current Results

| Pipeline Configuration | MRR@10 | NDCG@10 | Recall@50 | p95 Latency |
| :--- | :--- | :--- | :--- | :--- |
| Lexical BM25 Only | 0.582 | 0.621 | 0.745 | 18 ms |
| Dense Bi-Encoder Only | 0.741 | 0.772 | 0.912 | 24 ms |
| Dense + Cross-Encoder Rerank | **0.864** | **0.889** | **0.912** | **68 ms** |
