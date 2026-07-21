import logging
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AtlasException

logger = logging.getLogger(__name__)

async def atlas_exception_handler(
        request: Request,
        exc: AtlasException
):
    logger.warning(exc.message)

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message,
        },
        
    )