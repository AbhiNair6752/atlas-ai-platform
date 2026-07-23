from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy import select
from fastapi import HTTPException

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
    
    def get_all_users(
            self,
            db: Session
    ):
        statement = select(User)
        result = db.execute(statement)
        users = result.scalars().all()

        return users
    def get_user_by_id(
            self,
            user_id: int,
            db: Session
    ):
        statement = (select(User).where(User.id==user_id))
        result = db.execute(statement)
        user = result.scalar_one_or_none()

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User Not Found"
            )
        return user    
user_service = UserService()