from aiogram.types import Message
from core.keyboards.reply import kb_menu


async def get_back(message: Message):
    await message.answer('Ви повернулись у головне меню', reply_markup=kb_menu())
