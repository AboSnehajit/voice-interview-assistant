from fastapi import APIRouter
from app.models.user_model import User

router =APIRouter()

@router.post("/users")
def create_user(user: User):
    return {
        "message":"User created successfully",
        "user": user
    } 