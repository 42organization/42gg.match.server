from app.schemas.auth import FortyTwoToken
from pydantic import BaseModel

class User(BaseModel):
    forty_two_id : int
    intra_id: str
    profile_image: str
    email: str
    forty_two_access_token: FortyTwoToken