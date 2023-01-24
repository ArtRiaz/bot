from aiogram.types import Message, FSInputFile
from aiogram import Bot
import asyncio
from core.keyboards.reply import kb_back


async def get_diplom(message: Message, bot: Bot):
    photo1 = FSInputFile(path=r'/Users/artem/Desktop/uk_pasport.png')
    photo2 = FSInputFile(path=r'/Users/artem/Desktop/uk_diya.png')
    # Лицензия А
    await bot.send_photo(chat_id=message.from_user.id, photo=photo1, caption=' Тренерська Лiцензiя А UEFA',
                         reply_markup=kb_back())

    # Диплом Психолога
    await asyncio.sleep(3)
    await bot.send_photo(chat_id=message.from_user.id, photo=photo2, caption=' Диплом вищоï освiти: МАУП м.Киïв, Практичний психолог')
