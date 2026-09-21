"""Direct Azure OpenAI SDK smoke test.

This bypasses LangChain so Azure authentication can be isolated from
LangChain configuration.
"""

import pytest

from app.config import get_settings


@pytest.mark.integration
def test_azure_openai_direct():
    settings = get_settings()

    if not settings.AZURE_OPENAI_API_KEY:
        pytest.fail(
            "AZURE_OPENAI_API_KEY is not loaded. Ensure backend/.env exists "
            "and contains a non-empty AZURE_OPENAI_API_KEY."
        )

    endpoint = settings.AZURE_OPENAI_ENDPOINT.rstrip("/")
    deployment = settings.AZURE_OPENAI_CHAT_DEPLOYMENT

    if not endpoint.endswith(".openai.azure.com"):
        pytest.fail(
            "Expected a direct Azure OpenAI resource endpoint ending in "
            "*.openai.azure.com"
        )

    try:
        from openai import AzureOpenAI
    except ImportError:
        pytest.fail(
            "The 'openai' package is required for this direct SDK test. "
            "Install it with: pip install openai"
        )

    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=settings.AZURE_OPENAI_API_KEY,
        api_version=settings.AZURE_OPENAI_API_VERSION,
    )

    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {
                    "role": "user",
                    "content": "Reply with exactly: AZURE_DIRECT_OK",
                }
            ],
        )
    except Exception as exc:
        status = getattr(exc, "status_code", None)
        if status:
            pytest.fail(f"Azure OpenAI request failed with HTTP {status}: {exc}")
        pytest.fail(f"Azure OpenAI request failed: {exc}")

    content = (response.choices[0].message.content or "").strip()
    assert content, "Azure OpenAI returned an empty response"
