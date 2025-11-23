from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/ping")
async def ping():
    return {"ping": "pong"}
