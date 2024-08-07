from app.core.config import settings
from app.utils.http_client import fetch

class FortyTwoAPIService:
    def __init__(self):
        self.base_url = settings.FORTY_TWO_API_BASE_URL
        self.client_id = settings.FORTY_TWO_OAUTH_CLIENT_ID
        self.client_secret = settings.FORTY_TWO_OAUTH_CLIENT_SECRET

    async def get_user_info_by_forty_two_access_token(self, forty_two_access_token: str) -> dict:
        """
        42 access_token을 이용하여 사용자 정보를 가져옵니다.
        :param forty_two_access_token:
        :return: 42API 사용자 정보
        """
        user_info = await fetch(
            url="https://api.intra.42.fr/v2/me",
            method="GET",
            headers={"Authorization": f"Bearer {forty_two_access_token}"}
        )
        return user_info

forty_two_api_service = FortyTwoAPIService()