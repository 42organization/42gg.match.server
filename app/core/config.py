import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "42gg.match.server"
    api_v1_str: str = "/api/v1"
    secret_key: str = os.getenv("SECRET_KEY", "supersecretkey")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    forty_two_api_base_url: str = os.getenv("FORTY_TWO_API_BASE_URL", "https://api.intra.42.fr")
    forty_two_oauth_client_id: str = os.getenv("FORTY_TWO_OAUTH_CLIENT_ID", "")
    forty_two_oauth_client_secret: str = os.getenv("FORTY_TWO_OAUTH_CLIENT_SECRET", "")

    class Config:
        case_sensitive = True

settings = Settings()