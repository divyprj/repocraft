# ADR-001: Selecting PostgreSQL with Redis Caching

- **Status**: Accepted
- **Date**: 2026-11-20
- **Deciders**: Infrastructure & Backend Architecture Team

## Context and Problem Statement

PulseOps requires a data storage tier capable of handling relational cluster configurations and alert definitions alongside high-frequency telemetry reports. We evaluated pure NoSQL databases (MongoDB, DynamoDB) against relational databases with caching (PostgreSQL + Redis).

## Decision Drivers

- Strong consistency requirements for user accounts, cluster configurations, and alert thresholds.
- Need for flexible analytical queries on metric history.
- High-write throughput for incoming probe heartbeats.
- Operational simplicity and open-source licensing.

## Considered Options

1. **Option 1**: MongoDB cluster for all data.
2. **Option 2**: PostgreSQL for relational state + Redis for buffer caching and sessions.
3. **Option 3**: DynamoDB for metrics + Aurora PostgreSQL for configurations.

## Decision Outcome

Chosen option: **Option 2 (PostgreSQL + Redis)**, because PostgreSQL provides proven relational integrity, transactional guarantees, and time-series query indexing, while Redis absorbs peak write loads through stream buffering.
