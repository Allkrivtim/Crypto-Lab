from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from app.config import API_TOKEN, NGROK_URL, COMMUNITY_LINK

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def send_welcome(message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Играть в Крипто-лабораторию",
                web_app=WebAppInfo(url=f"{NGROK_URL}/lab/?user_id={message.from_user.id}")
                #web_app=WebAppInfo(url=f"{NGROK_URL}/lab")
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
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
