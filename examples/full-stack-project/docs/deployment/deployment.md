# PulseOps Deployment Guide

> **Notice**: Illustrative deployment documentation.

## 1. Container Architecture

PulseOps is containerized using multi-stage Docker builds:
- `backend.Dockerfile`: Python 3.12 slim image with non-root user execution (`uid 10001`).
- `frontend.Dockerfile`: Node.js 20 Alpine standalone output build.

## 2. Docker Compose Deployment

To run a production-like staging environment locally:

```bash
docker compose -f docker-compose.prod.yml up -d
```

## 3. Environment Variables Reference

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATABASE_URL` | PostgreSQL asyncpg connection string | None |
| `REDIS_URL` | Redis connection URL | `redis://redis:6379/0` |
| `SECRET_KEY` | 32-byte hexadecimal JWT signing secret | None |
| `CORS_ORIGINS` | Comma-separated list of allowed frontend origins | `http://localhost:3000` |
