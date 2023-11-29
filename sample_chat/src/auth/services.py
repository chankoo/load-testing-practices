from datetime import datetime, timedelta, UTC
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from src.auth import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 30 * 60


def create_access_token(data: dict):
    raw = data.copy()
    expire = datetime.now(UTC) + timedelta(seconds=ACCESS_TOKEN_EXPIRE)
    raw.update({"exp": expire})
    encoded = jwt.encode(raw, SECRET_KEY, ALGORITHM)
    return encoded


def verify_access_token(token: str, credentials_exception: Exception) -> schemas.TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme)) -> int:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials", headers={"WWW-Authenticate": "Bearer"})
    token_data = verify_access_token(token, credentials_exception)
    return token_data.id
