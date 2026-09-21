import pytest

from app.agent.orchestrator import AgentOrchestrator
from app.core.security import get_mock_user


@pytest.mark.asyncio
async def test_orchestrator_routes_leave_balance_to_find():
    result = await AgentOrchestrator(get_mock_user()).run("What is my leave balance?")

    assert result.capability == "FIND"
    assert "14 days" in result.message


@pytest.mark.asyncio
async def test_orchestrator_routes_it_ticket_to_find():
    result = await AgentOrchestrator(get_mock_user()).run("Show my IT tickets")

    assert result.capability == "FIND"
    assert "INC-MOCK-1001" in result.message


@pytest.mark.asyncio
async def test_orchestrator_routes_expense_to_find():
    result = await AgentOrchestrator(get_mock_user()).run("Show my expense claims")

    assert result.capability == "FIND"
    assert "EXP-MOCK-1001" in result.message


@pytest.mark.asyncio
async def test_orchestrator_routes_action_to_confirmation():
    result = await AgentOrchestrator(get_mock_user()).run("Submit a leave request")

    assert result.capability == "ACT"
    assert result.action_required is True
