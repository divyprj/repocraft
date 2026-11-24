# System Architecture

## 1. Overview and Style

Describe the overarching architectural pattern (e.g. Clean Architecture, Hexagonal, Modular Monolith, Microservices) and the design goals.

## 2. Component Diagram

```mermaid
graph TD
    Client[Web / Mobile Client] -->|HTTPS/REST| Gateway[API Gateway]
    Gateway -->|gRPC / Internal HTTP| AuthService[Auth Service]
    Gateway -->|gRPC / Internal HTTP| CoreService[Core Business Service]
    CoreService -->|SQL| Database[(Relational Database)]
    CoreService -->|Pub/Sub| MessageBroker[Message Broker]
    MessageBroker -->|Consume| Worker[Async Task Worker]
```

## 3. Core Components

### API Gateway / Router
- **Role**: Request routing, rate limiting, SSL termination, and CORS enforcement.
- **Protocols**: HTTPS, WebSocket.

### Core Service
- **Role**: Domain business logic, transaction boundaries, and entity management.
- **Dependencies**: Relational database, cache layer.

### Background Worker
- **Role**: Asynchronous execution of long-running tasks, email dispatch, and reports.

## 4. Data Flow

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Gateway as API Gateway
    participant Service as Core Service
    participant DB as Database

    User->>Gateway: POST /api/v1/resource (payload)
    Gateway->>Service: Forward request with validated JWT
    Service->>DB: INSERT into resources
    DB-->>Service: Return row ID and created_at
    Service-->>Gateway: HTTP 201 Created (JSON)
    Gateway-->>User: HTTP 201 Created
```

## 5. Security and Network Boundaries

- Describe authentication boundaries (JWT validation, session tokens).
- Describe internal service networks vs public-facing interfaces.
- Specify transport encryption (TLS 1.3) and storage encryption at rest.

## 6. Known Constraints and Trade-offs

- Document known scale limits, latency characteristics, or single points of failure.
