from app.core.logger import router_logger
from fastapi import APIRouter
from fastapi.requests import Request

router = APIRouter()

@router.get("/main_page")
async def home(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})