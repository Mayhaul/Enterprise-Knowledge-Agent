"""Deterministic mock HR integration for local development."""

from app.core.security import AuthenticatedUser


class MockHRService:
    """Provides deterministic employee-specific HR data."""

    async def get_leave_balance(self, user: AuthenticatedUser) -> dict:
        return {
            "employee_id": user.user_id,
            "leave_balance": 14,
            "unit": "days",
            "source": "mock_hr",
        }

    async def submit_leave_request(
        self,
        user: AuthenticatedUser,
        start_date: str,
        end_date: str,
        reason: str,
    ) -> dict:
        return {
            "employee_id": user.user_id,
            "request_id": "LEAVE-MOCK-0001",
            "status": "submitted",
            "start_date": start_date,
            "end_date": end_date,
            "reason": reason,
            "source": "mock_hr",
        }
