# Agent Design

## Objective

The AI agent is responsible for understanding employee requests and orchestrating the appropriate capability of the Enterprise Knowledge & Task Assistant.

The agent uses LangChain for:

- Intent understanding
- RAG orchestration
- Tool calling
- Internal API interaction
- Conversational context
- Response generation

The agent operates around three primary capabilities:

- ASK
- FIND
- ACT

---

## 1. ASK

ASK is used when the employee wants information from corporate knowledge.

Examples:

- "What is the company's work-from-home policy?"
- "Can I claim hotel expenses during a business trip?"
- "What is the leave policy?"
- "Does that policy apply to interns?"

### ASK Flow

```text
User Question
      |
      v
Understand Request
      |
      v
Corporate Knowledge Required
      |
      v
RAG Retrieval
      |
      v
Authorized Corporate Information
      |
      v
LLM
      |
      v
Grounded Response + Citation