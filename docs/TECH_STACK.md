# Technology Stack

## Frontend

- React
- TypeScript

The frontend is responsible for the employee-facing conversational interface, including chat, citations, action confirmations, loading states, and error states.

## Backend

- Python
- FastAPI

FastAPI provides the application API layer, request handling, authentication/authorization integration, conversation handling, and communication with the AI orchestration layer.

## AI Orchestration

- LangChain

LangChain is responsible for:

- Agent orchestration
- RAG pipelines
- Retrieval
- Tool calling
- LLM interaction
- Conversational context
- Routing between ASK, FIND, and ACT capabilities

## AI Platform

- Microsoft Foundry

Microsoft Foundry provides the Microsoft AI platform used by the project.

## LLM

- Azure OpenAI

The application uses an Azure OpenAI model for natural-language understanding and response generation.

The specific model deployment must be configurable and must not be hardcoded throughout the application.

## RAG

- Retrieval-Augmented Generation (RAG)

RAG is used to ground corporate knowledge responses in private organizational documents.

## Search

- Azure AI Search

Azure AI Search is used for corporate knowledge retrieval.

The search architecture should support:

- Keyword search
- Vector search
- Hybrid search
- Semantic ranking
- Metadata filtering
- Permission-aware retrieval

## Document Storage

- Azure Blob Storage

Azure Blob Storage is used to store corporate source documents before they are processed and indexed for retrieval.

## Authentication

- Microsoft Entra ID

Microsoft Entra ID is used for employee authentication and identity-aware authorization.

## Database

- PostgreSQL

PostgreSQL may be used for application-level data such as:

- Conversation metadata
- User/application metadata
- Application state
- Other persistent data required by the backend

Corporate documents should remain in the dedicated document-storage/search pipeline rather than being treated as ordinary application records.

## Internal Business APIs

Internal APIs provide access to live enterprise information and business operations.

Potential systems include:

- HR
- IT service management
- Finance
- Project/business systems

These integrations support the FIND and ACT capabilities.

## Deployment

- Microsoft Azure

Azure is the target cloud environment for the project's AI and supporting infrastructure.

## Technology Boundaries

### React

Responsible for the user interface.

### FastAPI

Responsible for the backend/API layer.

### LangChain

Responsible for AI orchestration, RAG, agent behavior, and tool calling.

### Microsoft Foundry / Azure OpenAI

Responsible for model and AI platform capabilities.

### Azure AI Search

Responsible for enterprise knowledge retrieval.

### Azure Blob Storage

Responsible for source document storage.

### Microsoft Entra ID

Responsible for authentication and identity.

### PostgreSQL

Responsible for application persistence.

### Internal APIs

Responsible for live enterprise data and business actions.

## Technology Decision Rules

1. React + TypeScript is the frontend stack.
2. Python + FastAPI is the backend stack.
3. LangChain is the AI orchestration framework.
4. Microsoft Foundry and Azure OpenAI are used for the AI platform/model layer.
5. Azure AI Search is used for enterprise knowledge retrieval.
6. Azure Blob Storage is used for corporate document storage.
7. Microsoft Entra ID is used for authentication.
8. PostgreSQL is used for application-level persistence where required.
9. Do not introduce another agent framework when LangChain can fulfill the requirement.
10. Do not introduce additional infrastructure without a concrete project requirement.
11. Keep secrets and environment-specific configuration outside source code.
12. Keep technology-specific implementation details isolated so components can evolve independently.