"""LangChain-compatible HR tools."""

from app.core.security import AuthenticatedUser
from app.integrations.mock_hr import MockHRService


class HRTools:
    """Application-facing HR operations."""

    def __init__(self, user: AuthenticatedUser):
        self.user = user
        self.service = MockHRService()

    async def get_leave_balance(self) -> dict:
        """Return the authenticated employee's leave balance."""
        return await self.service.get_leave_balance(self.user)

    async def submit_leave_request(
        self,
        start_date: str,
        end_date: str,
        reason: str,
    ) -> dict:
        """Submit a leave request for the authenticated employee."""
        return await self.service.submit_leave_request(
            self.user,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
        )
