from typing import List, Optional
from pydantic import BaseModel, Field


class Citation(BaseModel):
    """Citation identifying corporate source document and section."""

    document_name: str = Field(..., description="Corporate document title or filename")
    section: Optional[str] = Field(None, description="Section or heading in document")
    content_snippet: Optional[str] = Field(None, description="Excerpt of text supporting the answer")


class ChatRequest(BaseModel):
    """Incoming user chat message request."""

    message: str = Field(..., min_length=1, description="Employee question or task prompt")
    conversation_id: Optional[str] = Field(None, description="Optional thread/conversation ID")


class ChatResponse(BaseModel):
    """Structured assistant response."""

    conversation_id: str
    message: str
    capability: str = Field(..., description="ASK | FIND | ACT")
    citations: List[Citation] = Field(default_factory=list)
    action_required: bool = False
    action_id: Optional[str] = None
