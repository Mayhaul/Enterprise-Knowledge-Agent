import pytest

from app.agent.tools.finance_tools import FinanceTools
from app.core.security import get_mock_user


@pytest.mark.asyncio
async def test_get_my_expense_claims():
    tools = FinanceTools(get_mock_user())

    result = await tools.get_my_expense_claims()

    assert result["employee_id"] == "usr-dev-001"
    assert len(result["claims"]) == 2
    assert result["claims"][0]["claim_id"] == "EXP-MOCK-1001"


@pytest.mark.asyncio
async def test_submit_expense_claim():
    tools = FinanceTools(get_mock_user())

    result = await tools.submit_expense_claim(
        description="Team lunch",
        amount=1250.0,
        currency="INR",
    )

    assert result["status"] == "Submitted"
    assert result["claim_id"] == "EXP-MOCK-1003"
    assert result["amount"] == 1250.0
