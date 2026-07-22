from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

class UserService:

    def create_user(
            self,
            user_data: UserCreate,
            db: Session
    ):
        user = User(
            email=user_data.email,
            full_name=user_data.full_name
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user