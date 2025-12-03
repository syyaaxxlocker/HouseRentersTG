import asyncio
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from handlers import renters

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(filename)s - %(message)s")

load_dotenv()

TOKEN = os.getenv("TOKEN_BOT")

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    dp.include_routers(renters.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
