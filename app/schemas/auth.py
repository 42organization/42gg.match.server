from pydantic import BaseModel
class FortyTwoToken(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    scope: str
    created_at: int