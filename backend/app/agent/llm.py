"""LLM initialization module for Azure OpenAI / Microsoft Foundry."""
from typing import Any, Optional
from app.config import get_settings


def get_llm() -> Optional[Any]:
    """Initialize AzureChatOpenAI instance based on environment settings.

    Deferred import keeps startup fast and testable when LangChain Azure dependencies
    are mocked or not yet configured.
    """
    settings = get_settings()

    try:
        from langchain_openai import AzureChatOpenAI

        return AzureChatOpenAI(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            azure_deployment=settings.AZURE_OPENAI_CHAT_DEPLOYMENT,
            api_version=settings.AZURE_OPENAI_API_VERSION,
            api_key=settings.AZURE_OPENAI_API_KEY or "placeholder-key",
            temperature=0.0,
        )
    except ImportError:
        # Fallback / stub if dependency not loaded
        return None

