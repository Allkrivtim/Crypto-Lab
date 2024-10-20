from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from handlers import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить доступ с любого источника
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (POST, GET, OPTIONS и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)

# Подключаем шаблоны Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})