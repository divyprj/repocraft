# PulseOps Database Design

> **Notice**: Illustrative database design document.

## 1. Engine and Extensions

- **Database Engine**: PostgreSQL 16
- **Extensions**: `uuid-ossp` (UUID generation), `btree_gist` (indexing constraints)
- **Migrations**: Managed via Alembic under `backend/alembic/`

## 2. Entity Relationship Diagram

```mermaid
erDiagram
    CLUSTERS ||--o{ NODES : contains
    CLUSTERS {
        uuid id PK
        string name UK
        string environment
        timestamp created_at
    }
    NODES ||--o{ METRICS : emits
    NODES {
        uuid id PK
        uuid cluster_id FK
        string hostname
        string ip_address
        string status
        timestamp last_seen
    }
    METRICS {
        uuid id PK
        uuid node_id FK
        float cpu_percent
        float memory_percent
        float disk_percent
        timestamp recorded_at
    }
    CLUSTERS ||--o{ ALERT_RULES : defines
    ALERT_RULES {
        uuid id PK
        uuid cluster_id FK
        string metric_name
        float threshold
        string severity
    }
```

## 3. Important Indexes

- `idx_nodes_cluster_id`: BTREE on `nodes(cluster_id)`
- `idx_metrics_node_recorded`: BTREE on `metrics(node_id, recorded_at DESC)`
- `idx_alert_rules_cluster`: BTREE on `alert_rules(cluster_id)`
