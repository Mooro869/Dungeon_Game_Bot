import logging
import time
from random import randint
from time import sleep

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import config
import keyboard

bot = Bot(token=config.TOKEN_API)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=config.START_TEXT)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=config.HELP_COMMANDS)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
