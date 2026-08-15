from langgraph.checkpoint.redis import RedisSaver

from app.config.settings import get_settings

settings = get_settings()

REDIS_URL = (
    f"redis://"
    f"{settings.REDIS_HOST}:"
    f"{settings.REDIS_PORT}"
)

checkpointer_context = RedisSaver.from_conn_string(
    REDIS_URL
)
checkpointer = checkpointer_context.__enter__()

checkpointer.setup()