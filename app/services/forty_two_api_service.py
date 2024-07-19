import httpx
from app.core.config import settings
from app.exceptions.http_exceptions import NotFoundException, UnauthorizedException


class FortyTwoAPIService:
    def __init__(self):
        self.base_url = settings.FORTY_TWO_API_BASE_URL
        self.client_id = settings.FORTY_TWO_OAUTH_CLIENT_ID
        self.client_secret = settings.FORTY_TWO_OAUTH_CLIENT_SECRET

forty_two_api_service = FortyTwoAPIService()