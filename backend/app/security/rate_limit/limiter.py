import redis

from app.config.settings import get_settings

settings = get_settings()

class RateLimiter:

    MAX_REQUESTS = 10
    WINDOW_SECONDS = 60

    def __init__(self):
        self.redis = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )
    
    def allow(self, client_id: str) -> bool:

        key = f"rate limit: {client_id}"

        current_count = self.redis.incr(key)

        if current_count == 1:
            self.redis.expire(
                key,
                self.WINDOW_SECONDS
            )

        return current_count <=self.MAX_REQUESTS
    
rate_limiter = RateLimiter()