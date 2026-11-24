# PulseOps System Design

> **Notice**: Illustrative system design document.

## 1. Subsystem Decomposition

### Ingestion Pipeline
The telemetry ingestion subsystem receives heartbeat packets from agents running across monitored nodes. To maintain high availability during peak traffic spikes:
- Packets are validated in memory using Pydantic models.
- Validated metrics are buffered in a Redis stream.
- A batch worker flushes accumulated stream entries into PostgreSQL every 5 seconds or upon reaching 500 entries.

### Alert Evaluation Engine
- Runs as an asynchronous loop inside the FastAPI core service.
- Evaluates incoming metric thresholds against user-defined alert rules.
- If a rule breaches its threshold for 3 consecutive evaluation cycles, an alert event is published to Redis Pub/Sub.

## 2. Caching and State Management

- **Cluster Health Status**: Cached in Redis with a 10-second TTL to avoid redundant SQL queries on active dashboards.
- **User Sessions**: Revocable JWT tokens paired with Redis session keys.
