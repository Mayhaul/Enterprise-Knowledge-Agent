"""LangChain-compatible IT tools."""

from app.core.security import AuthenticatedUser
from app.integrations.mock_it import MockITService


class ITTools:
    """Application-facing IT operations."""

    def __init__(self, user: AuthenticatedUser):
        self.user = user
        self.service = MockITService()

    async def get_my_tickets(self) -> dict:
        """Return IT tickets belonging to the authenticated employee."""
        return await self.service.get_tickets(self.user)

    async def create_it_ticket(
        self,
        issue_description: str,
        category: str,
        priority: str,
    ) -> dict:
        """Create an IT ticket for the authenticated employee."""
        return await self.service.create_ticket(
            self.user,
            issue_description=issue_description,
            category=category,
            priority=priority,
        )
