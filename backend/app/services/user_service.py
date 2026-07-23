from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
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
    def update_user(
            self,
            user_id: int,
            user_data: UserUpdate,
            db: Session
    ):
        user = self.get_user_by_id(
            user_id=user_id,
            db=db
        )
        user.email = user_data.email
        user.full_name = user_data.full_name

        db.commit()
        db.refresh(user)
        return user   
user_service = UserService()