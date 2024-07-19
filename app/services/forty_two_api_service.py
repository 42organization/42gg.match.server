import httpx
from app.core.config import settings
from app.exceptions.http_exceptions import NotFoundException, UnauthorizedException


class FortyTwoAPIService:
    def __init__(self):
        self.base_url = settings.forty_two_api_base_url
        self.client_id = settings.oauth_client_id
        self.client_secret = settings.oauth_client_secret
        self.redirect_uri = settings.oauth_redirect_uri

forty_two_api_service = FortyTwoAPIService()