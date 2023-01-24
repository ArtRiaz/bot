from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def kb_menu():
    kb = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text='Про мене')],
        [KeyboardButton(text='Моï дипломи та лiцензiï')],
        [KeyboardButton(text='Фотогалерея')],
        [KeyboardButton(text='Моï контакти')
         ]], resize_keyboard=True, one_time_keyboard=True)

    return kb


def kb_back():
    kb = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text='Повернутись на головне меню')
    ]], resize_keyboard=True, one_time_keyboard=True)

    return kb
