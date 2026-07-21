from fastapi import FastAPI

app = FastAPI(
    title="Project Atlas API",
    version="0.1.0",
    description="Enterprise AI platform"
)

@app.get("/")
async def root():
    return {
        "application": "Project Atlas",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }