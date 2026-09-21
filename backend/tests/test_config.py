from app.config import Settings
from app.core.exceptions import AuthorizationException, ResourceNotFoundException


def test_settings_cors_parsing():
    """Test that Settings correctly parses both list and comma-separated string origins."""
    s1 = Settings(BACKEND_CORS_ORIGINS=["http://localhost:5173", "http://127.0.0.1:5173"])
    assert len(s1.BACKEND_CORS_ORIGINS) == 2

    s2 = Settings(BACKEND_CORS_ORIGINS="http://localhost:5173, http://127.0.0.1:5173")
    assert s2.BACKEND_CORS_ORIGINS == ["http://localhost:5173", "http://127.0.0.1:5173"]


def test_custom_exceptions():
    """Verify status codes and messages of custom domain exceptions."""
    auth_exc = AuthorizationException("User not authorized")
    assert auth_exc.status_code == 403
    assert auth_exc.message == "User not authorized"

    not_found_exc = ResourceNotFoundException("Document missing")
    assert not_found_exc.status_code == 404
    assert not_found_exc.message == "Document missing"
