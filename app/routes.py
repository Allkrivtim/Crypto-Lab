from fastapi import APIRouter, Request, HTTPException, Query, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .database import get_db, User
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import logging

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserData(BaseModel):
    user_id: int
    tokens: int
    mining_speed: int
    auto_mining: int
    knowledge_points: int
    energy: int
    energy_recovery_speed: int

@router.get("/lab", response_class=HTMLResponse)
async def read_root(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /lab with user_id: {user_id}")
    return templates.TemplateResponse("index.html", {"request": request, "user_id": user_id})

@router.get("/page1", response_class=HTMLResponse)
async def read_page1(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /page1 with user_id: {user_id}")
    return templates.TemplateResponse("page1.html", {"request": request, "user_id": user_id})

@router.get("/page2", response_class=HTMLResponse)
async def read_page2(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /page2 with user_id: {user_id}")
    return templates.TemplateResponse("page2.html", {"request": request, "user_id": user_id})

@router.get("/page3", response_class=HTMLResponse)
async def read_page3(request: Request, user_id: int = Query(None)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Telegram ID not found")
    logger.info(f"Accessing /page3 with user_id: {user_id}")
    return templates.TemplateResponse("page3.html", {"request": request, "user_id": user_id})

@router.post("/api/sync")
async def sync_user_data(user_data: UserData, db: AsyncSession = Depends(get_db)):
    logger.info(f"Syncing data for user_id: {user_data.user_id}")
    query = select(User).filter(User.id == user_data.user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if user:
        user.tokens = user_data.tokens
        user.mining_speed = user_data.mining_speed
        user.auto_mining = user_data.auto_mining
        user.knowledge_points = user_data.knowledge_points
        user.energy = user_data.energy
        user.energy_recovery_speed = user_data.energy_recovery_speed
        
        db.add(user)
        await db.commit()
        logger.info("Data synced successfully")
        return {"status": "success"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
