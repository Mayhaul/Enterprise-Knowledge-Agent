class EnterpriseAgentException(Exception):
    """Base exception for all enterprise agent errors."""

    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class AuthorizationException(EnterpriseAgentException):
    """Raised when user lacks permission to access knowledge or perform an action."""

    def __init__(self, message: str = "Access denied: insufficient permissions"):
        super().__init__(message, status_code=403)


class ResourceNotFoundException(EnterpriseAgentException):
    """Raised when a requested resource or corporate document is not found."""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)


class ActionConfirmationRequiredException(EnterpriseAgentException):
    """Raised when a consequential action requires explicit human confirmation."""

    def __init__(self, action_id: str, message: str = "Action requires confirmation"):
        super().__init__(message, status_code=428)
        self.action_id = action_id
