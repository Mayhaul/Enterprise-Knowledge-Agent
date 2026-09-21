# System Architecture

## 1. Architectural Overview

The Enterprise Knowledge & Task Assistant consists of:

- React frontend
- FastAPI backend
- LangChain AI orchestration
- Microsoft Foundry / Azure OpenAI
- Azure AI Search for enterprise knowledge retrieval
- Azure Blob Storage for corporate documents
- Microsoft Entra ID for authentication
- Internal business-system APIs for personalized information and actions

The system follows a layered architecture so that the user interface, API layer, AI orchestration, retrieval system, and enterprise integrations remain separated.

## 2. High-Level Architecture

```text
                         Employee
                            |
                            v
                  +-------------------+
                  |   React Frontend  |
                  |   TypeScript      |
                  +---------+---------+
                            |
                       HTTP / SSE
                            |
                            v
                  +-------------------+
                  |   FastAPI Backend |
                  |                   |
                  | Auth / API /      |
                  | Request Handling  |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  |     LangChain     |
                  | AI Orchestration  |
                  +---------+---------+
                            |
              +-------------+-------------+
              |             |             |
              v             v             v
          Knowledge      Personalized    Business
          Retrieval      Information      Actions
              |             |             |
              v             v             v
       Azure AI Search  Internal APIs   Internal APIs
              |
              v
       Corporate Documents
       / Azure Blob Storage

                            |
                            v
                 Microsoft Foundry /
                    Azure OpenAI
                            |
                            v
                  Grounded Response
                     + Citations