import fastapi
from fastapi import File, UploadFile

userRoutes = fastapi.APIRouter()

@userRoutes.get("/users")
def get_users():
    return {"message": "Hello World"}


@userRoutes.get("/fileupload")
def fileupload(file: UploadFile = File(...)):
    return {"message": "File uploaded successfully", "file_name": file.filename}