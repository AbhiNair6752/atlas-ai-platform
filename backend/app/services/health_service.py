class HealthService:
    def get_health(self):
        return {
            "status": "healthy"
        }

health_service = HealthService()