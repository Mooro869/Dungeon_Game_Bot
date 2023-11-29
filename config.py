import config

TOKEN_API = "6598630985:AAH6hm8idDR8J4SxkhljfEzBoYnKE4Q4X4s"

# Характеристика персонажей
wizard = dict(name='Волшебник', pw=60, hp=40)
knight = dict(name='Рыцарь', pw=40, hp=70)

# Характеристики монстров
spider = dict()
golem = dict()
slime = dict()
skeleton = dict()
demon = dict()
dragon = dict()

# Текст при запуске бота
START_TEXT = ''' 
Здравствуй, друг! Приветствую тебя в моём боте. Это приключение затянет тебя надолго.
'''

# Текст кнопки информация !!!!!!!!!!!!!!
INFORMATION_TEXT = ''' 
ТУТ БУДЕТ ТЕКСТ ПРО БОТА И ОПИСАНИЕ ИГРЫ
'''

START_GAME_TEXT = f'''
Перед начало ознакомтесь с характеристиками персонажей, которых вам надо будет выбрать для прохождения игры:

ХАРАКТЕРИСТИКА ВОЛШЕБНИКА:\n
Здоровье: {wizard["hp"]}\n
Сила: {wizard["pw"]}\n

ХАРАКТЕРИСТИКА РЫЦАРЯ:\n
Здоровье: {knight["hp"]}\n
Сила: {knight["pw"]}
'''

WIZARD_OPS = f'''
Характеристики волшебника:\n
Здоровье: {config.wizard["hp"]}\n
Сила: {config.wizard["pw"]}
'''

KNIGHT_OPS = f'''
Характеристики рыцаря:\n
Здоровье: {config.knight["hp"]}\n
Сила: {config.knight["pw"]}
'''
