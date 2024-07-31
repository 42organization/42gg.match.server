from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError, ExpiredSignatureError
from fastapi import HTTPException, status
from app.core.config import settings

class JwtTokenProvider:
    def __init__(self):
        self.secret_key = settings.SECRET_KEY
        self.algorithm = settings.ENCODE_ALGORITHM
        self.access_token_expire_minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES
        self.refresh_token_expire_days = settings.REFRESH_TOKEN_EXPIRE_DAYS

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=self.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def create_refresh_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(days=self.refresh_token_expire_days)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def decode_token(self, token: str):
        credentials_exception = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except (JWTError, ExpiredSignatureError):
            raise credentials_exception


    def is_token_expired(self, token: str) -> bool:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            exp = payload.get("exp")
            if exp:
                return datetime.now(timezone.utc) > datetime.fromtimestamp(exp)
            return False
        except JWTError:
            return True

    def refresh_access_token(self, refresh_token: str) -> str:
        if self.is_token_expired(refresh_token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        payload = self.decode_token(refresh_token)
        new_access_token = self.create_access_token({"sub": payload["sub"]})
        return new_access_token

jwt_provider = JwtTokenProvider()