import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from handlers import renters

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token="8288904305:AAHpwvRNJ5N4wTMHpTNUwn5oXvY51NfptuI")
    dp = Dispatcher()
    
    dp.include_routers(renters.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
