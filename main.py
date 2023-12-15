import time
from random import randint

from aiogram import Bot, Dispatcher, types
from aiogram import executor

import config
import keyboard as kb

bot = Bot(token=config.TOKEN_API)
# bot = Bot(token=config.TOKEN_API, proxy='http://10.0.48.52:3128')
dp = Dispatcher(bot=bot)


# НАЧАЛО
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=config.START_TEXT, reply_markup=kb.keyb)


@dp.message_handler(text=['Информация'])
async def information_command(message: types.Message):
    await message.answer(text=config.INFORMATION_TEXT)


@dp.message_handler(text=['Начать игру'])
async def information_command(message: types.Message):
    await message.answer(text=config.START_GAME_TEXT, reply_markup=kb.persons_button)


# ВОЛШЕБНИК
@dp.callback_query_handler(lambda x: x.data == "wizard")
async def wizard_delete_button(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(callback_query.from_user.id, config.WIZARD_HISTORY)
    # Вывод дверных кнопок
    await bot.send_message(callback_query.from_user.id, config.WIZARD_START_TEXT, reply_markup=kb.doors)


# Комната 1 Дверь 1. Паук атака
@dp.callback_query_handler(lambda x: x.data == "door1")
async def wizard_room1_delete_button(callback_query: types.CallbackQuery):  # Функция с основным выводом текста
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(callback_query.from_user.id, config.SPIDER_MEETING, reply_markup=kb.battle)


# Действия при атаке 1_1
@dp.callback_query_handler(lambda x: x.data == "attack")
async def wizard_room1_attack_button(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
        w_push = randint(1, config.wizard['pw'])
        s_push = randint(1, config.spider['pw'])
        config.spider['hp'] -= w_push
        config.wizard['hp'] -= s_push

        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.spider['hp'] = 40  # Возвращаем здоровье пауку после драки

            await bot.send_message(callback_query.from_user.id, text=config.YOU_DEAD_SPIDER_WIZARD)
            break
        elif config.wizard['hp'] >= 1:  # Действия при победе над пауком
            config.spider['hp'] = 40

            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER_WIZARD)
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_WIZARD)  # Вывод здоровья
            break
    await bot.send_message(callback_query.from_user.id, text='тест')  # Тестовый вывод текста


# Действия при побеге 1_1
@dp.callback_query_handler(lambda x: x.data == "away")
async def wizard_room1_attack_button(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_WIZARD_SPIDER)
# дописать побег и продолжить вторую дверь
# понять как после побега исопользовать атаку хотя она уже есть

# РЫЦАРЬ
@dp.callback_query_handler(lambda x: x.data == "knight")
async def knight_delete_button(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(callback_query.from_user.id, config.KNIGHT_HISTORY)
    time.sleep(5)  # написать время ожидания после вывода текста
    await bot.send_message(callback_query.from_user.id, config.KNIGHT_START_TEXT)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
