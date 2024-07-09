from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router as app_router
from app.database import init_db

app = FastAPI()

# Подключение маршрутизатора
app.include_router(app_router)

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.on_event("startup")
async def startup_event():
    await init_db()
