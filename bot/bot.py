import logging
import os
import asyncio
from aiogram import Router
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram.types import Message, FSInputFile, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from id_encryption import encrypt_id

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s | %(message)s - %(asctime)s'
)
logger = logging.getLogger('Bot')

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message(Command("start"))
async def start(message: Message):
    telegram_id = str(message.from_user.id)
    encrypted_id = encrypt_id(telegram_id)
    logger.info(f"Received /start command from user {telegram_id}")
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Community",
        url="https://t.me/cryptolabgamecommunity"
    )
    builder.button(
        text="Buy crypto coins",
        callback_data="buy_coins"
    )
    builder.button(
        text="Earn crypto dust right now!",
        web_app=WebAppInfo(url=f"https://crypto-lab.website/telegram-bot/{encrypted_id}")
    )
    builder.adjust(2)
    await message.answer(
        "Greetings! We invite you to play Crypto-Lab:",
        reply_markup=builder.as_markup()
    )

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
    else:
        logger.info("Bot successfully started")

if __name__ == "__main__":
    asyncio.run(main())