from fastapi import APIRouter, Depends, HTTPException, status

from app.api.v1.deps import get_current_user, CurrentUser
from app.schemas.user import User

router = APIRouter()


@router.get("")
def users():
    return "This is User!"


@router.get("/me", response_model=User, status_code=status.HTTP_200_OK)
def me(current_user: CurrentUser):
    """
    헤더의 Bearer 토큰을 토대로 사용자 정보를 반환합니다.
    :param current_user: \[User\] 사용자 정보
    :return: \[User\] 사용자 정보
    """
    return current_user
