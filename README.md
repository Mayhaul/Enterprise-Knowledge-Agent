# Enterprise Knowledge & Task Assistant

An AI-powered corporate assistant built with **React + TypeScript**, **FastAPI**, **LangChain**, and **Microsoft Azure AI** services. The assistant enables employees to securely interact with corporate knowledge and enterprise business systems through natural language.

---

## Capabilities

The assistant operates around three core capabilities:

- **ASK (Corporate Knowledge)**: Answers questions grounded in corporate documents, policies, handbooks, and SOPs using Retrieval-Augmented Generation (RAG) and Azure AI Search.
- **FIND (Personalized Information)**: Retrieves live, authenticated user data (leave balances, expense status, IT tickets) from internal enterprise systems.
- **ACT (Business Tasks)**: Executes authorized business actions (raising IT tickets, submitting leave requests, creating expense claims) with human-in-the-loop confirmation.

---

## Architecture Overview

```text
React (TypeScript) Frontend
       │
   HTTP / SSE
       ▼
FastAPI Backend (Auth / Validation / Routes)
       │
LangChain AI Orchestration
       ├── ASK  ──► Azure AI Search (Blob Storage Documents) + Azure OpenAI
       ├── FIND ──► Authorized Internal APIs (HR, IT, Finance)
       └── ACT  ──► Business Systems (with user confirmation flow)
```

---

## Repository Structure

```text
Enterprise-Knowledge-Agent/
├── docs/                        # Specifications and design documentation
├── backend/                     # Python + FastAPI backend service
│   ├── app/
│   │   ├── main.py              # FastAPI app setup, CORS, lifespan
│   │   ├── config.py            # Pydantic Settings configuration
│   │   ├── core/                # Security, exceptions, logging
│   │   ├── api/                 # Thin API routers (v1/health, v1/chat, etc.)
│   │   ├── schemas/             # Pydantic DTOs & domain models
│   │   ├── agent/               # LangChain orchestration layer (ASK/FIND/ACT)
│   │   ├── rag/                 # Azure AI Search retriever & pipeline
│   │   └── integrations/        # Business service connectors (HR/IT/Finance)
│   ├── tests/                   # Pytest test suite
│   └── requirements.txt
├── frontend/                    # React 19 + TypeScript + Vite application
│   ├── src/
│   │   ├── components/          # Modular UI components
│   │   ├── services/            # API client & backend service connectors
│   │   ├── types/               # TypeScript interfaces matching backend DTOs
│   │   ├── App.tsx              # Main dashboard & status page
│   │   └── main.tsx
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
├── .env.example                 # Environment configuration template
└── AGENTS.md                    # Core architecture & coding instructions
```

---

## Prerequisites

- **Python**: 3.11 or higher
- **Node.js**: 20 or higher (`npm` / `npm.cmd`)
- Optional for full enterprise cloud integration:
  - Microsoft Entra ID tenant
  - Azure OpenAI resource deployment (`gpt-4o`, `text-embedding-3-large`)
  - Azure AI Search service
  - Azure Blob Storage account

---

## Getting Started

### 1. Backend Setup

1. Open a terminal in `backend/`:
   ```powershell
   cd backend
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Configure environment variables:
   Copy `.env.example` to `.env` in `backend/` (or use the project root `.env`):
   ```powershell
   copy .env.example .env
   ```

3. Run the backend development server:
   ```powershell
   uvicorn app.main:app --reload --port 8000
   ```

4. Verify health endpoint:
   - Status endpoint: [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health)
   - Interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

5. Run automated tests:
   ```powershell
   python -m pytest tests/
   ```

---

### 2. Frontend Setup

1. Open a terminal in `frontend/`:
   ```powershell
   cd frontend
   npm.cmd install
   ```

2. Configure environment variables:
   Copy `.env.example` to `.env` in `frontend/`:
   ```powershell
   copy .env.example .env
   ```

3. Start the Vite development server:
   ```powershell
   npm.cmd run dev
   ```

3. Open the application:
   Navigate to [http://localhost:5173](http://localhost:5173) to see the dashboard and check the real-time backend connectivity badge.

---

## Architectural Rules & Standards

Please consult [AGENTS.md](file:///d:/Enterprise-Knowledge-Agent/AGENTS.md) and the `/docs` directory for guidelines on:
- Server-side authorization and Entra ID identity preservation
- Grounded RAG citations and anti-hallucination guardrails
- Tool security and confirmation flows for consequential business tasks