"""Deterministic mock IT service for local development."""

from app.core.security import AuthenticatedUser


class MockITService:
    """Provides deterministic IT ticket data and actions."""

    async def get_tickets(self, user: AuthenticatedUser) -> dict:
        return {
            "employee_id": user.user_id,
            "tickets": [
                {
                    "ticket_id": "INC-MOCK-1001",
                    "title": "Laptop Wi-Fi connectivity",
                    "status": "In Progress",
                    "priority": "Medium",
                },
                {
                    "ticket_id": "INC-MOCK-1002",
                    "title": "VPN access request",
                    "status": "Resolved",
                    "priority": "Low",
                },
            ],
            "source": "mock_itsm",
        }

    async def create_ticket(
        self,
        user: AuthenticatedUser,
        issue_description: str,
        category: str,
        priority: str,
    ) -> dict:
        return {
            "employee_id": user.user_id,
            "ticket_id": "INC-MOCK-1003",
            "status": "Created",
            "issue_description": issue_description,
            "category": category,
            "priority": priority,
            "source": "mock_itsm",
        }
