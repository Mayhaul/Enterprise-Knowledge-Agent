"""Integration checks for the configured Azure OpenAI deployment."""

import os

import pytest

from app.agent.llm import get_llm
from app.config import get_settings


@pytest.mark.integration
def test_azure_openai_chat_completion():
    """Call the configured deployment using credentials from backend/.env.

    This test is skipped when no API key is configured, so normal unit test
    runs do not require Azure credentials.
    """
    settings = get_settings()

    if not settings.AZURE_OPENAI_API_KEY:
        pytest.skip("AZURE_OPENAI_API_KEY is not configured")

    endpoint = settings.AZURE_OPENAI_ENDPOINT.rstrip("/")
    if not endpoint.endswith(".openai.azure.com"):
        pytest.fail(
            "This integration test expects a direct Azure OpenAI resource endpoint "
            f"(*.openai.azure.com), got: {endpoint}"
        )

    llm = get_llm()
    assert llm is not None

    response = llm.invoke("Reply with exactly: AZURE_OK")
    content = getattr(response, "content", "")
    assert content, "Azure OpenAI returned an empty response"


@pytest.mark.integration
def test_azure_openai_configuration_is_loaded():
    """Verify the local environment contains the expected deployment settings."""
    settings = get_settings()

    if not settings.AZURE_OPENAI_API_KEY:
        pytest.skip("AZURE_OPENAI_API_KEY is not configured")

    assert settings.AZURE_OPENAI_ENDPOINT.startswith("https://")
    assert settings.AZURE_OPENAI_CHAT_DEPLOYMENT == "gpt-4.1-mini"
    assert settings.AZURE_OPENAI_API_VERSION
