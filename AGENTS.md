# AI Coding Agent Instructions

## Project

This repository contains an AI-powered Corporate Knowledge & Task Assistant.

The assistant provides three core capabilities:

- ASK: Answer questions using authorized corporate knowledge.
- FIND: Retrieve authorized personalized information from internal systems.
- ACT: Perform authorized business tasks through internal systems.

The project uses React, FastAPI, LangChain, and Microsoft Azure AI services.

## Project Documentation

Before making significant changes, read the relevant documentation in:

- `docs/PROJECT_OVERVIEW.md`
- `docs/REQUIREMENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/TECH_STACK.md`
- `docs/RAG_DESIGN.md`
- `docs/AGENT_DESIGN.md`
- `docs/SECURITY.md`
- `docs/TOOLS_AND_INTEGRATIONS.md`
- `docs/DEVELOPMENT_GUIDELINES.md`

These documents describe the intended product behavior and architecture.

## Core Architecture

The intended architecture is:

React Frontend
→ FastAPI Backend
→ LangChain AI Orchestration
→ Azure AI Search / Internal APIs
→ Microsoft Foundry / Azure OpenAI
→ Grounded or authorized response

Do not replace this architecture with a different framework or architecture unless explicitly instructed.

## Development Rules

1. Understand the existing project structure before modifying code.
2. Follow the documented architecture and requirements.
3. Use React + TypeScript for the frontend.
4. Use Python + FastAPI for the backend.
5. Use LangChain for AI orchestration, RAG, and tool calling.
6. Use the documented Azure services for enterprise AI functionality.
7. Do not introduce unnecessary frameworks, libraries, or cloud services.
8. Keep frontend, backend, AI orchestration, retrieval, and integrations modular.
9. Prefer small, focused changes over large rewrites.
10. Reuse existing components and utilities where appropriate.
11. Do not duplicate business logic.
12. Keep configuration separate from application code.
13. Never hardcode secrets, API keys, tokens, passwords, or connection credentials.
14. Use environment variables or appropriate secret-management mechanisms for sensitive configuration.

## AI Rules

1. Corporate-specific answers must be grounded in retrieved corporate information or authorized internal system data.
2. Do not invent company policies, procedures, figures, employee information, or API results.
3. If sufficient information cannot be found, explicitly state that the information is unavailable.
4. Do not claim that an action succeeded unless the relevant internal API confirms success.
5. Do not fabricate ticket IDs, request IDs, balances, statuses, or other system results.
6. Use RAG for corporate knowledge questions.
7. Use authorized internal APIs for personalized, live information.
8. Use controlled tools/APIs for business actions.
9. Preserve the user's authorization context during retrieval and tool execution.

## Security Rules

1. Authentication should use Microsoft Entra ID.
2. Authorization must be enforced server-side.
3. Never rely on the LLM or frontend alone for authorization.
4. Retrieval must respect the user's permissions.
5. Internal APIs must only be accessed when the user is authorized.
6. Do not expose privileged credentials to the frontend.
7. Sensitive or consequential actions must follow the documented confirmation flow.
8. Do not expose information that the authenticated user is not authorized to access.

## Change Management

Before making a significant architectural change:

1. Check the relevant documentation.
2. Identify why the existing design is insufficient.
3. Explain the proposed change.
4. Update the relevant documentation.
5. Implement the smallest appropriate change.
6. Add or update tests.

Do not silently change major architectural decisions.

## Code Quality

- Keep functions and modules focused.
- Prefer readable code over clever code.
- Use meaningful names.
- Add appropriate error handling.
- Validate external input.
- Keep API routes thin.
- Keep AI orchestration separate from HTTP route handling.
- Keep tool integrations isolated and testable.
- Add tests for non-trivial functionality.

## When Requirements Are Ambiguous

Do not invent major product behavior.

First inspect:

1. Existing code
2. Project documentation
3. Related configuration
4. Existing interfaces and contracts

If the ambiguity materially affects architecture or user behavior, ask for clarification before implementing it.

## Source of Truth

The project documentation under `docs/` represents the intended product requirements and architecture.

Existing code represents the current implementation.

When the documentation and implementation differ, do not blindly rewrite the project. Identify the difference and make the smallest change necessary to satisfy the current requirements.