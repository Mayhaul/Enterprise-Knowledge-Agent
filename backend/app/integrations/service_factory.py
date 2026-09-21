"""Factory selecting real HTTP integrations or local development adapters."""

from app.config import get_settings
from app.core.security import AuthenticatedUser
from app.integrations.internal_api import InternalServiceClient
from app.integrations.mock_finance import MockFinanceService
from app.integrations.mock_hr import MockHRService
from app.integrations.mock_it import MockITService


class ServiceFactory:
    """Centralize integration selection."""

    def __init__(self, user: AuthenticatedUser):
        self.user = user
        self.settings = get_settings()

    def hr(self):
        if self.settings.USE_MOCK_INTERNAL_SERVICES:
            return MockHRService()
        return InternalServiceClient(self.user)

    def it(self):
        if self.settings.USE_MOCK_INTERNAL_SERVICES:
            return MockITService()
        return InternalServiceClient(self.user)

    def finance(self):
        if self.settings.USE_MOCK_INTERNAL_SERVICES:
            return MockFinanceService()
        return InternalServiceClient(self.user)
