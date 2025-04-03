from app.core.logger import router_logger
from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

router = APIRouter()

@router.get("/pages/blocked")
async def home(request: Request):
    return templates.TemplateResponse("pages/blocked.html", {"request": request})