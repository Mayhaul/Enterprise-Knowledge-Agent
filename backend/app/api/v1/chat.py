"""Chat API endpoint."""

from fastapi import APIRouter, Depends

from app.agent.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.core.security import AuthenticatedUser
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    user: AuthenticatedUser = Depends(get_current_user),
) -> ChatResponse:
    orchestrator = AgentOrchestrator(user)
    return await orchestrator.run(
        request.message,
        conversation_id=request.conversation_id,
    )
