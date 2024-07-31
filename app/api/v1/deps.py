from typing import Annotated
from fastapi import Depends, status, Request, HTTPException

from app.schemas.user import User
from app.utils.jwt_token_provider import jwt_provider


def get_token(request: Request) -> str:
    """
    헤더의 Authorization에서 Bearer 토큰을 추출합니다.
    :param request: Request
    :return: jwt access token
    :raise: HTTPException
    """
    authorization: str = request.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return authorization.split(" ")[1]


def get_current_user(token: User = Depends(get_token)) -> User:
    """
    사용자의 토큰을 토대로 사용자 정보를 반환합니다.
    :param token: 사용자 jwt access token
    :return: User: 사용자 정보
    """
    payload = jwt_provider.decode_token(token)
    user = User(**payload)
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
