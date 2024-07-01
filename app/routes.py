from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from .models import User

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def read_root(request: Request):
    user = User.get_or_create("default_user")
    return templates.TemplateResponse("index.html", {"request": request, "user": user})

@router.post("/collect_dust/")
async def collect_dust(request: Request):
    form = await request.json()
    user_id = form.get("user_id")
    user = User.get(user_id)
    user.tokens += 1
    user.save()
    return {"tokens": user.tokens}

@router.get("/page1/")
async def read_page1(request: Request):
    return templates.TemplateResponse("page1.html", {"request": request})

@router.get("/page2/")
async def read_page2(request: Request):
    return templates.TemplateResponse("page2.html", {"request": request})
