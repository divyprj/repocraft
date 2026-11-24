# API Reference

Base URL: `https://api.example.com/v1` (or `http://localhost:8000/v1`)

## Authentication

All protected endpoints require a Bearer token:
```http
Authorization: Bearer <jwt-token>
```

---

## Endpoints

### 1. Health Check

`GET /health`

Returns service availability and subsystem ping status.

#### Response
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "database": "connected"
}
```

---

### 2. List Items

`GET /items`

Retrieve a paginated list of items.

#### Query Parameters
- `limit` (integer, optional, default: 20): Number of records to return (max: 100).
- `cursor` (string, optional): Pagination cursor for keyset traversal.

#### Response (`200 OK`)
```json
{
  "items": [
    {
      "id": "e3a89a8e-5b12-4f32-841c-b695e2df9d32",
      "name": "Sample Item",
      "created_at": "2026-11-24T12:00:00Z"
    }
  ],
  "next_cursor": "eyJpZCI6ICJlM2E4OWE4ZS01YjEyLTRmMzItODQxYy1iNjk1ZTJkZjlkMzIifQ=="
}
```

---

### 3. Create Item

`POST /items`

Create a new item.

#### Request Body
```json
{
  "name": "New Resource Name"
}
```

#### Response (`201 Created`)
```json
{
  "id": "d1b54a9c-2f31-4c21-987a-a123e456f789",
  "name": "New Resource Name",
  "created_at": "2026-11-24T12:05:00Z"
}
```
