
from fastapi import FastAPI
from backend.api import routes
from backend.api.telegram_bot import start_bot

app = FastAPI()

app.include_router(routes.router)

@app.on_event("startup")
async def startup_event():
    await start_bot()

@app.get("/ping")
async def ping():
    return {"message": "pong"}
