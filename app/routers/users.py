from fastapi import APIRouter
from app.database import users
from app.database.models import userModel

router = APIRouter()

@router.get("/")
async def list_users():
    result = await users.list_users()
    return {"status":"true", "message": "Smart Services Api server is running", 'data': result}

@router.post("/")
async def create_user(
    input_user: userModel.UserCreate
):
    result = await users.create_user(input_user)
    return {"status":"true", "message": "Smart Services Api server is running", 'data': result}