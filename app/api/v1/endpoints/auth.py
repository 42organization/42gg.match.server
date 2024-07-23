import traceback

from app.schemas.auth import FortyTwoToken
from fastapi import APIRouter, HTTPException, Request, status
from app.core.config import settings
from authlib.integrations.starlette_client import OAuth
from app.services.auth_service import auth_service

oauth = OAuth()
oauth.register(
    name="forty_two",
    client_id=settings.FORTY_TWO_OAUTH_CLIENT_ID,
    client_secret=settings.FORTY_TWO_OAUTH_CLIENT_SECRET,
    authorize_url=settings.FORTY_TWO_API_BASE_URL + "/oauth/authorize",
    authorize_params=None,
    access_token_url=settings.FORTY_TWO_API_BASE_URL + "/oauth/token",
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri=settings.FORTY_TWO_OAUTH_REDIRECT_URI,
    client_kwargs={"scope": "public"},
)

router = APIRouter()

@router.get("")
def auth():
    return "This is Auth!"

@router.get("/login/oauth/42")
async def forty_two_login(request: Request):
    """
    42 OAuth 로그인 엔드포인트
    세션 쿠키를 전송하며 42 OAuth 로그인 페이지로 리다이렉트합니다.
    로그인 성공시 "/login/oauth/42/callback" 콜백 엔드포인트로 리다이렉트됩니다.
    TODO: 요청에 따라서 callback주소 변경
    """
    redirect_uri = settings.FORTY_TWO_OAUTH_REDIRECT_URI
    response = await oauth.forty_two.authorize_redirect(request, redirect_uri)
    return response

@router.get("/login/oauth/42/callback", status_code=status.HTTP_200_OK)
async def forty_two_callback(request: Request):
    """
    42 OAuth 콜백 엔드포인트
    42 OAuth 로그인 콜백을 처리합니다.
    로그인 성공시 42 access_token을 포함한 JWT 토큰을 반환합니다.
    """
    try:
        forty_two_token : FortyTwoToken = await oauth.forty_two.authorize_access_token(request)
        jwt_token = await auth_service.create_jwt_token_from_forty_two_token(forty_two_token)
        return {"access_token": jwt_token}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
