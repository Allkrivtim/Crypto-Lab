import asyncpg
import asyncio

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "myuser",
    "password": "mypassword",
    "database": "mydatabase"
}

#пример словаря для вставки
clicker_data = {
    'user_id': 1,
    'telegram_id': 12345,
    'user_count': 100,
    'user_upgrades': 2,
    'user_time': 1609459200,
    'user_updatetime': 1609459200,
    'user_energy': 50
}

async def connect_db():
    return await asyncpg.connect(**DB_CONFIG)

async def insert_clicker(data):
    conn = await connect_db()
    try:
        await conn.execute('''
            INSERT INTO clicker (user_id, telegram_id, user_count, user_upgrades, user_time, user_updatetime, user_energy)
            VALUES ($1, $2, $3, $4, $5, $6, $7)
        ''', data['user_id'], data['telegram_id'], data['user_count'], data['user_upgrades'], data['user_time'], data['user_updatetime'], data['user_energy'])
        print("Запись успешно добавлена")
    finally:
        await conn.close()

async def update_clicker(data):
    conn = await connect_db()
    try:
        await conn.execute('''
            UPDATE clicker
            SET telegram_id = $2, user_count = $3, user_upgrades = $4, user_time = $5, user_updatetime = $6, user_energy = $7
            WHERE user_id = $1
        ''', data['user_id'], data['telegram_id'], data['user_count'], data['user_upgrades'], data['user_time'], data['user_updatetime'], data['user_energy'])
        print("Запись успешно обновлена")
    finally:
        await conn.close()