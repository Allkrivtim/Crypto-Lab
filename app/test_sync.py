import asyncpg
import asyncio

async def test_connection():
    try:
        conn = await asyncpg.connect(
            user='myuser', password='mypassword',
            database='mydatabase', host='localhost', port=5432
        )
        print("Connection successful")
        await conn.close()
    except Exception as e:
        print(f"Connection error: {e}")

asyncio.run(test_connection())