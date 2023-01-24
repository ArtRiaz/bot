from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def ikb_contact_menu():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Telegram', url='tg://user?id=1064938479'),
        InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/artemriazantsev22/')

    ], [
        InlineKeyboardButton(text='Мiй номер', callback_data='contact'),
        InlineKeyboardButton(text='Наша Локацiя', callback_data='location')
    ], [
        InlineKeyboardButton(text='Головне меню', callback_data='menu')
    ]])

    return ikb
