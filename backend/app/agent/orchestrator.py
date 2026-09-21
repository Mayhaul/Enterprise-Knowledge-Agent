"""AI Agent Orchestrator skeleton for ASK / FIND / ACT routing."""
from typing import Optional
from app.core.security import AuthenticatedUser
from app.schemas.chat import ChatResponse


class AgentOrchestrator:
    """Coordinates intent classification, RAG retrieval, and tool calling."""

    def __init__(self, user: AuthenticatedUser):
        self.user = user

    async def run(self, message: str, conversation_id: Optional[str] = None) -> ChatResponse:
        """Process user input and route to the appropriate capability (ASK, FIND, ACT).

        Stub implementation for project skeleton. To be implemented in subsequent milestones.
        """
        return ChatResponse(
            conversation_id=conversation_id or "conv-stub-001",
            message="Orchestrator skeleton initialized. Capability execution not yet implemented.",
            capability="ASK",
            citations=[],
            action_required=False,
        )
