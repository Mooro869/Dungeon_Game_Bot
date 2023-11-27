import aiogram
import logging
from random import randint
from time import sleep

import executor
from aiogram import Bot, Dispatcher, types

import config
import keyboard

bot = Bot(token=config.TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
