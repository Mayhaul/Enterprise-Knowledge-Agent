from typing import Annotated
from fastapi import APIRouter, Depends
from app.config import Settings, get_settings
from app.schemas.health import HealthResponse

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse, summary="Service Health Check")
async def health_check(
    settings: Annotated[Settings, Depends(get_settings)]
) -> HealthResponse:
    """Return health status and basic application metadata."""
    return HealthResponse(
        status="ok",
        app_name=settings.APP_NAME,
        version=settings.APP_VERSION,
        environment=settings.ENVIRONMENT,
    )
