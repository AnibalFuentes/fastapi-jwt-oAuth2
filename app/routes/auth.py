from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.services.auth_service import authenticate_user
from app.schemas.token import Token
from app.core.security import create_access_token
from app.core.config import settings
from app.models.user import fake_users_db
router = APIRouter()

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
