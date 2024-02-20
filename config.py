TOKEN_API = "6598630985:AAH6hm8idDR8J4SxkhljfEzBoYnKE4Q4X4s"

# Характеристика персонажей
wizard = dict(name='Волшебник', pw=60, hp=55)
knight = dict(name='Рыцарь', pw=40, hp=70)

# Характеристики монстров(pw - сила, hp - здоровье)
slime = dict(name='Слайм', pw=20, hp=40)
spider = dict(name='Паук', pw=30, hp=40)
skeleton = dict(name='Скелет', pw=45, hp=60)
golem = dict(name='Голем', pw=55, hp=65)
demon = dict(name='Демон', pw=75, hp=85)  # Босс для Волшебника
dragon = dict(name='Дракон', pw=55, hp=90)  # Босс для Рыцаря

# Здоровье
HP_KNIGHT = 70
HP_WIZARD = 55

HP_SLIME = 30
HP_SPIDER = 40
HP_SKELETON = 60
HP_GOLEM = 65

HP_DEMON = 85
HP_DRAGON = 90

# Текст при запуске бота
START_TEXT = ''' 
Здравствуй, друг! Приветствую тебя в моей игре. 
Желаю тебе удачи пройти её!
'''

# Текст кнопки информация (написать)
INFORMATION_TEXT = ''' 
ТУТ БУДЕТ ТЕКСТ ПРО БОТА И ОПИСАНИЕ ИГРЫ
'''

START_GAME_TEXT = f'''
Перед началом ознакомьтесь с характеристиками персонажей, которых вам надо будет выбрать для прохождения игры:

ХАРАКТЕРИСТИКА ВОЛШЕБНИКА:\n
Здоровье: {wizard["hp"]}
Сила: {wizard["pw"]}

ХАРАКТЕРИСТИКА РЫЦАРЯ:\n
Здоровье: {knight["hp"]}
Сила: {knight["pw"]}
'''

WIZARD_OPS = f'''
Характеристики волшебника:\n
Здоровье: {wizard["hp"]}
Сила: {wizard["pw"]}
'''

KNIGHT_OPS = f'''
Характеристики рыцаря:\n
Здоровье: {knight["hp"]}
Сила: {knight["pw"]}
'''

WIZARD_HISTORY = '''
Волшебник, хороший выбор!
'''

KNIGHT_HISTORY = '''
Рыцарь, хороший выбор!
'''

WIZARD_START_TEXT = '''
Вы появляйтесь в подземелье и видите перед собой две двери, в какую войдете?
'''

KNIGHT_START_TEXT = '''
Вы появляйтесь в подземелье и видите перед собой две двери, в какую войдете?
'''

# Текста при встречах с монстрами
SLIME_MEETING = f'''
Вы встречайте перед собой слайма. Перед тем как выбрать действие посмотрите характеристики монстра:\n
Характеристики слайма:
Здоровье: {slime["hp"]}
Сила: {slime["pw"]}
'''

SPIDER_MEETING = f'''
Вы встречайте перед собой паука. Перед тем как выбрать действие посмотрите характеристики монстра:\n
Характеристики паука:
Здоровье: {spider["hp"]}
Сила: {spider["pw"]}
'''

SKELETON_MEETING = f'''
Вы встречайте перед собой скелета. Перед тем как выбрать действие посмотрите характеристики монстра:\n
Характеристики скелета:
Здоровье: {skeleton["hp"]}
Сила: {skeleton["pw"]}
'''

GOLEM_MEETING = f'''
Вы встречайте перед собой голем. Перед тем как выбрать действие посмотрите характеристики монстра:\n
Характеристики голема:
Здоровье: {golem["hp"]}
Сила: {golem["pw"]}
'''

DEMON_MEETING = f'''
Входя в огромную комнату, вы встречайте перед собой демона, вот его характеристики:\n
Характеристики голема:
Здоровье: {demon["hp"]}
Сила: {demon["pw"]}
'''

YOU_DEAD_DEMON_WIZARD = '''
Вас убил демон!
Игра окончена!
'''

YOU_DEAD_SPIDER_WIZARD = '''
Вы умерли от лап паука!
Игра окончена!
'''

YOU_DEAD_SLIME_WIZARD = '''
Вы умерли от слайма!
Игра окончена!
'''

YOU_DEAD_SKELETON_WIZARD = '''
Вы умерли от скелета!
Игра окончена!
'''

YOU_WIN_SPIDER_WIZARD = '''
Вы победили паука!
'''

AFTER_FIGHT_WIZARD_HP = '''
После боя у вас осталось здоровья: 
'''

# побег 1_1
AWAY_TEXT_WIZARD_SPIDER = '''
Вы решайте сбежать от паука.\n 
При попытке побега паук вас задевает
и вы теряйте 5 здоровья.
'''

AWAY_TEXT_WIZARD_SLIME = '''
Вы решайте сбежать от слайма.\n 
При попытке побега слайм вас задевает
и вы теряйте 3 здоровья.
'''

ROOM_WIZARD_SPIDER = '''
После победы над пауком вы проходите в следующую комнату и видите две двери, в какую войдете?
'''

ROOM_WIZARD_SKELETON = '''
После победы над скелетом вы проходите в следующую комнату и видите две двери, в какую войдете?
'''

ROOM_WIZARD_SLIME = '''
После победы над слаймом вы проходите в следующую комнату и видите две двери, в какую войдете?
'''

ROOM_WIZARD_GOLEM = '''
После победы над големом вы проходите в следующую комнату и видите две двери, в какую войдете?
'''

AWAY_TEXT_WIZARD_SKELETON = '''
Вы решайте сбежать от скелета.\n 
При попытке побега он вас задевает
и вы теряйте 7 здоровья.
'''

NO_HP_DEAD_WIZARD = '''
Вы погибли от нехватки здоровья!
Игра окончена!
'''

AFTER_AWAY = '''
После побега у вас осталось здоровья: 
'''

YOU_WIN_SLIME_WIZARD = '''
Вы победили слайма!
'''

YOU_DEAD_GOLEM_WIZARD = '''
Вы умерли от голема!
Игра окончена!
'''

YOU_WIN_GOLEM_WIZARD = '''
Вы победили голема!
'''

YOU_WIN_SKELETON_WIZARD = '''
Вы победили скелета!
'''

TRANSITION_SPIDER_WIZARD = f'''
Войдя в другую дверь, вы видите перед собой паука с характеристиками:\n
Характеристики паука:
Здоровье: {spider["hp"]}
Сила: {spider["pw"]}\n
Вариантов у вас не будет, вы точно будете сражаться с пауком, т.к сбежали из другой комнаты.
'''

TRANSITION_SLIME_WIZARD = f'''
Войдя в другую дверь, вы видите перед собой слайма с характеристиками:\n
Характеристики слайма:
Здоровье: {slime["hp"]}
Сила: {slime["pw"]}\n
Вариантов у вас не будет, вы точно будете сражаться со слаймом, т.к сбежали из другой комнаты.
'''

TRANSITION_SKELETON_WIZARD = f'''
Войдя в другую дверь, вы видите перед собой скелета с характеристиками:\n
Характеристики скелета:
Здоровье: {skeleton["hp"]}
Сила: {skeleton["pw"]}\n
Вариантов у вас не будет, вы точно будете сражаться с скелетом, т.к сбежали из другой комнаты.
'''

TRANSITION_GOLEM_WIZARD = f'''
Войдя в другую дверь, вы видите перед собой голема с характеристиками:\n
Характеристики голема:
Здоровье: {golem["hp"]}
Сила: {golem["pw"]}\n
Вариантов у вас не будет, вы точно будете сражаться с големом, т.к сбежали из другой комнаты.
'''

AWAY_TEXT_WIZARD_GOLEM = '''
Вы решайте сбежать от голема.\n 
При попытке побега он вас задевает
и вы теряйте 9 здоровья.
'''

END_GAME_WIZARD = '''
Поздравляю, вы победили демона!
Игра пройдена!
'''

END_GAME_KNIGHT = '''
Поздравляю, вы победили дракона!
Игра пройдена!
'''

BONUS_HP = '''
Перед тем, как сразиться с боссом, вы находите бонус +15 здоровья.
Теперь у вас здоровья: 
'''