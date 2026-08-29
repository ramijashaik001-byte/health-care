# app/core/config.py
"""
Application configuration module.
This file sets up configurations using Pydantic BaseSettings, which integrates with environment variables.
"""
import os
from typing import List, Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CareFlow Healthcare System"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "SUPER_SECRET_KEY_FOR_CAREFLOW_APPLICATION_THAT_MUST_BE_CHANGED_IN_PRODUCTION"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 1 week
    
    # SQLite fallback
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./careflow.db")
    
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    # Additional settings for scalability
    MAX_DB_POOL_SIZE: int = 20
    DB_TIMEOUT_SECONDS: int = 30
    LOG_LEVEL: str = "INFO"
    
    class Config:
        case_sensitive = True

settings = Settings()
