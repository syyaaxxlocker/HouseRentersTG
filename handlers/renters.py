import aiohttp
import handlers.keyboards as kb
from utils.get_number_emoji import get_number_emoji as emoji
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.reply(text=f'Привет, {message.from_user.first_name}', reply_markup=kb.main)

@router.message(F.text == 'Подселенцы')
async def get_renters(message: Message):
    dataUrl = "https://raw.githubusercontent.com/syyaaxxlocker/renters/refs/heads/main/renters.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(dataUrl) as response:
            responseJson = await response.json(content_type='text/plain')

    renters = ''
    for i, value in enumerate(responseJson):
        renters = renters + f"{emoji(i + 1)} - `{value['nick']}` - *{value['paidUntil']}* - {value['perHours']}/час\n"
    await message.answer(text=f"🏠Состояние комнат\n\nКомната - Арендатор - Окончание аренды - Ставка\n{renters}", parse_mode=ParseMode.MARKDOWN)
        
    
