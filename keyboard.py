from aiogram import types

keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
info_button = types.KeyboardButton('Информация')
start_game = types.KeyboardButton('Начать игру')
keyb.add(info_button, start_game)
