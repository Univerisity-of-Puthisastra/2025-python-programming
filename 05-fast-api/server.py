import fastapi
from routes.users import userRoutes
from fastapi import Depends, HTTPException, Response
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
# import uvicorn
from middlewares.basic_auth import verify_basic_auth
from middlewares.bearer_auth import verify_bearer_auth
from utils.jwt_utils import create_access_token

webapp = fastapi.FastAPI()
webapp.include_router(userRoutes)
@webapp .get("/api/v1/test")
def home_page(payload: str = Depends(verify_basic_auth)):
    # http_response = fastapi.responses.PlainTextResponse(content='<h1>Hello World</h1>', status_code=200)
    # return {"message": "Hello World"}
    # return HTMLResponse(status_code=200, content="Error Not Found") 
    content = f"<html><body><h1>Login User: {payload}</h1><p>This is fully customizable.</p></body></html>"
    headers = {
        "X-Custom-Header": "Fully-Customizable",
        "Server-Status": "Excellent"
    }
    
    return Response(
        content=content, 
        status_code=200, 
        headers=headers,
        media_type="text/html"
    ) 

@webapp.post("/api/v1/login")
def login(request: dict):
    username = request.get("username")
    password = request.get("password")
    print(request)
    if username == "admin" and password == "password":
        token = create_access_token({"username": username})
        return {"message": "Login successful", "token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@webapp .get("/api/v1/test/jwt")
def home_page(payload: dict = Depends(verify_bearer_auth)):
    # http_response = fastapi.responses.PlainTextResponse(content='<h1>Hello World</h1>', status_code=200)
    # return {"message": "Hello World"}
    # return HTMLResponse(status_code=200, content="Error Not Found") 
    print(payload)
    content = f"<html><body><h1>Login User: {payload}</h1><p>This is fully customizable.</p></body></html>"
    headers = {
        "X-Custom-Header": "Fully-Customizable",
        "Server-Status": "Excellent"
    }
    
    return Response(
        content=content, 
        status_code=200, 
        headers=headers,
        media_type="text/html"
    ) 