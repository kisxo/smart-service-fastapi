from fastapi import APIRouter
from app.database import users

router = APIRouter()

@router.get("/")
async def list_users():
    result = await users.list_users()
    return {"status":"true", "message": "Smart Services Api server is running", 'data': result}