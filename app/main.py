from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return templates.TemplateResponse("error.html", {"request": request, "message": exc.detail}, status_code=exc.status_code)

@app.get("/lab", response_class=HTMLResponse)
async def read_root(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /lab with user_id: {user_id}")
    return templates.TemplateResponse("index.html", {"request": request, "user_id": user_id})

@app.get("/page1", response_class=HTMLResponse)
async def read_page1(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /page1 with user_id: {user_id}")
    return templates.TemplateResponse("page1.html", {"request": request, "user_id": user_id})

@app.get("/page2", response_class=HTMLResponse)
async def read_page2(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /page2 with user_id: {user_id}")
    return templates.TemplateResponse("page2.html", {"request": request, "user_id": user_id})

@app.get("/page3", response_class=HTMLResponse)
async def read_page3(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /page3 with user_id: {user_id}")
    return templates.TemplateResponse("page3.html", {"request": request, "user_id": user_id})
