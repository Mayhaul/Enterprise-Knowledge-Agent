"""Azure AI Search retriever stub with permission-aware filtering placeholder."""
from typing import List
from app.core.security import AuthenticatedUser
from app.schemas.chat import Citation


class CorporateKnowledgeRetriever:
    """Wrapper for Azure AI Search with security trimming."""

    def __init__(self, user: AuthenticatedUser):
        self.user = user

    async def retrieve(self, query: str, top_k: int = 3) -> List[Citation]:
        """Retrieve relevant grounded corporate document chunks matching the user's authorization.

        Stub implementation for project skeleton.
        """
        return []
