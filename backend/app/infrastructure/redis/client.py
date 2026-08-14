import redis

from app.config.settings import get_settings

settings = get_settings()

class RedisClient:

    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )
    
    def ping(self) -> bool:
        return self.client.ping()


redis_client = RedisClient()