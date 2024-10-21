import asyncpg
import asyncio

DB_CONFIG = {
    "host": "172.24.156.7",
    "user": "myuser",
    "password": "mypassword",
    "database": "mydatabase"
}

async def connect_db():
    return await asyncpg.connect(**DB_CONFIG)

async def get_user_by_id(user_id):
    """Проверка, существует ли пользователь с заданным user_id, и получение всех его данных"""
    conn = await connect_db()
    try:
        result = await conn.fetchrow('''
            SELECT * FROM clicker WHERE user_id = $1
        ''', user_id)
        return result
    finally:
        await conn.close()

async def upsert_clicker(data):
    """Вставка новой записи о пользователе или прибавление user_count к существующему значению"""
    conn = await connect_db()
    try:
        # Приведение типов данных
        user_id = int(data['user_id'])
        telegram_id = int(data['telegram_id'])
        user_count = int(data['user_count'])
        user_upgrades = int(data['user_upgrades'])
        user_time = int(data['user_time'])  # Если это временная метка, она может быть целым числом
        user_updatetime = int(data['user_updatetime'])  # Если это временная метка, она может быть целым числом
        user_energy = int(data['user_energy'])

        # Проверяем, существует ли пользователь
        existing_user = await get_user_by_id(user_id)
        
        if existing_user:
            # Если пользователь существует, прибавляем user_count к уже существующему значению
            new_user_count = existing_user['user_count'] + user_count
            await conn.execute('''
                UPDATE clicker
                SET user_count = $2, telegram_id = $3, user_upgrades = $4, user_time = $5, user_updatetime = $6, user_energy = $7
                WHERE user_id = $1
            ''', user_id, new_user_count, telegram_id, user_upgrades, user_time, user_updatetime, user_energy)
            print(f"Запись обновлена: user_id {user_id}, новое значение user_count = {new_user_count}")
        else:
            # Если пользователя нет, создаём новую запись
            await conn.execute('''
                INSERT INTO clicker (user_id, telegram_id, user_count, user_upgrades, user_time, user_updatetime, user_energy)
                VALUES ($1, $2, $3, $4, $5, $6, $7)
            ''', user_id, telegram_id, user_count, user_upgrades, user_time, user_updatetime, user_energy)
            print("Запись успешно добавлена")
    finally:
        await conn.close()


async def get_user_data(user_id):
    """Получение данных о пользователе по user_id"""
    user_data = await get_user_by_id(user_id)
    if user_data:
        return {
            'user_id': user_data['user_id'],
            'telegram_id': user_data['telegram_id'],
            'user_count': user_data['user_count'],
            'user_upgrades': user_data['user_upgrades'],
            'user_time': user_data['user_time'],
            'user_updatetime': user_data['user_updatetime'],
            'user_energy': user_data['user_energy']
        }
    else:
        return None
