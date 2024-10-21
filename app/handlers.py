from fastapi import APIRouter, Body, HTTPException
from fastapi.responses import JSONResponse
from database import upsert_clicker, get_user_data
from datetime import datetime

router = APIRouter()

@router.post("/api/clicker/tap")
async def click(data=Body()):
    try:
        telegram_id = int(data['telegram_id'])
        user_id = int(data['user_id'])
        count = int(data['user_count'])

        # Убедитесь, что user_time и user_updatetime - строки
        time_str = data['user_time']
        update_time_str = data['user_updatetime']
        
        if isinstance(time_str, str) and isinstance(update_time_str, str):
            # Преобразуем строки в объекты datetime
            time = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
            update_time = datetime.fromisoformat(update_time_str.replace('Z', '+00:00'))
        else:
            raise ValueError("user_time и user_updatetime должны быть строками")

        upgrades = int(data['user_upgrades'])
        energy = int(data['user_energy'])

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

    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {str(e)}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Неверный тип данных: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")



@router.get("/api/clicker/user/{user_id}")
async def get_user(user_id: int):
    """Получение данных о пользователе по user_id"""
    try:
        user_data = await get_user_data(user_id)
        if user_data:
            return JSONResponse(user_data)
        else:
            raise HTTPException(status_code=404, detail=f"Пользователь с id {user_id} не найден")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")
