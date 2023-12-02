from random import randint
import time
from aiogram import Bot, Dispatcher, types
from aiogram import executor

import config
import keyboard as kb


# bot = Bot(token=config.TOKEN_API)
bot = Bot(token=config.TOKEN_API, proxy='http://10.0.48.52:3128')
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


# Комната 1 Дверь 1
@dp.callback_query_handler(lambda x: x.data == "door1")
async def wizard_room1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, config.___, reply_markup=kb.battle)










# РЫЦАРЬ
@dp.callback_query_handler(lambda x: x.data == "knight")
async def knight_delete_button(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(callback_query.from_user.id, config.KNIGHT_HISTORY)
    time.sleep(5)  # написать время ожидания после вывода текста
    await bot.send_message(callback_query.from_user.id, config.KNIGHT_START_TEXT)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
