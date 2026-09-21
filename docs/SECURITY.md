# Security

## Security Objective

The Enterprise Knowledge & Task Assistant handles corporate and potentially sensitive employee information.

Security must therefore be enforced at the application and infrastructure level and must not depend solely on the LLM's instructions.

## Authentication

Use Microsoft Entra ID for employee authentication.

The authenticated identity should be available to the backend so that the system can determine which resources and operations the employee is authorized to access.

## Authorization

The system must support role-based authorization.

Example access model:

| Role | Authorized Access |
|---|---|
| Employee | HR policies, IT policies |
| Manager | HR policies, authorized team information |
| HR Admin | HR policies, authorized employee records |

Examples of restricted information:

- Confidential executive salary data
- Confidential HR records
- Employee information belonging to users without the required permissions

Authorization must be enforced by the backend and relevant services.

The LLM must never be treated as the authorization layer.

## Permission-Aware Retrieval

The RAG system must retrieve only information that the authenticated employee is permitted to access.

The retrieval layer should support appropriate mechanisms such as:

- Document-level permissions
- Metadata filtering
- Permission-aware search
- Backend authorization checks

A document being present in the search index does not automatically mean every employee can retrieve it.

## Internal API Security

Internal business APIs must only be accessed through controlled backend integrations.

The frontend must never contain privileged service credentials.

Every protected operation must verify that the authenticated user is authorized to perform the requested operation.

## Tool Security

Each LangChain tool should define:

- Required permissions
- Accepted inputs
- Expected outputs
- Allowed operations
- Error behavior

The agent must not be allowed to arbitrarily access internal systems.

Only explicitly configured and authorized tools should be available to the agent.

## Sensitive and Consequential Actions

Actions that change enterprise data or create requests may require confirmation before execution.

Examples include:

- Creating an IT ticket
- Submitting a leave request
- Creating an expense claim
- Raising an HR request
- Requesting a new laptop

The confirmation should clearly describe the intended action before execution.

## Example Confirmation

```text
The following IT ticket will be created:

Issue:
Laptop cannot connect to Wi-Fi.

Do you want to proceed?