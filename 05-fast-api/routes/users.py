import fastapi

userRoutes = fastapi.APIRouter()

@userRoutes.get("/users")
def get_users():
    return {"message": "Hello World"}