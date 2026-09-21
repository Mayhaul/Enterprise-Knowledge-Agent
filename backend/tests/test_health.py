from fastapi.testclient import TestClient


def test_health_check_endpoint(client: TestClient):
    """Verify that GET /api/v1/health returns 200 OK and expected schema."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert "app_name" in data
    assert "version" in data
    assert "environment" in data


def test_root_endpoint(client: TestClient):
    """Verify that GET / returns 200 OK and application metadata."""
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert "health" in data
    assert "docs" in data
    assert data["health"] == "/api/v1/health"
