"""Azure AI Search retriever with permission-aware filtering."""

from typing import List

from app.config import get_settings
from app.core.security import AuthenticatedUser
from app.schemas.chat import Citation


class CorporateKnowledgeRetriever:
    """Searches authorized corporate knowledge."""

    def __init__(self, user: AuthenticatedUser):
        self.user = user

    async def retrieve(self, query: str, top_k: int = 3) -> List[Citation]:
        """Retrieve grounded document chunks using Azure AI Search.

        Returns an empty list until the search index/client is configured.
        """
        settings = get_settings()

        if not settings.AZURE_SEARCH_SERVICE_ENDPOINT or not settings.AZURE_SEARCH_API_KEY:
            return []

        try:
            from azure.core.credentials import AzureKeyCredential
            from azure.search.documents import SearchClient
        except ImportError:
            return []

        try:
            client = SearchClient(
                endpoint=settings.AZURE_SEARCH_SERVICE_ENDPOINT.rstrip("/"),
                index_name=settings.AZURE_SEARCH_INDEX_NAME,
                credential=AzureKeyCredential(settings.AZURE_SEARCH_API_KEY),
            )
            filter_expression = f"employee_id eq '{self.user.user_id}'"
            results = client.search(
                search_text=query,
                top=top_k,
                filter=filter_expression,
            )

            citations: List[Citation] = []
            for item in results:
                citations.append(
                    Citation(
                        document_name=item.get("document_name") or item.get("title") or "Unknown document",
                        section=item.get("section"),
                        content_snippet=item.get("content") or item.get("chunk"),
                    )
                )
            return citations
        except Exception:
            return []
