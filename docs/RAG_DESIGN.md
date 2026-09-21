# RAG Design

## Objective

The Retrieval-Augmented Generation (RAG) system grounds the assistant's corporate knowledge responses in the organization's private documents and policies.

The assistant should not rely solely on the LLM's training data when answering company-specific questions.

## Knowledge Sources

The knowledge base may contain:

- HR policies
- Employee handbooks
- IT documentation
- Standard Operating Procedures (SOPs)
- Finance policies
- Project documentation
- Product documentation
- Company announcements
- Training materials
- Internal FAQs

## Document Storage

Corporate documents are stored in Azure Blob Storage.

The documents are then processed and indexed so that relevant information can be retrieved when an employee asks a question.

```text
Corporate Documents
        |
        v
Azure Blob Storage
        |
        v
Document Processing
        |
        v
Indexing
        |
        v
Azure AI Search

## retrieval flow
Employee Question
        |
        v
FastAPI
        | 
        v
LangChain
        |
        v
Azure AI Search
        |
        v
Relevant Corporate Information
        |
        v
LangChain RAG Pipeline
        |
        v
Azure OpenAI / Microsoft Foundry
        |
        v
Grounded Response + Citation