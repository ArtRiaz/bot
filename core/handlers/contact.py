from aiogram.types import Message, CallbackQuery
from aiogram import Bot
from core.keyboards.inline import ikb_contact_menu
from core.keyboards.reply import kb_menu


async def get_contact(message: Message):
    await message.answer("Як зi мною зв'язатись:", reply_markup=ikb_contact_menu())


async def get_number_phone(call: CallbackQuery):
    await call.message.answer_contact(phone_number='0769766710', first_name='Артем', last_name='Рязанцев')


async def get_location(call: CallbackQuery):
    await call.message.answer_location(latitude=48.5735615, longitude=7.7140432)

async def back_to_menu(call: CallbackQuery):
    await call.message.answer(text='Ви повернулись у головне меню',reply_markup=kb_menu())
