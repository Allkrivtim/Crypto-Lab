from fastapi import FastAPI, Depends, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db, engine
from app.models import Base, User

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/lab", response_class=HTMLResponse)
async def read_root(request: Request, db: AsyncSession = Depends(get_db), user_id: int = Query(...)):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        user = User(id=user_id, tokens=0)
        db.add(user)
        await db.commit()
        await db.refresh(user)
    return templates.TemplateResponse("index.html", {"request": request, "tokens": user.tokens})

@app.post("/update_tokens")
async def update_tokens(request: Request, db: AsyncSession = Depends(get_db)):
    data = await request.json()
    user_id = data.get("user_id")
    tokens = data.get("tokens")
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if user:
        user.tokens = tokens
        db.add(user)
        await db.commit()
        await db.refresh(user)
    return {"status": "success"}
