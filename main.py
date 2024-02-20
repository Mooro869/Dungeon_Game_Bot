import time
import random
from aiogram import Bot, Dispatcher, types
from aiogram import executor

import config
import keyboard as kb

bot = Bot(token=config.TOKEN_API)
# bot = Bot(token=config.TOKEN_API, proxy='http://10.0.48.52:3128')
dp = Dispatcher(bot=bot)


def recovery_all_hp():  # Востановление всем здоровья
    config.knight = config.HP_KNIGHT
    config.wizard = config.HP_WIZARD

    config.slime = config.HP_SLIME
    config.spider = config.HP_SPIDER
    config.skeleton = config.HP_SKELETON
    config.golem = config.HP_GOLEM

    config.demon = config.HP_DEMON
    config.dragon = config.HP_DRAGON


# НАЧАЛО
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=config.START_TEXT, reply_markup=kb.keyb)


@dp.message_handler(text=['Информацияℹ️'])
async def information_command(message: types.Message):
    await message.answer(text=config.INFORMATION_TEXT)


@dp.message_handler(text=['Начать игру🎮'])
async def start_command(message: types.Message):
    await message.answer(text=config.START_GAME_TEXT, reply_markup=kb.persons_button)


# ВОЛШЕБНИК
@dp.callback_query_handler(lambda x: x.data == "wizard")
async def wizard_delete_button(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.WIZARD_HISTORY)
    # Вывод дверных кнопок 1 комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.WIZARD_START_TEXT, reply_markup=kb.doors1)


'''
Функции вывода кнопок
'''


# 1_1 Паук
@dp.callback_query_handler(lambda x: x.data == "door1_1")
async def wizard_room1_buttons(callback_query: types.CallbackQuery):  # Функция с основным выводом текста
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING, reply_markup=kb.battle1_1)


# 1_2 Слайм

@dp.callback_query_handler(lambda x: x.data == "door1_2")
async def wizard_room1_buttons(callback_query: types.CallbackQuery):  # Функция с основным выводом текста
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING, reply_markup=kb.battle1_2)


# 2_1 Слайм
@dp.callback_query_handler(lambda x: x.data == "door2_1")
async def wizard_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING, reply_markup=kb.battle2_1)


# 2_2 Скелет
@dp.callback_query_handler(lambda x: x.data == "door2_2")
async def wizard_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SKELETON_MEETING, reply_markup=kb.battle2_2)


# 3_1 Голем
@dp.callback_query_handler(lambda x: x.data == "door3_1")
async def wizard_room3_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.GOLEM_MEETING, reply_markup=kb.battle3_1)


# 3_2 Паук
@dp.callback_query_handler(lambda x: x.data == "door3_2")
async def wizard_room3_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING, reply_markup=kb.battle3_2)


# 4_1 Паук
@dp.callback_query_handler(lambda x: x.data == "door4_1")
async def wizard_room4_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING, reply_markup=kb.battle4_1)


# 4_2 Скелет
@dp.callback_query_handler(lambda x: x.data == "door4_2")
async def wizard_room4_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SKELETON_MEETING, reply_markup=kb.battle4_2)


# 5 Демон
@dp.callback_query_handler(lambda x: x.data == "door5")
async def wizard_room5_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    config.wizard += 15
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.BONUS_HP + str(config.wizard['hp']))
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.DEMON_MEETING, reply_markup=kb.battle5)


'''
Функции атаки
'''


# Действия при атаке 1_1
@dp.callback_query_handler(lambda x: x.data == "attack1_1")
async def wizard1_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sp_push = random.randint(1, config.spider['pw'])
        config.spider['hp'] -= w_push
        config.wizard['hp'] -= sp_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.spider['hp'] = config.HP_SPIDER  # Возвращаем здоровье пауку после драки
            recovery_all_hp()
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER_WIZARD)
            break
        elif config.wizard['hp'] >= 1:
            config.spider['hp'] = config.HP_SPIDER
            break
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER_WIZARD)
    # Вывод здоровья
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
    # Создание кнопок второй комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SPIDER,
                           reply_markup=kb.doors2)
    # закончен


# Действия при атаке 1_2
@dp.callback_query_handler(lambda x: x.data == "attack1_2")
async def wizard1_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.slime['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sl_push = random.randint(1, config.slime['pw'])
        config.slime['hp'] -= w_push
        config.wizard['hp'] -= sl_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.slime['hp'] = config.HP_SLIME  # Возвращаем здоровье слайму после драки
            recovery_all_hp()
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME_WIZARD)
            break
        elif config.wizard['hp'] >= 1:
            config.slime['hp'] = config.HP_SLIME
            break
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME_WIZARD)
    # Вывод здоровья
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
    # Создание кнопок второй комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SLIME,
                           reply_markup=kb.doors2)
    # закончен


# Действия при атаке 2_1
@dp.callback_query_handler(lambda x: x.data == "attack2_1")
async def wizard2_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.slime['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sl_push = random.randint(1, config.slime['pw'])
        config.slime['hp'] -= w_push
        config.wizard['hp'] -= sl_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.slime['hp'] = config.HP_SLIME  # Возвращаем здоровье слайму после драки
            recovery_all_hp()
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME_WIZARD)
            break
        elif config.wizard['hp'] >= 1:
            config.slime['hp'] = config.HP_SLIME
            break
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME_WIZARD)
        # Вывод здоровья
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
    # Создание кнопок второй комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SLIME,
                           reply_markup=kb.doors3)
    # закончен


# Действия при атаке 2_2
@dp.callback_query_handler(lambda x: x.data == "attack2_2")
async def wizard2_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.skeleton['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sk_push = random.randint(1, config.skeleton['pw'])
        config.skeleton['hp'] -= w_push
        config.wizard['hp'] -= sk_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.skeleton['hp'] = config.HP_SKELETON  # Возвращаем здоровье скелету после драки
            recovery_all_hp()
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON_WIZARD)
            break
        elif config.wizard['hp'] >= 1:
            config.skeleton['hp'] = config.HP_SKELETON
            break
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON_WIZARD)
        # Вывод здоровья
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
    # Создание кнопок второй комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SKELETON,
                           reply_markup=kb.doors3)
    # закончен


# Действия при атаке 3_1
@dp.callback_query_handler(lambda x: x.data == "attack3_1")
async def wizard3_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.golem['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        g_push = random.randint(1, config.golem['pw'])
        config.golem['hp'] -= w_push
        config.wizard['hp'] -= g_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.golem['hp'] = config.HP_GOLEM  # Возвращаем здоровье скелету после драки
            recovery_all_hp()
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM_WIZARD)
            break
        elif config.wizard['hp'] >= 1:  # Действия при победе над големом
            config.golem['hp'] = config.HP_GOLEM
            break
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM_WIZARD)
        # Вывод здоровья
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
    # Создание кнопок второй комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_GOLEM,
                           reply_markup=kb.doors4)
    # закончен


# Действия при атаке 3_2
@dp.callback_query_handler(lambda x: x.data == "attack3_2")
async def wizard3_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sp_push = random.randint(1, config.spider['pw'])
        config.spider['hp'] -= w_push
        config.wizard['hp'] -= sp_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.spider['hp'] = config.HP_SPIDER  # Возвращаем здоровье пауку после драки
            recovery_all_hp()
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER_WIZARD)
            break
        elif config.wizard['hp'] >= 1:
            config.spider['hp'] = config.HP_SPIDER
            break
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER_WIZARD)
    # Вывод здоровья
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
    # Создание кнопок второй комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SPIDER,
                           reply_markup=kb.doors4)
    # закончен


# Действия при атаке 4_1
@dp.callback_query_handler(lambda x: x.data == "attack4_1")
async def wizard4_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sp_push = random.randint(1, config.spider['pw'])
        config.spider['hp'] -= w_push
        config.wizard['hp'] -= sp_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.spider['hp'] = config.HP_SPIDER  # Возвращаем здоровье пауку после драки
            recovery_all_hp()
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER_WIZARD)
            break
        elif config.wizard['hp'] >= 1:
            config.spider['hp'] = config.HP_SPIDER
            break
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER_WIZARD)
    # Вывод здоровья
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
    # Создание кнопок второй комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SPIDER,
                           reply_markup=kb.doors5)
    # закончен


# Действия при атаке 4_2
@dp.callback_query_handler(lambda x: x.data == "attack4_2")
async def wizard4_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.skeleton['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sk_push = random.randint(1, config.skeleton['pw'])
        config.skeleton['hp'] -= w_push
        config.wizard['hp'] -= sk_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.skeleton['hp'] = config.HP_SKELETON  # Возвращаем здоровье скелету после драки
            recovery_all_hp()
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON_WIZARD)
            break
        elif config.wizard['hp'] >= 1:
            config.skeleton['hp'] = config.HP_SKELETON
            break
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON_WIZARD)
        # Вывод здоровья
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
    # Создание кнопок второй комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SKELETON,
                           reply_markup=kb.doors5)
    # закончен


# Действия при атаке 5
@dp.callback_query_handler(lambda x: x.data == "attack5")
async def wizard5_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)


    # Цикл атаки
    while config.wizard['hp'] > 0 and config.demon['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        de_push = random.randint(1, config.demon['pw'])
        config.demon['hp'] -= w_push
        config.wizard['hp'] -= de_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.demon['hp'] = config.HP_DEMON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_DEMON_WIZARD)
            recovery_all_hp()
            break
        elif config.wizard['hp'] >= 1:
            config.demon['hp'] = config.HP_DEMON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.END_GAME_WIZARD)
            recovery_all_hp()
            break

    # закончен


'''
Функции побега
'''


# Действия при побеге 1_1(переход в 1_2(битва со слаймом))
@dp.callback_query_handler(lambda x: x.data == "away1_1")
async def wizard1_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_WIZARD_SPIDER)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 3
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD_WIZARD)
        recovery_all_hp()
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SLIME_WIZARD)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.slime['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sl_push = random.randint(1, config.slime['pw'])
            config.slime['hp'] -= w_push
            config.wizard['hp'] -= sl_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.slime['hp'] = config.HP_SLIME  # Возвращаем здоровье пауку после драки
                recovery_all_hp()
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME_WIZARD)
                break
            elif config.wizard['hp'] >= 1:
                config.slime['hp'] = config.HP_SLIME
                break
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME_WIZARD)
        # Вывод здоровья
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SLIME,
                               reply_markup=kb.doors2)
        # закончен


# Действия при побеге 1_2(переход в 1_1(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "away1_2")
async def wizard1_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_WIZARD_SLIME)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 5
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD_WIZARD)
        recovery_all_hp()
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER_WIZARD)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sp_push = random.randint(1, config.spider['pw'])
            config.spider['hp'] -= w_push
            config.wizard['hp'] -= sp_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.spider['hp'] = config.HP_SPIDER  # Возвращаем здоровье пауку после драки
                recovery_all_hp()
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER_WIZARD)
                break
            elif config.wizard['hp'] >= 1:
                config.spider['hp'] = config.HP_SPIDER
                break
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER_WIZARD)
        # Вывод здоровья
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SPIDER,
                               reply_markup=kb.doors2)
        # закончен


# Действия при побеге 2_1(переход в 2_2(битва со скелетом))
@dp.callback_query_handler(lambda x: x.data == "away2_1")
async def wizard2_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_WIZARD_SLIME)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 7
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD_WIZARD)
        recovery_all_hp()
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SKELETON_WIZARD)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.skeleton['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sk_push = random.randint(1, config.skeleton['pw'])
            config.skeleton['hp'] -= w_push
            config.wizard['hp'] -= sk_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.skeleton['hp'] = config.HP_SKELETON  # Возвращаем здоровье пауку после драки
                recovery_all_hp()
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON_WIZARD)
                break
            elif config.wizard['hp'] >= 1:
                config.skeleton['hp'] = config.HP_SKELETON
                break
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON_WIZARD)
        # Вывод здоровья
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SKELETON,
                               reply_markup=kb.doors3)
        # закончен


# Действия при побеге 2_2(переход в 2_1(битва со слаймом))
@dp.callback_query_handler(lambda x: x.data == "away2_2")
async def wizard2_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_WIZARD_SKELETON)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 7
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD_WIZARD)
        recovery_all_hp()
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SLIME_WIZARD)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.slime['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sl_push = random.randint(1, config.slime['pw'])
            config.slime['hp'] -= w_push
            config.wizard['hp'] -= sl_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.slime['hp'] = config.HP_SLIME  # Возвращаем здоровье пауку после драки
                recovery_all_hp()
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME_WIZARD)
                break
            elif config.wizard['hp'] >= 1:
                config.slime['hp'] = config.HP_SLIME
                break
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME_WIZARD)
        # Вывод здоровья
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SLIME,
                               reply_markup=kb.doors3)
        # закончен


# Действия при побеге 3_1(переход в 3_2(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "away3_1")
async def wizard3_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_WIZARD_GOLEM)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 7
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD_WIZARD)
        recovery_all_hp()
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER_WIZARD)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sp_push = random.randint(1, config.spider['pw'])
            config.spider['hp'] -= w_push
            config.wizard['hp'] -= sp_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.spider['hp'] = config.HP_SPIDER  # Возвращаем здоровье пауку после драки
                recovery_all_hp()
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER_WIZARD)
                break
            elif config.wizard['hp'] >= 1:
                config.spider['hp'] = config.HP_SPIDER
                break
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER_WIZARD)
        # Вывод здоровья
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SPIDER,
                               reply_markup=kb.doors4)
        # закончен


# Действия при побеге 3_2(переход в 3_1(битва с големом))
@dp.callback_query_handler(lambda x: x.data == "away3_2")
async def wizard3_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_WIZARD_SPIDER)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 5
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD_WIZARD)
        recovery_all_hp()
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_GOLEM_WIZARD)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.golem['hp'] > 0:
            w_push = random.randint(1, config.golem['pw'])
            g_push = random.randint(1, config.golem['pw'])
            config.golem['hp'] -= w_push
            config.wizard['hp'] -= g_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.golem['hp'] = config.HP_SPIDER  # Возвращаем здоровье пауку после драки
                recovery_all_hp()
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM_WIZARD)
                break
            elif config.wizard['hp'] >= 1:  # Действия при победе над големом
                config.golem['hp'] = config.HP_GOLEM
                break
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM_WIZARD)
        # Вывод здоровья
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SPIDER,
                               reply_markup=kb.doors4)
        # закончен


# Действия при побеге 4_1(переход в 4_2(битва со скелетом))
@dp.callback_query_handler(lambda x: x.data == "away4_1")
async def wizard4_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_WIZARD_SPIDER)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 5
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD_WIZARD)
        recovery_all_hp()
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SKELETON_WIZARD)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.skeleton['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sk_push = random.randint(1, config.skeleton['pw'])
            config.skeleton['hp'] -= w_push
            config.wizard['hp'] -= sk_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.skeleton['hp'] = config.HP_SKELETON  # Возвращаем здоровье пауку после драки
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON_WIZARD)
                recovery_all_hp()
                break
            elif config.wizard['hp'] >= 1:
                config.skeleton['hp'] = config.HP_SKELETON
                break
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON_WIZARD)
        # Вывод здоровья
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SKELETON,
                               reply_markup=kb.doors5)
        # закончен


# Действия при побеге 4_2(переход в 4_1(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "away4_2")
async def wizard4_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_WIZARD_SKELETON)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 7
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD_WIZARD)
        recovery_all_hp()
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER_WIZARD)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sp_push = random.randint(1, config.spider['pw'])
            config.spider['hp'] -= w_push
            config.wizard['hp'] -= sp_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.spider['hp'] = config.HP_SPIDER  # Возвращаем здоровье пауку после драки
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER_WIZARD)
                recovery_all_hp()
                break
            elif config.wizard['hp'] >= 1:
                config.spider['hp'] = config.HP_SPIDER
                break
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER_WIZARD)
        # Вывод здоровья
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_FIGHT_WIZARD_HP + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_WIZARD_SPIDER,
                               reply_markup=kb.doors5)
        # закончен


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
