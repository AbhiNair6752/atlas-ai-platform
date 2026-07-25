from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.user import Token, UserLogin
from app.services.auth_service import auth_service
from app.core.jwt import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/login", response_model=Token)
def login(
    form_data : OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = auth_service.authenticate_user(
        db,
        email=form_data.username,
        password=form_data.password,
    )

    access_token = create_access_token(
        data = {
            "sub": user.email
        }
    )

    return Token(
        access_token=access_token,
        token_type="Bearer"
    )