from aiogram import Bot
from aiogram.enums import ParseMode

async def notify_admin(bot: Bot, message):
    
    if message.from_user.id != 1956887942:
        await bot.send_message(
            chat_id=1956887942,
            text=f"❗Бот был кем-то запущен. Данные о пользователе:\n\n"
                 f"Full name: `{message.from_user.full_name}`\n"
                 f"Telegram ID: `{message.from_user.id}`\n"
                 f"Username: {message.from_user.username or 'Unknown'}\n"
                 f"Is premium: {message.from_user.is_premium}\n"
                 f"Запущен: {message.date}\n",
            parse_mode=ParseMode.MARKDOWN
        )
    
