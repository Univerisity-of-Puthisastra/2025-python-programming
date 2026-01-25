from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

basic_auth = HTTPBasic()

def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(basic_auth)):
    username, password = "admin", "password"

    if credentials.username != username or credentials.password != password:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return credentials.username