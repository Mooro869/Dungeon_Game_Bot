from aiogram import types

# Кнопки при запуске бота
keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
info_button = types.KeyboardButton('Информация')
start_game = types.KeyboardButton('Начать игру')
keyb.add(info_button, start_game)

# Кнопки персонажа
persons_button = types.InlineKeyboardMarkup(row_width=2)
wizard = types.KeyboardButton("Волшебник", callback_data="wizard")
knight = types.KeyboardButton("Рыцарь", callback_data="knight")

persons_button.add(wizard, knight)
