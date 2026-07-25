from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.models.user import User
from fastapi import HTTPException
from app.core.security import verify_password

class AuthService:
    def authenticate_user(
            self,
            db:Session,
            user_login: UserLogin
    ):
        user = (
            db.query(User)
            .filter(User.email == user_login.email)
            .first()
        )
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )
        if not verify_password(
            user_login.password,
            user.hashed_password
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )
        return user
auth_service = AuthService()