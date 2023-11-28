from aiogram import types

keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
info_button = types.KeyboardButton('Информация')
start_game = types.KeyboardButton('Начать игру')
keyb.add(info_button, start_game)

сharacter_button = types.InlineKeyboardMarkup(row_width=1)
wizard = types.InlineKeyboardButton("Волшебник", callback_data="wizard")
knight = types.InlineKeyboardButton("Рыцарь", callback_data="knight")
dasha = types.InlineKeyboardButton("Даша", callback_data="dasha")

сharacter_button.add(wizard, knight, dasha)
