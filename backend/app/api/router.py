from app.api.routes.health import router as health_router
from app.api.routes.user import router as user_router
from app.api.routes.auth import router as auth_router
from app.api.routes.chat import router as chat_router
from app.api.routes.document import router as document_router
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

router.include_router(
    chat_router,
    tags=["AI chat"]
)

router.include_router(
    document_router,
    tags=["Documents"]
)