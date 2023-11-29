from aiogram import types

keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
info_button = types.KeyboardButton('Информация')
start_game = types.KeyboardButton('Начать игру')
keyb.add(info_button, start_game)

persons_button = types.InlineKeyboardMarkup(row_width=1)
wizard = types.InlineKeyboardButton("Волшебник", callback_data="wizard")
knight = types.InlineKeyboardButton("Рыцарь", callback_data="knight")
priest = types.InlineKeyboardButton("Священник", callback_data="priest")

persons_button.add(wizard, knight, priest)
