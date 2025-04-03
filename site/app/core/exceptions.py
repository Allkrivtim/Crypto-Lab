from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.core.logger import router_logger

templates = Jinja2Templates(directory="templates")

async def not_found(request: Request, exc):
    router_logger.error(f"404 error for {request.url}")
    return templates.TemplateResponse("pages/404.html", {"request": request})