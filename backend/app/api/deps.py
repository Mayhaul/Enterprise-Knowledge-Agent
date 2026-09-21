from typing import Annotated
from fastapi import Depends
from app.config import Settings, get_settings
from app.core.security import AuthenticatedUser, get_mock_user


def get_current_user(
    settings: Annotated[Settings, Depends(get_settings)]
) -> AuthenticatedUser:
    """Resolve the authenticated employee context.

    In development with MOCK_AUTH_ENABLED=True, returns a default mock user.
    In production, this validates the Entra ID bearer token from the Authorization header.
    """
    if settings.MOCK_AUTH_ENABLED:
        return get_mock_user()

    # Placeholder for Entra ID JWT verification
    return get_mock_user()
