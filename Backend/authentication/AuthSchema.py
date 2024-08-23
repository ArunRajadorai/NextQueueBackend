from typing import Dict, Any

from pydantic import BaseModel

"Class for handling auth objects"
"Author @Arun"


class AppSignIn(BaseModel):
    username: str
    password: str


class AppSignInResponse(BaseModel):
    token: str


class JwtResponse(BaseModel):
    data: Dict[str, Any]
