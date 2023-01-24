from aiogram.types import Message, FSInputFile
from aiogram import Bot
from core.keyboards.reply import kb_back


async def get_about_me(messsage: Message, bot: Bot):
    photo = FSInputFile(path=r'/Users/artem/Desktop/portfolio.jpeg')
    await bot.send_photo(messsage.chat.id, photo=photo,
                         caption=f'Мене звати Рязанцев Артем,\n'
                                 'я тренер з футболу. Тренерський досвiд роботи 14 рокiв.\n'
                                 'Працював з дiтьми та дорослими профiciйними командами у мiстi Одеса.\n'
                                 'У Францii працюю у клубах тренером \nFCOSK 06 м.Страсбург, та тренером i координатором FC Saverne.\n'
                                 'Маю два дипломи вищоï освiти Практичного психолога та Педагога з фiзичноï культури,\n'
                                 'також маю футбольну тренерську\nлiцензiю А UEFA та рiзнi стажування у профiсiйних клубах Германii,Польшi,Голандii.\n'
                                 'Дуже полюбляю працювати з дiтьми i знаходить у кожноï дитини потенцiал, давати не лише фiзичну освiту,а й духовний розвиток, впевненiсть у своïх силах та внутрiшню дисциплiну,бо це дуже важливо у наш час.\n'
                                 '<b>Приеднуйтесь до нас!</b>', reply_markup=kb_back()
                         )
