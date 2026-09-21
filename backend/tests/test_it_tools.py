import pytest

from app.agent.tools.it_tools import ITTools
from app.core.security import get_mock_user


@pytest.mark.asyncio
async def test_get_my_tickets():
    tools = ITTools(get_mock_user())

    result = await tools.get_my_tickets()

    assert result["employee_id"] == "usr-dev-001"
    assert len(result["tickets"]) == 2
    assert result["tickets"][0]["ticket_id"] == "INC-MOCK-1001"


@pytest.mark.asyncio
async def test_create_it_ticket():
    tools = ITTools(get_mock_user())

    result = await tools.create_it_ticket(
        issue_description="Laptop cannot connect to Wi-Fi",
        category="Network",
        priority="High",
    )

    assert result["status"] == "Created"
    assert result["ticket_id"] == "INC-MOCK-1003"
    assert result["priority"] == "High"
