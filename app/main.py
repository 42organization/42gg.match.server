from fastapi import FastAPI
from app.api.v1.endpoints import auth, evaluation, user

app = FastAPI(    title="42gg.match.server API",
    description="API documentation for 42gg.match.server",
    version="0.1.0",
    docs_url="/api/docs",  # Swagger UI 경로 설정
    redoc_url="/api/redoc"  # ReDoc 경로 설정
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(evaluation.router, prefix="/evaluations", tags=["evaluations"])
app.include_router(user.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the 42gg.match.server API!"}
