import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram import Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from config import BOT_TOKEN, NGROK_URL, COMMUNITY_LINK

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

@router.message(Command("start"))
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Играть в Крипто-лабораторию",
                web_app=WebAppInfo(url=f"{NGROK_URL}/lab/?user_id={message.from_user.id}")
            )
        ],
        [
            InlineKeyboardButton(
                text="Telegram канал сообщества",
                url=COMMUNITY_LINK
            )
        ]
    ])
    await message.answer("Приветствуем вас! Предлагаем вам поиграть в Крипто-лабораторию:", reply_markup=keyboard)

async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())