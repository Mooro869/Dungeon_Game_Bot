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

# Основные кнопки
battle = types.InlineKeyboardMarkup(row_width=2)
attack = types.KeyboardButton('Атаковать👊', callback_data='attack')
away = types.KeyboardButton('Сбежать🏃', callback_data='away')
battle.add(attack, away)

# Двери
doors = types.InlineKeyboardMarkup(row_width=2)
door1 = types.KeyboardButton('Первая дверь🚪', callback_data='door1')
door2 = types.KeyboardButton('Вторая дверь🚪', callback_data='door2')
doors.add(door1, door2)




