"""ASK / FIND / ACT agent orchestration."""

from typing import Optional

from app.agent.llm import get_llm
from app.agent.prompts import SYSTEM_PROMPT
from app.agent.tools.finance_tools import FinanceTools
from app.agent.tools.hr_tools import HRTools
from app.agent.tools.it_tools import ITTools
from app.core.security import AuthenticatedUser
from app.rag.retriever import CorporateKnowledgeRetriever
from app.schemas.chat import ChatResponse


class AgentOrchestrator:
    """Coordinates simple deterministic routing for ASK, FIND, and ACT."""

    def __init__(self, user: AuthenticatedUser):
        self.user = user
        self.retriever = CorporateKnowledgeRetriever(user)
        self.hr = HRTools(user)
        self.it = ITTools(user)
        self.finance = FinanceTools(user)

    @staticmethod
    def _classify(message: str) -> str:
        """Classify common enterprise requests without requiring an LLM."""
        text = message.lower()

        act_markers = (
            "submit",
            "create ticket",
            "raise ticket",
            "file expense",
            "submit expense",
            "request leave",
            "apply leave",
        )
        find_markers = (
            "leave balance",
            "my tickets",
            "it tickets",
            "expense claims",
            "expense claim status",
        )

        if any(marker in text for marker in act_markers):
            return "ACT"
        if any(marker in text for marker in find_markers):
            return "FIND"
        return "ASK"

    async def run(
        self, message: str, conversation_id: Optional[str] = None
    ) -> ChatResponse:
        """Route a message and execute only supported deterministic operations."""
        conv_id = conversation_id or "conv-local-001"
        capability = self._classify(message)

        if capability == "FIND":
            text = message.lower()
            if "leave balance" in text:
                result = await self.hr.get_leave_balance()
                reply = f"You have {result['leave_balance']} {result['unit']} of leave remaining."
                return ChatResponse(
                    conversation_id=conv_id,
                    message=reply,
                    capability="FIND",
                )

            if "ticket" in text:
                result = await self.it.get_my_tickets()
                tickets = result["tickets"]
                reply = (
                    "You have no IT tickets."
                    if not tickets
                    else "Your IT tickets: "
                    + "; ".join(
                        f"{t['ticket_id']} ({t['status']}): {t['title']}" for t in tickets
                    )
                )
                return ChatResponse(
                    conversation_id=conv_id,
                    message=reply,
                    capability="FIND",
                )

            if "expense" in text or "claim" in text:
                result = await self.finance.get_my_expense_claims()
                claims = result["claims"]
                reply = (
                    "You have no expense claims."
                    if not claims
                    else "Your expense claims: "
                    + "; ".join(
                        f"{c['claim_id']} (₹{c['amount']:.2f}, {c['status']}): {c['description']}"
                        for c in claims
                    )
                )
                return ChatResponse(
                    conversation_id=conv_id,
                    message=reply,
                    capability="FIND",
                )

        if capability == "ACT":
            return ChatResponse(
                conversation_id=conv_id,
                message=(
                    "This request is an ACT operation. "
                    "Confirmation is required before an enterprise action is executed."
                ),
                capability="ACT",
                action_required=True,
            )

        citations = await self.retriever.retrieve(message)
        llm = get_llm()

        if citations and llm is not None:
            context = "\n\n".join(
                f"[{c.document_name}] {c.content_snippet or ''}" for c in citations
            )
            prompt = (
                f"{SYSTEM_PROMPT}\n\nAuthorized context:\n{context}"
                f"\n\nEmployee question: {message}"
            )
            response = await llm.ainvoke(prompt)
            answer = getattr(response, "content", str(response))
        elif citations:
            answer = (
                "I found authorized corporate information, but the answer generator "
                "is currently unavailable."
            )
        else:
            answer = "I could not find authorized corporate information for that question."

        return ChatResponse(
            conversation_id=conv_id,
            message=answer,
            capability="ASK",
            citations=citations,
        )
