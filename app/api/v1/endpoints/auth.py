from fastapi import APIRouter, HTTPException, Request
from app.core.config import settings
from authlib.integrations.starlette_client import OAuth

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


"""
42 OAuth 로그인 엔드포인트
세션 쿠키를 전송하며 42 OAuth 로그인 페이지로 리다이렉트합니다.
로그인 성공시 "/login/oauth/42/callback" 콜백 엔드포인트로 리다이렉트됩니다.
"""
@router.get("/login/oauth/42")
async def forty_two_login(request: Request):
    redirect_uri = settings.FORTY_TWO_OAUTH_REDIRECT_URI
    response = await oauth.forty_two.authorize_redirect(request, redirect_uri)
    return response

"""
42 OAuth 콜백 엔드포인트
42 OAuth 로그인 콜백을 처리합니다.
로그인 성공시 42access_token을 포함한 JWT 토큰을 반환합니다.
"""
@router.get("/login/oauth/42/callback")
async def forty_two_callback(request: Request):
    try:
        token = await oauth.forty_two.authorize_access_token(request)

        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
