from app.schemas.auth import FortyTwoToken
from app.schemas.user import User
from app.services.forty_two_api_service import forty_two_api_service
from app.utils.jwt_token_provider import jwt_provider


class AuthService():
    def __init__(self):
        pass
    async def create_jwt_token_from_forty_two_token(self, token : FortyTwoToken):
        """
        42 access_token을 이용하여 JWT 토큰을 생성합니다.
        :param token: 42 토큰
        :return: JWT 토큰
        """
        try:
            forty_two_user_info = await forty_two_api_service.get_user_info_by_forty_two_access_token(
                token["access_token"])
            user = User(
                forty_two_id=forty_two_user_info["id"],
                intra_id=forty_two_user_info["login"],
                profile_image=forty_two_user_info.get("image", {}).get("link"),
                email=forty_two_user_info["email"],
                forty_two_access_token=token
            )
            return jwt_provider.create_access_token(user.dict())
        except KeyError as e:
            raise ValueError(f"Missing essential user information: {e}")


# class User(BaseModel):
#     id : int
#     intra_id: int
#     profile_image: str
#     email: str
#     forty_two_access_token: FortyTwoToken

auth_service = AuthService()