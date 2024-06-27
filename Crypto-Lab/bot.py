import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import API_TOKEN, WEB_APP_URL, COMMUNITY_CHANNEL_URL
from aiogram.filters import CommandStart

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Обработчик команды /start
@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    buttons = [
        InlineKeyboardButton(text="Играть в Крипто Лабораторию", web_app=WebAppInfo(url=WEB_APP_URL)),
        InlineKeyboardButton(text="Канал сообщества", url=COMMUNITY_CHANNEL_URL)
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])

    await message.answer("Приветствуем вас! Предлагаем вам поиграть в Крипто Лабораторию:", reply_markup=keyboard)


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
