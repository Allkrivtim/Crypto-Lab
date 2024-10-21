from fastapi import APIRouter, Depends, HTTPException
import logging

from src.services.utils import get_db_pool


router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.get(
    '/{user_id}',
    description='Publish',
    summary='Publish',
)
async def get_user(
    user_id: int,
    db_pool = Depends(get_db_pool)
):
    """Получение данных о пользователе по user_id"""

    try:
        print(user_id)
        async with db_pool.acquire() as conn:
            row = await conn.fetchrow("""SELECT * FROM content.clicker
                                         WHERE telegram_id = $1""", user_id)
            return row['id']
        # user_data = await get_user_data(user_id)
        # if user_data:
        #     return JSONResponse(user_data)
        # else:
        #     raise HTTPException(status_code=404, detail=f"Пользователь с id {user_id} не найден")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")
