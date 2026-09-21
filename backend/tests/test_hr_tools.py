import pytest

from app.agent.tools.hr_tools import HRTools
from app.core.security import get_mock_user


@pytest.mark.asyncio
async def test_get_leave_balance_uses_authenticated_user():
    user = get_mock_user()
    tools = HRTools(user)

    result = await tools.get_leave_balance()

    assert result["employee_id"] == user.user_id
    assert result["leave_balance"] == 14
    assert result["unit"] == "days"


@pytest.mark.asyncio
async def test_submit_leave_request():
    tools = HRTools(get_mock_user())

    result = await tools.submit_leave_request(
        start_date="2026-10-01",
        end_date="2026-10-03",
        reason="Personal",
    )

    assert result["status"] == "submitted"
    assert result["request_id"] == "LEAVE-MOCK-0001"
