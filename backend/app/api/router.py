from app.api.routes.health import router as health_router
from app.api.routes.user import router as user_router
from app.api.routes.auth import router as auth_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(
    health_router,
    tags=["Health"]
)
router.include_router(
    user_router,
    tags=["User"]
)

router.include_router(
    auth_router,
    tags=["Authentication"]
)