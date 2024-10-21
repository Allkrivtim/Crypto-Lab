import sys
import logging
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException

from src.services.utils import get_db_pool
from database import upsert_clicker, get_user_data


router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.post(
    '/tap',
    description='Publish',
    summary='Publish',
)
async def click(
    telegram_id: int,
    user_count: int,
    user_energy: int,
    user_id: int,
    user_time: str,
    user_updatetime: str,
    user_upgrades: int,
    db_pool = Depends(get_db_pool)
):
    try:
        telegram_id = int(telegram_id)
        user_id = int(user_id)
        count = int(user_count)


        # Убедитесь, что user_time и user_updatetime - строки
        time_str = str(user_time)
        update_time_str = user_updatetime

        if isinstance(time_str, str) and isinstance(update_time_str, str):
            # Преобразуем строки в объекты datetime
            time = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
            update_time = datetime.fromisoformat(update_time_str.replace('Z', '+00:00'))
        else:
            raise ValueError("user_time и user_updatetime должны быть строками")

        upgrades = int(user_upgrades)
        energy = int(user_energy)

        # Подготовка данных для вставки или обновления
        clicker_data = {
            'user_id': user_id,
            'telegram_id': telegram_id,
            'user_count': count,
            'user_upgrades': upgrades,
            'user_time': int(time.timestamp()),  # Преобразуем в UNIX timestamp
            'user_updatetime': int(update_time.timestamp()),  # Преобразуем в UNIX timestamp
            'user_energy': energy
        }

        # Вызов функции вставки или обновления данных
        await upsert_clicker(clicker_data)

        return JSONResponse({'message': f"Данные успешно обработаны для user_id {user_id}"})
    except Exception as e:
        error = str(f"error: {e} -------{sys.exc_info()[-1].tb_lineno}")
        raise HTTPException(status_code=400, detail=f"Number string error: {error}")
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {str(e)}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Неверный тип данных: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")
