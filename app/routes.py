from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import text
from app.database import get_session  # Импортируем get_session
from starlette.templating import Jinja2Templates
from starlette.responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/page1", response_class=HTMLResponse)
async def read_page1(request: Request):
    return templates.TemplateResponse("page1.html", {"request": request})

@router.get("/page2", response_class=HTMLResponse)
async def read_page2(request: Request):
    return templates.TemplateResponse("page2.html", {"request": request})

@router.get("/page3", response_class=HTMLResponse)
async def read_page3(request: Request):
    return templates.TemplateResponse("page3.html", {"request": request})
