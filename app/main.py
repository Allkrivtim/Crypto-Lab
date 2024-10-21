from fastapi import FastAPI
from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
# from handlers import router
from fastapi.middleware.cors import CORSMiddleware
import logging
import asyncpg
import uvicorn

from src.api.v1 import tap, user
from src.services import utils


logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title='Project name',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить доступ с любого источника
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (POST, GET, OPTIONS и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(tap.router, prefix='/api/clicker', tags=['Api Clicker'])
app.include_router(user.router, prefix='/api/clicker/user', tags=['User'])

# Подключаем шаблоны Jinja2
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.on_event('startup')
async def startup():
    utils.db_pool = await asyncpg.create_pool(
        host='postgres',
        port=5432,
        user='myuser',
        password='mypassword',
        database='mydatabase',
        min_size=1,
        max_size=20,
        max_queries=50000,
        max_inactive_connection_lifetime=300,
        statement_cache_size=0,
    )


@app.on_event('shutdown')
async def shutdown():
    await utils.db_pool.close()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
    )