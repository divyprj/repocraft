# PulseOps API Reference

> **Notice**: Illustrative API reference specification.

Base URL: `http://localhost:8000/api/v1`

## Authentication

All endpoints except `/health` require a Bearer token:
```http
Authorization: Bearer <access_token>
```

---

## Endpoints

### 1. Ingest Telemetry

`POST /telemetry/heartbeat`

Submit a heartbeat metric report from a cluster probe.

#### Request Body
```json
{
  "node_id": "7b8d80f8-c923-424d-842b-586b51c1102e",
  "cpu_percent": 42.5,
  "memory_percent": 68.1,
  "disk_percent": 54.0,
  "recorded_at": "2026-11-24T12:00:00Z"
}
```

#### Response (`202 Accepted`)
```json
{
  "status": "queued",
  "receipt_id": "rcpt_98213812"
}
```

---

### 2. List Active Alerts

`GET /alerts/active`

Retrieve all currently firing alerts across monitored clusters.

#### Response (`200 OK`)
```json
{
  "alerts": [
    {
      "id": "alt_192831",
      "cluster_name": "prod-us-east-1",
      "node_hostname": "worker-04",
      "severity": "critical",
      "message": "Memory usage exceeded 90% for 3 cycles",
      "triggered_at": "2026-11-24T11:58:30Z"
    }
  ]
}
```
