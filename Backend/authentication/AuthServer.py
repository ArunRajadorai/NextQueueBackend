from datetime import datetime, timedelta
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
import secrets
from starlette import status

from Backend.configs import Database
from Backend.authentication import AuthModel
import logging

"Class for jwt token creation and authentication"
"Author @Arun"

# Generate a secure secret key
SECRET_KEY = secrets.token_hex(32)
print(f"SECRET_KEY: {SECRET_KEY}")

security = HTTPBearer()

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 100  #Token is set to be expired after 30 minutes

logging.basicConfig(level=logging.ERROR)


def get_db():
    db = Database.DBSession()
    try:
        yield db
    finally:
        db.close()


db = Database.DBSession()


class AuthServer:
    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        #store the authentication back to db
        update_authkey(data, encoded_jwt)
        return encoded_jwt

    @staticmethod
    def decrypt_token(cls, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            data: dict = payload.get("sub")
            if data is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
            return data
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


def update_authkey(data, encoded_jwt):
    try:
        db_auth = AuthModel.Auth(App_name=data.get("app_name"), App_password=data.get("app_password"),
                                 access_token=encoded_jwt)
        db.add(db_auth)
        db.commit()
        db.refresh(db_auth)
    except Exception as e:
        db.rollback()
        logging.error(f"Database update error : {e}")
        raise HTTPException(status_code=400, detail=f"Database update error : {e}")

