# Inference Deployment and Service Budgets

> **Notice**: Illustrative deployment document.

## 1. Latency Budgets (SLA)

| Stage | Target p50 | Target p95 | Maximum Timeout |
| :--- | :--- | :--- | :--- |
| Query Embedding | 12 ms | 20 ms | 50 ms |
| Qdrant ANN Search | 8 ms | 15 ms | 40 ms |
| Cross-Encoder Rerank (50 items) | 35 ms | 55 ms | 100 ms |
| **Total End-to-End** | **55 ms** | **90 ms** | **200 ms** |

## 2. Model Serving Architecture

- **ONNX Runtime**: Models exported to ONNX format with float16 / INT8 quantization.
- **Hardware Target**: NVIDIA T4 / L4 GPU or c6i.4xlarge CPU with AVX-512 VNNI support.
- **Worker Concurrency**: 4 parallel ONNX execution threads per service instance.
