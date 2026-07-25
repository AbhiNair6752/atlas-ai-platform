from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.user import Token, UserLogin
from app.services.auth_service import auth_service
from app.core.jwt import create_access_token

router = APIRouter()