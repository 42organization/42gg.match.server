from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.http_exceptions import NotFoundException, UnauthorizedException, ForbiddenException, BadRequestException

async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

async def unauthorized_exception_handler(request: Request, exc: UnauthorizedException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

async def forbidden_exception_handler(request: Request, exc: ForbiddenException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

async def bad_request_exception_handler(request: Request, exc: BadRequestException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

async def unexpected_exception_handler(request: Request, exc: BaseException):
    return JSONResponse(status_code=500, content={"message": "Intrenal Server Error"})

# async def custom_exception_handler(request: Request, exc: CustomException):
#     return JSONResponse(status_code=400, content={"name": exc.name, "message": exc.detail})