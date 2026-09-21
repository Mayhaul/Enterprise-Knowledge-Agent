from functools import lru_cache
from pathlib import Path
from typing import List, Union

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


REPO_ROOT = Path(__file__).resolve().parents[2]
BACKEND_ENV = REPO_ROOT / "backend" / ".env"


class Settings(BaseSettings):
    """Application settings and environment configuration."""

    model_config = SettingsConfigDict(
        env_file=str(BACKEND_ENV),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_NAME: str = "Enterprise Knowledge & Task Assistant"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
    ]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        """Support JSON array and comma-separated string origins."""
        if isinstance(v, str) and not v.strip().startswith("["):
            return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v

    MOCK_AUTH_ENABLED: bool = True
    AZURE_TENANT_ID: str = "00000000-0000-0000-0000-000000000000"
    AZURE_CLIENT_ID: str = "00000000-0000-0000-0000-000000000000"
    AZURE_CLIENT_SECRET: str = ""

    AZURE_OPENAI_ENDPOINT: str = "https://placeholder.openai.azure.com/"
    AZURE_OPENAI_API_KEY: str = ""
    AZURE_OPENAI_API_VERSION: str = "2024-06-01"
    AZURE_OPENAI_CHAT_DEPLOYMENT: str = "gpt-4o"
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT: str = "text-embedding-3-large"

    AZURE_SEARCH_SERVICE_ENDPOINT: str = "https://placeholder.search.windows.net"
    AZURE_SEARCH_API_KEY: str = ""
    AZURE_SEARCH_INDEX_NAME: str = "corporate-knowledge-index"
    AZURE_SEARCH_USE_SEMANTIC_RANKER: bool = True

    AZURE_STORAGE_ACCOUNT_URL: str = "https://placeholder.blob.core.windows.net"
    AZURE_STORAGE_CONTAINER_NAME: str = "corporate-documents"
    AZURE_STORAGE_CONNECTION_STRING: str = ""

    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/enterprise_agent"

    USE_MOCK_INTERNAL_SERVICES: bool = True
    HR_SERVICE_URL: str = "http://localhost:8001/hr"
    IT_SERVICE_URL: str = "http://localhost:8001/it"
    FINANCE_SERVICE_URL: str = "http://localhost:8001/finance"


@lru_cache()
def get_settings() -> Settings:
    """Return cached application settings instance."""
    return Settings()
