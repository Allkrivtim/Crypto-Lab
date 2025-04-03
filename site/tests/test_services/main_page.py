from app.core.logger import router_logger
from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

router = APIRouter()

@router.get("/main_page")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})