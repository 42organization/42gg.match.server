import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME : str = "42gg.match.server"
    DOMAIN : str = "localhost:8000"
    SECRET_KEY : str
    ENCODE_ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 60
    REFRESH_TOKEN_EXPIRE_DAYS : int = 7

    API_V1_URI: str = "/api/v1"
    REDIS_URL : str = "redis://localhost:6379/0"

    FORTY_TWO_API_BASE_URL: str = "https://api.intra.42.fr"
    FORTY_TWO_OAUTH_CLIENT_ID : str
    FORTY_TWO_OAUTH_CLIENT_SECRET : str
    FORTY_TWO_OAUTH_REDIRECT_URI : str = "http://locahost:8000/api/v1/auth/login/oauth/42/callback"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()