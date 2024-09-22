import jwt
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

SECRET_KEY = 'secret'
ALGORITHM = "HS256"
scheme = OAuth2PasswordBearer(tokenUrl="token")
token_depends = Annotated[str,Depends(scheme)]

def handle_token(token: token_depends):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

verify_token = Annotated[str, Depends(handle_token)]