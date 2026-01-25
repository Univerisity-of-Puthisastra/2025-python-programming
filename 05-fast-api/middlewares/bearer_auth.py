from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt_utils import verify_token

bearer_auth = HTTPBearer()

def verify_bearer_auth(credentials: HTTPAuthorizationCredentials = Depends(bearer_auth)):
    token = credentials.credentials
    payload = verify_token(token)
    return payload