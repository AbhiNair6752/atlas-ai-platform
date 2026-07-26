from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user import User
from app.core.security import verify_password


class AuthService:
    def authenticate_user(
        self,
        db: Session,
        email: str,
        password: str,
    ):
        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        return user


auth_service = AuthService()