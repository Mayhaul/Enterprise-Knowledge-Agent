from typing import List, Optional
from pydantic import BaseModel


class AuthenticatedUser(BaseModel):
    """Authenticated employee context representing identity and role claims."""

    user_id: str
    email: str
    display_name: str
    roles: List[str] = ["Employee"]
    department: Optional[str] = None

    def has_role(self, role: str) -> bool:
        """Check if user has a specific role."""
        return role in self.roles


def get_mock_user() -> AuthenticatedUser:
    """Return default mock user for local development."""
    return AuthenticatedUser(
        user_id="usr-dev-001",
        email="dev.employee@example.com",
        display_name="Dev Employee",
        roles=["Employee"],
        department="Engineering",
    )
