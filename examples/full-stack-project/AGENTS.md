# AI Coding Agent Governance: PulseOps

> **Notice**: Illustrative agent governance document.

## 1. Operating Rules for Coding Agents

1. **Schema Migrations**: Never modify database models without generating a corresponding Alembic migration script in `backend/alembic/versions/`.
2. **Type Safety**: All frontend components must maintain strict TypeScript typing. Do not use `any`.
3. **API Contracts**: When backend routes change, update `docs/architecture/api-reference.md` and frontend API client types atomically.
4. **Verification**: Always run `pytest` and `npm test` before declaring tasks complete.
