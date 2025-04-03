from app.core.logger import router_logger
from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

router = APIRouter()

@router.get("/detect")
async def home(request: Request):
    return templates.TemplateResponse("pages/blank.html", {"request": request})