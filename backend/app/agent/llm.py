"""LLM initialization for Azure OpenAI via LangChain."""

from typing import Optional

from app.config import get_settings


def get_llm() -> Optional[object]:
    """Return a configured AzureChatOpenAI client, or None if unavailable."""
    settings = get_settings()

    if not settings.AZURE_OPENAI_API_KEY:
        return None

    try:
        from langchain_openai import AzureChatOpenAI
    except ImportError:
        return None

    return AzureChatOpenAI(
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT.rstrip("/"),
        azure_deployment=settings.AZURE_OPENAI_CHAT_DEPLOYMENT,
        api_version=settings.AZURE_OPENAI_API_VERSION,
        api_key=settings.AZURE_OPENAI_API_KEY,
        temperature=0.0,
    )
