"""Application-facing Finance tools."""

from app.core.security import AuthenticatedUser
from app.integrations.mock_finance import MockFinanceService


class FinanceTools:
    """Application-facing finance operations."""

    def __init__(self, user: AuthenticatedUser):
        self.user = user
        self.service = MockFinanceService()

    async def get_my_expense_claims(self) -> dict:
        """Return expense claims belonging to the authenticated employee."""
        return await self.service.get_expense_claims(self.user)

    async def submit_expense_claim(
        self,
        description: str,
        amount: float,
        currency: str = "INR",
    ) -> dict:
        """Submit an expense claim for the authenticated employee."""
        return await self.service.submit_expense_claim(
            self.user,
            description=description,
            amount=amount,
            currency=currency,
        )
