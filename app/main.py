from fastapi import FastAPI
from .config import Settings
from .logging_config import init_logging

settings = Settings()
init_logging()

app = FastAPI(title="TaskMaster (starter)", version="0.1.0")


@app.get("/healthz")
async def healthz():
    """
    简单健康检查接口，Week1 的主要目标是确保这个能在本地和 CI 上跑通。
    """
    return {"status": "ok"}