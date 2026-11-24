# Model Architecture Specifications

> **Notice**: Illustrative model specification document.

## 1. Dense Embedding Model

- **Base Architecture**: `BAAI/bge-large-en-v1.5`
- **Output Dimensions**: 1024
- **Context Window**: 512 tokens
- **Distance Metric**: Cosine Similarity
- **Normalization**: L2 normalized embeddings
- **Inference Quantization**: INT8 ONNX graph quantization

## 2. Cross-Encoder Reranking Model

- **Base Architecture**: `BAAI/bge-reranker-large`
- **Input Format**: `[CLS] Query [SEP] Passage [SEP]`
- **Maximum Sequence Length**: 512 tokens
- **Output**: Single scalar logit representing relevance score
- **Sigmoid Threshold**: 0.70 for high-confidence passage filtering
