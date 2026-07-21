from fastapi import FastAPI
import logging
from app.config.settings import get_settings
from app.core.logging import setup_logging
from app.middleware.request_logging import request_logging_middleware

settings = get_settings()

setup_logging()

logger = logging.getLogger(__name__)
logger.info("Starting Project Atlas API..")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise AI platform"
)
app.middleware("http")(request_logging_middleware)

@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running"
    }

@app.get("/health")
async def health():
    logger.info("Health endpoint called")
    return {
        "status": "healthy"
    }