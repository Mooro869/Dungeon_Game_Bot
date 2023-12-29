from aiogram import types

# Кнопки при запуске бота
keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
info_button = types.KeyboardButton('Информация')
start_game = types.KeyboardButton('Начать игру')
keyb.add(info_button, start_game)

# Кнопки персонажей
persons_button = types.InlineKeyboardMarkup(row_width=2)
wizard = types.KeyboardButton("Волшебник🧙‍♂️", callback_data="wizard")
knight = types.KeyboardButton("Рыцарь⚔️", callback_data="knight")
persons_button.add(wizard, knight)

# ВСЕ ОСНОВНЫЕ КНОПКИ ДЛЯ КАЖДОЙ ДВЕРИ
# Основные кнопки 1_1
battle1_1 = types.InlineKeyboardMarkup(row_width=2)
attack1_1 = types.KeyboardButton('Атаковать👊', callback_data='attack1_1')
away1_1 = types.KeyboardButton('Сбежать🏃', callback_data='away1_1')
battle1_1.add(attack1_1, away1_1)

# Основные кнопки 1_2
battle1_2 = types.InlineKeyboardMarkup(row_width=2)
attack1_2 = types.KeyboardButton('Атаковать👊', callback_data='attack1_2')
away1_2 = types.KeyboardButton('Сбежать🏃', callback_data='away1_2')
battle1_2.add(attack1_2, away1_2)

# Основные кнопки 2_1
battle2_1 = types.InlineKeyboardMarkup(row_width=2)
attack2_1 = types.KeyboardButton('Атаковать👊', callback_data='attack2_1')
away2_1 = types.KeyboardButton('Сбежать🏃', callback_data='away2_1')
battle2_1.add(attack2_1, away2_1)

# Основные кнопки 2_2
battle2_2 = types.InlineKeyboardMarkup(row_width=2)
attack2_2 = types.KeyboardButton('Атаковать👊', callback_data='attack2_2')
away2_2 = types.KeyboardButton('Сбежать🏃', callback_data='away2_2')
battle2_2.add(attack2_2, away2_2)

# Основные кнопки 3_1
battle3_1 = types.InlineKeyboardMarkup(row_width=2)
attack3_1 = types.KeyboardButton('Атаковать👊', callback_data='attack3_1')
away3_1 = types.KeyboardButton('Сбежать🏃', callback_data='away3_1')
battle3_1.add(attack3_1, away3_1)

# Основные кнопки 3_2
battle3_2 = types.InlineKeyboardMarkup(row_width=2)
attack3_2 = types.KeyboardButton('Атаковать👊', callback_data='attack3_2')
away3_2 = types.KeyboardButton('Сбежать🏃', callback_data='away3_2')
battle3_2.add(attack3_2, away3_2)

# Основные кнопки 4_1
battle4_1 = types.InlineKeyboardMarkup(row_width=2)
attack4_1 = types.KeyboardButton('Атаковать👊', callback_data='attack4_1')
away4_1 = types.KeyboardButton('Сбежать🏃', callback_data='away4_1')
battle4_1.add(attack4_1, away4_1)

# Основные кнопки 4_2
battle4_2 = types.InlineKeyboardMarkup(row_width=2)
attack4_2 = types.KeyboardButton('Атаковать👊', callback_data='attack4_2')
away4_2 = types.KeyboardButton('Сбежать🏃', callback_data='away4_2')
battle4_2.add(attack4_2, away4_2)

# Основные кнопки 5
battle5 = types.InlineKeyboardMarkup(row_width=2)
attack5 = types.KeyboardButton('Атаковать👊', callback_data='attack5')
battle5.add(attack5)  # будет только кнопка атаки, так как сражение против босса

# КНОПКИ ВСЕХ ДВЕРЕЙ
# Дверь 1
doors1 = types.InlineKeyboardMarkup(row_width=2)
door1_1_1 = types.KeyboardButton('Первая дверь🚪', callback_data='door1_1_1')
door2_1_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='door2_1_2')
doors1.add(door1_1_1, door2_1_2)

# Дверь 2
doors2 = types.InlineKeyboardMarkup(row_width=2)
door1_2_1 = types.KeyboardButton('Первая дверь🚪', callback_data='door1_2_1')
door2_2_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='door2_2_2')
doors2.add(door1_2_1, door2_2_2)

# Дверь 3
doors3 = types.InlineKeyboardMarkup(row_width=2)
door1_3_1 = types.KeyboardButton('Первая дверь🚪', callback_data='door1_3_1')
door2_3_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='door2_3_2')
doors3.add(door1_3_1, door2_3_2)

# Дверь 4
doors4 = types.InlineKeyboardMarkup(row_width=2)
door1_4_1 = types.KeyboardButton('Первая дверь🚪', callback_data='door1_4_1')
door2_4_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='door2_4_2')
doors4.add(door1_1_1, door2_4_2)

# Дверь 5
doors5 = types.InlineKeyboardMarkup(row_width=2)
door5 = types.KeyboardButton('Финальная дверь🚪', callback_data='door5')
doors5.add(door5)
