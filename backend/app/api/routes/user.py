from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate, MessageResponse
from app.services.user_service import user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "",
    response_model=UserResponse
)
async def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    return user_service.create_user(
        user_data=user_data,
        db=db
    )

@router.get(
    "",
    response_model=list[UserResponse]
)
async def get_all_users(
    db: Session = Depends(get_db)
):
    return user_service.get_all_users(db)


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
async def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):
    return user_service.get_user_by_id(
        user_id=user_id,
        db=db
    )

@router.put(
    "/{user_id}",
    response_model=UserResponse
)
async def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    return user_service.update_user(
        user_id=user_id,
        user_data=user_data,
        db=db
    )

@router.delete("/{user_id}", response_model=MessageResponse)
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return user_service.delete_user(
        user_id=user_id,
        db=db
    )
