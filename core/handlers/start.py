from aiogram.types import Message, FSInputFile
from core.utils.dbconnect import Request
from aiogram import Bot
from core.keyboards.reply import kb_menu


async def get_start(message: Message, request: Request, bot: Bot):
    photo = FSInputFile(path=r'/Users/artem/Desktop/start_id.jpeg')
    await bot.send_photo(message.chat.id, photo=photo)
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await message.answer(f'Ласкаво просимо {message.from_user.first_name} на мiй профiль! \n'
                         f'Я тренер та манеджер по футболу з Украïни', reply_markup=kb_menu())
