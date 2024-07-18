import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "42gg.match.server"
    api_v1_str: str = "/api/v1"
    secret_key: str = os.getenv("SECRET_KEY", "supersecretkey")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    oauth_client_id: str = os.getenv("OAUTH_CLIENT_ID", "")
    oauth_client_secret: str = os.getenv("OAUTH_CLIENT_SECRET", "")

    class Config:
        case_sensitive = True

settings = Settings()