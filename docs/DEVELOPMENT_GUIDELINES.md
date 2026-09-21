# Development Guidelines

## General Principles

- Keep the codebase modular and maintainable.
- Prefer simple and readable implementations.
- Avoid unnecessary abstractions.
- Avoid duplicated business logic.
- Keep responsibilities separated between frontend, backend, AI orchestration, RAG, and integrations.
- Reuse existing components and utilities where appropriate.
- Prefer incremental changes over large rewrites.

## Frontend Guidelines

Use React with TypeScript.

The frontend should be responsible for:

- Chat interface
- User interaction
- Displaying assistant responses
- Displaying citations
- Confirmation UI for consequential actions
- Loading states
- Error states

The frontend must not be responsible for enforcing security.

Do not rely on:

- Hidden UI elements
- Client-side role checks
- Client-side permission checks

as the actual authorization mechanism.

## Backend Guidelines

Use Python with FastAPI.

The backend should be responsible for:

- API endpoints
- Request validation
- Authentication integration
- Authorization
- Conversation handling
- Communication with LangChain
- Controlled access to internal APIs
- Backend error handling

Keep API route handlers thin.

AI orchestration should be implemented in dedicated modules rather than directly inside route handlers.

## LangChain Guidelines

Use LangChain for:

- Agent orchestration
- RAG
- Retrieval
- Tool calling
- LLM interaction
- Conversational context

Keep LangChain logic separate from:

- React components
- FastAPI route handlers
- Authentication implementation
- Database access
- Infrastructure configuration

Do not introduce another agent framework unless explicitly required.

## RAG Guidelines

The RAG system should:

- Retrieve relevant corporate information
- Preserve source metadata
- Preserve permission metadata
- Support citations
- Respect authorization
- Handle cases where no relevant information is found

The system should not fabricate retrieval results.

Corporate-specific answers should be based on retrieved corporate information or authorized internal-system data.

## Agent Guidelines

The agent should operate using the ASK / FIND / ACT model.

### ASK

Use RAG for corporate knowledge questions.

### FIND

Use authorized internal APIs for personalized information.

### ACT

Use authorized action tools/APIs for business operations.

The agent must not:

- Bypass authorization
- Invent tool results
- Invent corporate policies
- Invent employee information
- Claim an action succeeded without API confirmation

## Tool Guidelines

Every tool should have:

- A clear name
- A clear description
- Typed inputs
- Typed outputs
- Validation
- Authorization requirements
- Explicit error handling

Tools should perform focused operations.

For example:

```text
get_leave_balance
get_expense_status
get_it_tickets
create_it_ticket
submit_leave_request
create_expense_claim