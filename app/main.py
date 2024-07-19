from fastapi import FastAPI, APIRouter
from app.api.v1.endpoints import auth, evaluation, user
from app.core.config import settings
from starlette.middleware.sessions import SessionMiddleware
from app.exceptions.handlers import (
    not_found_exception_handler,
    unauthorized_exception_handler,
    forbidden_exception_handler,
    bad_request_exception_handler,
    unexpected_exception_handler
)
from app.exceptions.http_exceptions import NotFoundException, UnauthorizedException, ForbiddenException, BadRequestException

# FastAPI 인스턴스, docs 설정
app = FastAPI(
    title="42gg.match.server API",
    description="API documentation for 42gg.match.server",
    version="0.1.0",
    docs_url="/api/docs",  # Swagger UI 경로 설정
    redoc_url="/api/redoc"  # ReDoc 경로 설정
)

# SessionMiddleware 추가
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY, same_site="Lax")

# APIRouter 설정
api_v1_router = APIRouter(prefix=settings.API_V1_URI)
api_v1_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_v1_router.include_router(evaluation.router, prefix="/evaluations", tags=["evaluations"])
api_v1_router.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(api_v1_router)

# Global Exception Handlers
app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)
app.add_exception_handler(ForbiddenException, forbidden_exception_handler)
app.add_exception_handler(BadRequestException, bad_request_exception_handler)
app.add_exception_handler(Exception, unexpected_exception_handler)

@app.get("/")
def read_root():
    return {"message": "Welcome to the 42gg.match.server API!"}

@app.get("/test")
def test():
    raise NotFoundException(detail="Test Exception")
