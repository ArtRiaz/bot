from aiogram import Bot, Dispatcher
import asyncio
import logging
from core.handlers import start
from aiogram.filters import CommandStart
from core.settings import settings
import asyncpg
from core.utils.commands import set_commands
from aioredis import Redis
from aiogram.fsm.storage.redis import RedisStorage
from core.middlewares.dbmiddleware import DbSession
from core.handlers import about_me
from core.handlers import diploms
from core.handlers import media
from core.handlers import contact
from core.handlers import back
from aiogram import F

async def startup(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')


async def create_pool():
    return await asyncpg.create_pool(user=settings.db.db_user, password=settings.db.dp_password,
                                     database=settings.db.db_database, host=settings.db.db_host,
                                     port=5432, command_timeout=60)


async def start_bot():
    logging.basicConfig(level=logging.INFO,
                        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    redis = Redis()
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher(storage=RedisStorage(redis=redis))
    pool_connect = await create_pool()

    # Middleware
    dp.update.middleware.register(DbSession(pool_connect))



    # Handlers
    dp.startup.register(startup)
    dp.shutdown.register(stop_bot)
    dp.message.register(start.get_start, CommandStart())
    dp.message.register(about_me.get_about_me, F.text == 'Про мене')
    dp.message.register(diploms.get_diplom, F.text == 'Моï дипломи та лiцензiï')
    dp.message.register(media.get_mediagroup, F.text == 'Фотогалерея')
    dp.message.register(contact.get_contact, F.text == 'Моï контакти')
    dp.callback_query.register(contact.get_number_phone, F.data == 'contact')
    dp.callback_query.register(contact.get_location, F.data == 'location')
    dp.callback_query.register(contact.back_to_menu, F.data == 'menu')
    dp.message.register(back.get_back)





    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start_bot())
