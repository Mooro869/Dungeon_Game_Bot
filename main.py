import time
import random
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
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.WIZARD_HISTORY)
    # Вывод дверных кнопок 1 комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.WIZARD_START_TEXT, reply_markup=kb.doors1)

'''
От этого текста
будут начитаться доп фукнции для упрощения чтения и редактирования кода
'''

# 1_1 Паук
@dp.callback_query_handler(lambda x: x.data == "door1_1_1")
async def wizard_room1_buttons(callback_query: types.CallbackQuery):  # Функция с основным выводом текста
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING, reply_markup=kb.battle1_1)


# Действия при атаке 1_1
@dp.callback_query_handler(lambda x: x.data == "attack1_1")
async def wizard_room1_delete_buttons(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        s_push = random.randint(1, config.spider['pw'])
        config.spider['hp'] -= w_push
        config.wizard['hp'] -= s_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.spider['hp'] = config.HP_SPIDER  # Возвращаем здоровье пауку после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER_WIZARD)
            break
        elif config.wizard['hp'] >= 1:  # Действия при победе над пауком
            config.spider['hp'] = config.HP_SPIDER
            break
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER_WIZARD)
    # Вывод здоровья
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
    # Создание кнопок второй комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.TWO_ROOM_WIZARD, reply_markup=kb.doors2)
    # закончен


# 2_1 Слайм
@dp.callback_query_handler(lambda x: x.data == "door1_2_1")
async def wizard_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING, reply_markup=kb.battle2_1)


# Действия при атаке 2_1
@dp.callback_query_handler(lambda x: x.data == "attack2_1")
async def wizard_room2_delete_buttons(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.slime['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sl_push = random.randint(1, config.slime['pw'])
        config.slime['hp'] -= w_push
        config.wizard['hp'] -= sl_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.slime['hp'] = config.HP_SLIME  # Возвращаем здоровье пауку после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME_WIZARD)
            break
        elif config.wizard['hp'] >= 1:  # Действия при победе над пауком
            config.slime['hp'] = config.HP_SLIME
            break
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME_WIZARD)
        # Вывод здоровья
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
        # Создание кнопок второй комнаты
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.THREE_ROOM_WIZARD,
                               reply_markup=kb.doors3)
        # закончен


# Действия при побеге 1_1(переход в 1_2(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "away1_1")
async def wizard_room1_away_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_WIZARD_SPIDER_1_1)
    # Проверка колличества здоровья после побега
    config.wizard['hp'] -= 5
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD_WIZARD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY_WIZARD_1_1 + str(config.wizard['hp']))
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_TO_1_2_WIZARD)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            s_push = random.randint(1, config.spider['pw'])
            config.spider['hp'] -= w_push
            config.wizard['hp'] -= s_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.spider['hp'] = config.HP_SPIDER  # Возвращаем здоровье пауку после драки
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER_WIZARD)
                break
            elif config.wizard['hp'] >= 1:  # Действия при победе над пауком
                config.spider['hp'] = config.HP_SPIDER
                break
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER_WIZARD)
        # Вывод здоровья
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TWO_ROOM_WIZARD, reply_markup=kb.doors2)
        # закончен


# 1_2 Слайм
@dp.callback_query_handler(lambda x: x.data == "door1_2_1")
async def wizard_room1_buttons(callback_query: types.CallbackQuery):  # Функция с основным выводом текста
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING, reply_markup=kb.battle1_2)


# РЫЦАРЬ
@dp.callback_query_handler(lambda x: x.data == "knight")
async def knight_delete_button(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.KNIGHT_HISTORY)
    time.sleep(3)  # написать время ожидания после вывода текста
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.KNIGHT_START_TEXT)
    await bot.send_message(chat_id=callback_query.from_user.id, text='РЫЦАРЬ НЕ РАБОТАЕТ!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
