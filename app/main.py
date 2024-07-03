from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware
import logging
import os
import hashlib

app = FastAPI()

# Debugging information
staticfiles_path = os.path.abspath("app/staticfiles")
print(f"Static files path: {staticfiles_path}")
assert os.path.exists(staticfiles_path), "Static files directory does not exist"

app.mount("/staticfiles", StaticFiles(directory=staticfiles_path), name="staticfiles")
templates = Jinja2Templates(directory="app/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify the allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_file_hash(filepath):
    with open(filepath, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    return file_hash

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return templates.TemplateResponse("error.html", {"request": request, "message": exc.detail}, status_code=exc.status_code)

@app.get("/lab", response_class=HTMLResponse)
async def read_root(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /lab with user_id: {user_id}")
    styles_hash = get_file_hash("app/staticfiles/styles.css")
    script_hash = get_file_hash("app/staticfiles/script.js")
    return templates.TemplateResponse("index.html", {
        "request": request,
        "user_id": user_id,
        "styles_hash": styles_hash,
        "script_hash": script_hash
    })

@app.get("/page1", response_class=HTMLResponse)
async def read_page1(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /page1 with user_id: {user_id}")
    styles_hash = get_file_hash("app/staticfiles/styles.css")
    script_hash = get_file_hash("app/staticfiles/script.js")
    return templates.TemplateResponse("page1.html", {
        "request": request,
        "user_id": user_id,
        "styles_hash": styles_hash,
        "script_hash": script_hash
    })

@app.get("/page2", response_class=HTMLResponse)
async def read_page2(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /page2 with user_id: {user_id}")
    styles_hash = get_file_hash("app/staticfiles/styles.css")
    script_hash = get_file_hash("app/staticfiles/script.js")
    return templates.TemplateResponse("page2.html", {
        "request": request,
        "user_id": user_id,
        "styles_hash": styles_hash,
        "script_hash": script_hash
    })

@app.get("/page3", response_class=HTMLResponse)
async def read_page3(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /page3 with user_id: {user_id}")
    styles_hash = get_file_hash("app/staticfiles/styles.css")
    script_hash = get_file_hash("app/staticfiles/script.js")
    return templates.TemplateResponse("page3.html", {
        "request": request,
        "user_id": user_id,
        "styles_hash": styles_hash,
        "script_hash": script_hash
    })
