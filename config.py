TOKEN_API = "6598630985:AAH6hm8idDR8J4SxkhljfEzBoYnKE4Q4X4s"

# Характеристика персонажей
wizard = dict(name='Волшебник', pw=60, hp=40)
knight = dict(name='Рыцарь', pw=40, hp=70)

# Характеристики монстров
slime = dict(name='Слайм', pw=None, hp=None)
spider = dict(name='Паук', pw=None, hp=None)
skeleton = dict(name='Скелет', pw=None, hp=None)
golem = dict(name='Голем', pw=None, hp=None)
demon = dict(name='Демон', pw=None, hp=None)  # Босс для Волшебника
dragon = dict(name='Дракон', pw=None, hp=None)  # Босс для Рыцаря

# Текст при запуске бота
START_TEXT = ''' 
Здравствуй, друг! Приветствую тебя в моём боте. Это приключение затянет тебя надолго.
'''

# Текст кнопки информация (дописать)
INFORMATION_TEXT = ''' 
ТУТ БУДЕТ ТЕКСТ ПРО БОТА И ОПИСАНИЕ ИГРЫ
'''

START_GAME_TEXT = f'''
Перед начало ознакомьтесь с характеристиками персонажей, которых вам надо будет выбрать для прохождения игры:

ХАРАКТЕРИСТИКА ВОЛШЕБНИКА:\n
Здоровье: {wizard["hp"]}\n
Сила: {wizard["pw"]}\n

ХАРАКТЕРИСТИКА РЫЦАРЯ:\n
Здоровье: {knight["hp"]}\n
Сила: {knight["pw"]}
'''

WIZARD_OPS = f'''
Характеристики волшебника:\n
Здоровье: {wizard["hp"]}\n
Сила: {wizard["pw"]}
'''

KNIGHT_OPS = f'''
Характеристики рыцаря:\n
Здоровье: {knight["hp"]}\n
Сила: {knight["pw"]}
'''
# (дописать)
WIZARD_HISTORY = '''
Волшебник, хороший выбор!
и т.д
'''
# (дописать)
KNIGHT_HISTORY = '''
Рыцарь, хороший выбор!
и т.д
'''

# (дописать)
WIZARD_START_TEXT = '''
Вы появляйтесь в подземелье и видите перед собой две двери, в какую войдете?
'''

# (дописать)
KNIGHT_START_TEXT = '''
ТЕКСТ
'''

MEETING_SPIDER_WIZARD = '''

'''



# сделать текста при встече с каждым монстром с указанием его характеристик
