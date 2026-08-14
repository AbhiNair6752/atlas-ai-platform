from app.infrastructure.redis.client import redis_client

print("redis connection:", redis_client.ping())