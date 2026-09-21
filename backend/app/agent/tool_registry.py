"""Central registry of enterprise tools exposed to the agent."""

from app.agent.tools.finance_tools import FinanceTools
from app.agent.tools.hr_tools import HRTools
from app.agent.tools.it_tools import ITTools
from app.core.security import AuthenticatedUser


def get_tool_registry(user: AuthenticatedUser) -> dict[str, object]:
    """Return all available enterprise tools for an authenticated user."""
    return {
        "hr": HRTools(user),
        "it": ITTools(user),
        "finance": FinanceTools(user),
    }
