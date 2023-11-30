from random import randint
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import config
import keyboard as kb

bot = Bot(token=config.TOKEN_API)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=config.START_TEXT, reply_markup=kb.keyb)


@dp.message_handler(text=['Информация'])
async def information_command(message: types.Message):
    await message.answer(text=config.INFORMATION_TEXT)


@dp.message_handler(text=['Начать игру'])
async def information_command(message: types.Message):
    await message.answer(text=config.START_GAME_TEXT, reply_markup=kb.persons_button)


@dp.callback_query_handler()  # Кнопка при выборе персонажей
async def wizard_change(callback: types.CallbackQuery):
    if callback.data == 'wizard':
        await bot.send_message(chat_id=callback.from_user.id, text=config.WIZARD_HISTORY)
    elif callback.data == 'knight':
        await bot.send_message(chat_id=callback.from_user.id, text=config.KNIGHT_HISTORY)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
