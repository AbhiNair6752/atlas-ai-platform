from app.security.rate_limit.limiter import rate_limiter


client_id = "rate-test-001"

for i in range(12):

    allowed = rate_limiter.allow(client_id)

    print(
        f"Request {i + 1}: "
        f"{'ALLOWED' if allowed else 'BLOCKED'}"
    )