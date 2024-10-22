from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.responses import JSONResponse
from datetime import datetime
from src.services.utils import get_db_pool
from database import upsert_clicker

router = APIRouter()

@router.post(
    '/tap',
    description='Publish',
    summary='Publish',
)
async def click(
    telegram_id: int = Body(...),
    user_count: int = Body(...),
    user_energy: int = Body(...),
    user_id: int = Body(...),
    user_time: int = Body(...),
    user_updatetime: str = Body(...),
    user_upgrades: int = Body(...),
    db_pool=Depends(get_db_pool)
):
    try:
        # Если `user_time` — это метка времени UNIX, преобразуем ее через fromtimestamp()
        if isinstance(user_time, int):
            time = datetime.fromtimestamp(user_time)
        else:
            # Если это строка, то пытаемся преобразовать из ISO формата
            time = datetime.fromisoformat(user_time.replace('Z', '+00:00'))

        # Преобразуем `user_updatetime` из ISO 8601
        update_time = datetime.fromisoformat(user_updatetime.replace('Z', '+00:00'))

        # Подготовка данных для вставки или обновления
        clicker_data = {
            'user_id': user_id,
            'telegram_id': telegram_id,
            'user_count': user_count,
            'user_upgrades': user_upgrades,
            'user_time': int(time.timestamp()),  # Преобразуем в UNIX timestamp
            'user_updatetime': int(update_time.timestamp()),  # Преобразуем в UNIX timestamp
            'user_energy': user_energy
        }

        # # Вызов функции вставки или обновления данных
        # await upsert_clicker(clicker_data)

        return JSONResponse({'message': f"Данные успешно обработаны для user_id {user_id}"})

    except ValueError as e:
        error = str(f"Ошибка преобразования даты или данных: {e}")
        raise HTTPException(status_code=400, detail=error)

    except Exception as e:
        # Отлавливаем общие ошибки
        error = str(f"Ошибка: {e} на строке {sys.exc_info()[-1].tb_lineno}")
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {error}")
