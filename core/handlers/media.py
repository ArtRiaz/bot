from aiogram.types import InputMediaPhoto, InputMediaVideo, FSInputFile
from aiogram.types import Message
from aiogram import Bot
from core.keyboards.reply import kb_back


async def get_mediagroup(message: Message, bot: Bot):
    photo_1 = InputMediaPhoto(type='photo', media=FSInputFile(r'/Users/artem/Desktop/d1.jpeg'),
                              caption='I Feel Good😀'
                                      '')
    photo_2 = InputMediaPhoto(type='photo', media=FSInputFile(r'/Users/artem/Desktop/d2.jpeg'),
                              caption='Кубок мicта Черноморск ')

    photo_3 = InputMediaPhoto(type='photo', media=FSInputFile(r'/Users/artem/Desktop/d3.jpeg'),
                              caption='Маленькi чемпиони')
    video = InputMediaVideo(type='video',
                            media=FSInputFile(r'/Users/artem/Desktop/vid1.mp4'),
                            caption='Тренувальний процесс')
    media = [photo_1, photo_2, photo_3 , video]
    await bot.send_media_group(message.chat.id, media)
    await bot.send_message(chat_id=message.from_user.id, text='Чудовi спогади', reply_markup=kb_back())

