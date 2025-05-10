from fastapi import APIRouter, Depends
from app.schemas.user import User
from app.dependencies import get_active_user

router = APIRouter()

@router.get("/users/me", response_model=User)
def read_users_me(user: User = Depends(get_active_user)):
    return user

@router.get("/users/me/items/")
def read_own_items(user: User = Depends(get_active_user)):
    return [{"item_id": "Foo", "owner": user.username}]
