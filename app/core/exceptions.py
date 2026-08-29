# app/core/exceptions.py
"""
Custom application exceptions and handlers.
Allows uniform JSON response error structures.
"""
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

class CareFlowException(Exception):
    """Base exception for CareFlow system errors."""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class ResourceNotFoundError(CareFlowException):
    """Exception raised when database resources are not found."""
    def __init__(self, resource: str, identifier: str):
        super().__init__(f"Resource '{resource}' with identifier '{identifier}' not found.", status_code=404)

class ValidationFailedError(CareFlowException):
    """Exception raised when complex validation constraints fail."""
    def __init__(self, message: str):
        super().__init__(message, status_code=422)

class BusinessRuleViolationError(CareFlowException):
    """Exception raised when business flow policies are violated."""
    def __init__(self, message: str):
        super().__init__(message, status_code=409)

def exception_handler(request: Request, exc: CareFlowException) -> JSONResponse:
    """Global FastAPI exception handler for custom app exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "error": {"message": exc.message, "type": exc.__class__.__name__}}
    )
