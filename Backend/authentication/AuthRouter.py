from fastapi import APIRouter, HTTPException, status, Header, Depends
from fastapi.logger import logger
from fastapi.security import HTTPAuthorizationCredentials
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import timedelta
from Backend.authentication.AuthServer import AuthServer, ACCESS_TOKEN_EXPIRE_MINUTES, \
    security, SECRET_KEY, ALGORITHM  # Import the AuthServer class
from Backend.authentication.AuthSchema import AppSignIn, AppSignInResponse, JwtResponse

authrouter = APIRouter()

"Class for handling auth objects = Author @Arun"
"Author @Arun"

__private_static_appname = "nextQueue"


@authrouter.post("/auth-token", response_model=AppSignInResponse)
def user_login(sign_in: AppSignIn):
    # Dummy validation for illustration
    if sign_in.username != __private_static_appname or sign_in.password != "v1":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthServer.create_access_token(
        data={"app_name": sign_in.username, "app_password": sign_in.password}, expires_delta=access_token_expires
    )

    return AppSignInResponse(token=access_token)


#"Verify & Decrypt Auth token"
@authrouter.post("/verify-token", response_model=JwtResponse)
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        # payload = AuthServer.decrypt_token(token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Define the keys you want to extract from the payload
        keys_to_extract = ["app_name", "app_password"]

        # Extract the values and store them in a dictionary
        data = {key: payload.get(key) for key in keys_to_extract}
        if data is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return JwtResponse(data=data)
    except JWTError as e:
        logger.error(f"Parsing error occurred: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Parsing error occurred")
