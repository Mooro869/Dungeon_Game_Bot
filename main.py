import logging
from random import randint
from time import sleep

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import config
import keyboard

bot = Bot(token=config.TOKEN_API)
dp = Dispatcher(bot=bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
