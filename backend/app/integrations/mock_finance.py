"""Deterministic mock Finance service for local development."""

from app.core.security import AuthenticatedUser


class MockFinanceService:
    """Provides deterministic finance data and actions."""

    async def get_expense_claims(self, user: AuthenticatedUser) -> dict:
        return {
            "employee_id": user.user_id,
            "claims": [
                {
                    "claim_id": "EXP-MOCK-1001",
                    "description": "Client meeting travel",
                    "amount": 1850.0,
                    "currency": "INR",
                    "status": "Approved",
                },
                {
                    "claim_id": "EXP-MOCK-1002",
                    "description": "Office supplies",
                    "amount": 920.0,
                    "currency": "INR",
                    "status": "Pending",
                },
            ],
            "source": "mock_finance",
        }

    async def submit_expense_claim(
        self,
        user: AuthenticatedUser,
        description: str,
        amount: float,
        currency: str = "INR",
    ) -> dict:
        return {
            "employee_id": user.user_id,
            "claim_id": "EXP-MOCK-1003",
            "description": description,
            "amount": amount,
            "currency": currency,
            "status": "Submitted",
            "source": "mock_finance",
        }
