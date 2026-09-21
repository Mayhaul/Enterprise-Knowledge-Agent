# Requirements

## 1. Functional Requirements

### 1.1 Corporate Knowledge Q&A

The assistant must allow employees to ask natural-language questions about authorized corporate knowledge.

Supported knowledge may include:

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

The assistant should retrieve relevant corporate information and generate a grounded response.

Where possible, the response should include the source document and relevant section.

---

## 1.2 Personalized Information Retrieval

The assistant must be able to retrieve information specific to the authenticated employee from an authorized internal system or API.

Examples include:

- Leave balance
- Expense claim status
- IT ticket status
- Employee information
- Project information

Personalized information must come from the appropriate live internal system rather than being treated as static corporate-document knowledge.

### Example

User:

> How many leaves do I have remaining?

Expected behavior:

1. Identify that the request requires personalized information.
2. Access the appropriate authorized internal system.
3. Retrieve the employee's current leave information.
4. Return the result to the employee.

---

## 1.3 Business Task Execution

The assistant must be able to perform authorized business tasks through internal APIs.

Potential actions include:

- Create an IT ticket
- Submit a leave request
- Raise an HR request
- Request a new laptop
- Create an expense claim
- Check application/request status

### Example

User:

> Create an IT ticket because my laptop isn't connecting to Wi-Fi.

Expected behavior:

1. Understand the user's request.
2. Determine the information required by the IT system.
3. Ask for missing information if necessary.
4. Ask for confirmation when required.
5. Call the authorized IT ticketing API.
6. Verify that the API operation succeeded.
7. Return the resulting ticket number/status.

The assistant must never claim that an action succeeded unless the relevant API confirms success.

---

# 2. ASK / FIND / ACT Model

The application should organize its capabilities around three primary categories.

## ASK

Used for corporate knowledge questions.

Examples:

- "What is the work-from-home policy?"
- "Can I claim hotel expenses during business travel?"
- "What is the leave policy?"
- "Does the leave policy apply to interns?"

ASK should primarily use RAG over authorized corporate documents.

## FIND

Used for retrieving personalized or live information.

Examples:

- "How many leaves do I have remaining?"
- "What is the status of my expense claim?"
- "Show me my IT tickets."

FIND should use authorized internal APIs/systems.

## ACT

Used for performing business actions.

Examples:

- "Create an IT ticket."
- "Submit my leave request."
- "Raise an HR request."
- "Create an expense claim."

ACT should use controlled internal APIs and appropriate confirmation flows.

---

# 3. Retrieval Requirements

The knowledge retrieval system should support relevant retrieval from corporate documents.

The architecture should be capable of supporting:

- Keyword search
- Vector search
- Hybrid search
- Semantic ranking
- Metadata filtering
- Document-level security

Retrieved information must respect the authenticated user's permissions.

The assistant must not expose a document or information simply because the search system found it.

---

# 4. Source and Citation Requirements

Knowledge-based answers should provide supporting source information where possible.

A source should identify enough information for the employee to understand where the answer originated.

Example:

```text
Answer:
Hotel accommodation can be reimbursed according to the applicable travel policy limit.

Source:
Corporate Travel Policy, Section 4.2

User:
What is the leave policy?

Assistant:
[Grounded answer]

User:
Does that apply to interns?

Assistant:
[Answer using the relevant prior context and corporate knowledge]

Employee
├── HR policies                    ✓
├── IT policies                    ✓
└── Confidential executive salary  ✗

Manager
├── HR policies                    ✓
├── Authorized team information    ✓
└── Confidential HR records       ✗

HR Admin
├── HR policies                    ✓
└── Authorized employee records    ✓