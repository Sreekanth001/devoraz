import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MedSync AI"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "super_secret_key_for_jwt_auth_123" # In production, use env var
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8 # 8 days
    # Using SQLite for development; use /tmp on Vercel to avoid read-only FS errors
    DATABASE_URL: str = "sqlite:////tmp/medsync.db" if os.environ.get("VERCEL") else "sqlite:///./medsync.db"
    CORS_ORIGINS: str = "*"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
