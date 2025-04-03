import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from app.core.exceptions import not_found
from app.api.v1.endpoints.blocked import router as blocked_router
from app.api.v1.endpoints.telegram import router as telegram_router
from tests.test_services.main_page import router as test_main_page_router
from tests.test_api.detect import router as test_detect_router
from app.core.logger import site_logger

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(telegram_router)
app.include_router(blocked_router)
app.include_router(test_main_page_router)
app.include_router(test_detect_router)

app.add_exception_handler(404, not_found)


if __name__ == "__main__":
  try:
    uvicorn.run(app, host="0.0.0.0", port=8000)
    site_logger.info("Server started successfully")
  except Exception as e:
    site_logger.error(f"Failed to start the server: {e}")