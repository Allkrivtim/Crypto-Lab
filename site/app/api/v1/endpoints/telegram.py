from app.core.logger import router_logger
from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from app.utils.id_decryption import decrypt_id

router = APIRouter()

@router.get("/telegram-bot/{encrypted_id}")
async def home(request: Request):
    try:
        telegram_id = decrypt_id(encrypted_id)
        logger.info(f"Home endpoint accessed for user {telegram_id}")
        return templates.TemplateResponse("pages/index.html", {"request": request})
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return {"message": "Internal server error"}