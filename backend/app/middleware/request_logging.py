import logging
import time
import uuid

from fastapi import Request

logger = logging.getLogger(__name__)

async def request_logging_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.time()

    logger.info(
        f"Request Started | request_id = {request_id}"
        f"method={request.method}"
        f"path={request.url.path}"
    )

    response = await call_next(request)

    process_time = round(time.time()-start_time,3)

    logger.info(
        f"Request Completed | request_id={request_id}"
        f"status_code={response.status_code}"
        f"duration={process_time}s"
    )

    response.headers["X-Request-ID"] = request_id

    return response