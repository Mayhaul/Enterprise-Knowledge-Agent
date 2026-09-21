from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response payload."""

    status: str = Field(default="ok", description="Application status")
    app_name: str = Field(..., description="Name of the application")
    version: str = Field(..., description="Application version")
    environment: str = Field(..., description="Active environment (e.g., development, production)")
