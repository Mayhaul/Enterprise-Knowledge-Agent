# Enterprise Knowledge & Task Assistant

## Project Concept

The Enterprise Knowledge & Task Assistant is an AI-powered corporate assistant that allows employees to interact with corporate knowledge and internal business systems using natural language.

The assistant provides three core capabilities:

- ASK: Answer questions using authorized corporate knowledge.
- FIND: Retrieve personalized information from authorized internal systems.
- ACT: Perform authorized business tasks through internal systems.

The system uses Retrieval-Augmented Generation (RAG) to ground AI responses in the organization's private corporate knowledge rather than relying solely on the language model's training data.

## Problem Being Solved

Corporate information is often distributed across many sources, including:

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

Employees should not need to manually search through these sources to answer routine questions.

The assistant provides a natural-language interface through which an employee can ask a question and receive a direct answer supported by relevant corporate information.

## Core Capabilities

### ASK - Corporate Knowledge

ASK handles questions about corporate knowledge, including:

- Policies
- Procedures
- Documentation
- SOPs
- Internal FAQs
- Other authorized corporate information

Example:

> "Can I claim hotel expenses during a business trip?"

The system retrieves the relevant travel policy and provides an answer based on the retrieved information, along with its source.

### FIND - Personalized Information

FIND retrieves information specific to the authenticated employee from an authorized internal system or API.

Examples include:

- Leave balance
- Expense claim status
- IT ticket status
- Employee information
- Project information

Example:

> "How many leaves do I have remaining?"

The assistant retrieves the employee's current leave information from the appropriate internal system rather than relying on a static document.

### ACT - Business Tasks

ACT allows the assistant to perform authorized actions through internal business-system APIs.

Examples include:

- Create an IT ticket
- Submit a leave request
- Raise an HR request
- Request a new laptop
- Create an expense claim
- Check application/request status

Example:

> "Create an IT ticket because my laptop isn't connecting to Wi-Fi."

The assistant should understand the request, collect any required information, request confirmation when necessary, call the appropriate API, and return the resulting ticket number.

## High-Level User Experience

The employee interacts with the assistant through a conversational interface.

The system determines whether the request is primarily:

1. A corporate knowledge question
2. A request for personalized information
3. A request to perform a business action

It then uses the appropriate retrieval mechanism or tool.

## Grounded Responses

Corporate-specific responses should be based on retrieved corporate information or authorized internal system data.

The assistant should provide source information for knowledge-based answers where possible.

If sufficient information cannot be found, the assistant should state that the information is unavailable rather than inventing an answer.

## Security

The assistant handles corporate and potentially sensitive information.

The project therefore requires:

- Microsoft Entra ID authentication
- Role-based authorization
- Permission-aware retrieval
- Controlled access to internal APIs
- Confirmation before sensitive or consequential actions

The assistant must only expose information that the authenticated employee is authorized to access.

## Example User Scenarios

### Corporate Knowledge

> "What is the company's work-from-home policy?"

Retrieve the relevant policy and provide a grounded answer with its source.

### Multi-Document RAG

> "Compare domestic and international travel reimbursement."

Retrieve the relevant information from the appropriate documents and present the comparison.

### Conversational RAG

> "What is the leave policy?"

Followed by:

> "Does that apply to interns?"

The assistant should retain the relevant conversational context and use it when answering the follow-up.

### Personalized Information

> "How many leaves do I have remaining?"

Retrieve the current employee-specific information from an authorized internal system.

### Business Action

> "Create an IT ticket because my laptop isn't connecting to Wi-Fi."

Use the appropriate authorized IT integration and return the resulting ticket information after successful execution.

### Security

> "Show me another employee's salary."

The system should deny access when the authenticated employee does not have permission to view that information.

### Unknown Information

> "What is the company's policy for employees working on Mars?"

If no relevant corporate information exists, the assistant should state that no relevant information was found.

## Project Scope

The initial project focuses on demonstrating:

- Enterprise RAG
- Agent-based orchestration
- Personalized information retrieval
- Authorized business actions
- Source citations
- Authentication and authorization
- Hallucination prevention

## Future Enhancements

Potential future capabilities include:

- Hybrid keyword + vector search
- Semantic ranking
- Document-level security
- Metadata filtering
- Multilingual employee support
- Conversation history
- Contextual follow-up questions
- Feedback collection
- Retrieval accuracy evaluation
- Groundedness evaluation
- Audit logs for agent actions
- Integration with HR, IT service management, finance, and collaboration systems

## One-Line Description

An AI-powered corporate assistant that enables employees to securely access corporate knowledge, retrieve personalized information, and perform authorized business tasks through natural language.