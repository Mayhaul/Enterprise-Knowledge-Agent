"""HTTP clients for enterprise HR, IT, and Finance services."""

from typing import Any

import httpx

from app.config import get_settings
from app.core.security import AuthenticatedUser


class InternalServiceClient:
    """Thin HTTP client that preserves the authenticated employee context."""

    def __init__(self, user: AuthenticatedUser):
        self.user = user
        self.settings = get_settings()

    @property
    def headers(self) -> dict[str, str]:
        return {
            "X-Employee-Id": self.user.user_id,
            "X-Employee-Email": self.user.email,
        }

    async def _get(self, url: str, params: dict[str, Any] | None = None) -> dict:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()

    async def _post(self, url: str, payload: dict[str, Any]) -> dict:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()

    async def get_hr_leave_balance(self) -> dict:
        return await self._get(f"{self.settings.HR_SERVICE_URL.rstrip('/')}/leave-balance")

    async def submit_hr_leave(self, payload: dict[str, Any]) -> dict:
        return await self._post(f"{self.settings.HR_SERVICE_URL.rstrip('/')}/leave", payload)

    async def get_it_tickets(self) -> dict:
        return await self._get(f"{self.settings.IT_SERVICE_URL.rstrip('/')}/tickets")

    async def create_it_ticket(self, payload: dict[str, Any]) -> dict:
        return await self._post(f"{self.settings.IT_SERVICE_URL.rstrip('/')}/tickets", payload)

    async def get_expense_claims(self) -> dict:
        return await self._get(f"{self.settings.FINANCE_SERVICE_URL.rstrip('/')}/claims")

    async def submit_expense_claim(self, payload: dict[str, Any]) -> dict:
        return await self._post(f"{self.settings.FINANCE_SERVICE_URL.rstrip('/')}/claims", payload)
