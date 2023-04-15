from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



"""***********************************  MAIN KEYBOARDS  **************************************"""


# region register Ketboards
def start_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton("/create"))
    return kb


def register_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton("выйти"))
    return kb


def register_sex_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton("Мужской"), KeyboardButton("Женский"))
    return kb


# endregion


"""***********************************  БЛОК КЛАВИАТУР ДОМАШНИХ ТРЕНИРОВОК  **************************************"""


# region БЛОК КЛАВИАТУР ДОМАШНИХ ТРЕНИРОВОК
def home_train_menu_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Верх тела", callback_data="верх_тела_дома")],
        [InlineKeyboardButton("Спина", callback_data="спина_дома")],
        [InlineKeyboardButton("Пресс", callback_data="пресс_дома")],
        [InlineKeyboardButton("Ноги", callback_data="ноги_дома")],
        [InlineKeyboardButton("Фулбади", callback_data="фулбади_дома")],
        [InlineKeyboardButton("Кардио", callback_data="кардио_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# endregion
"""***********************************  РАБОТА С КАТЕГОРИЯМИ  **************************************"""


# region MUSKLE GROUP HOME
def home_train_upperbody_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Трицепс", callback_data="трицепс_дома")],
        [InlineKeyboardButton("Бицепс", callback_data="бицепс_дома")],
        [InlineKeyboardButton("Грудные мышцы", callback_data="грудные_дома")],
        [InlineKeyboardButton("назад", callback_data="тренировки_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# "Верх спины", callback_data="верх_спины_дома"
def home_train_back_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Верх спины", callback_data="верх_спины_дома")],
        [InlineKeyboardButton("Нижняя часть спины", callback_data="низ_спины_дома")],
        [InlineKeyboardButton("назад", callback_data="тренировки_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# "Прямые скручивания", callback_data="прямые_скручивания_дома"
def home_train_press_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Прямые скручивания", callback_data="прямые_скручивания_дома")],
        [InlineKeyboardButton("Боковые скручивания", callback_data="боковые_скручивания_дома")],
        [InlineKeyboardButton("Подъем ног лежа на боку", callback_data="подъем_ног_на_боку_дома")],
        [InlineKeyboardButton("Скручивания с качанием носков", callback_data="скручивания_до_носков_дома")],
        [InlineKeyboardButton("назад", callback_data="тренировки_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


#  "Приседания с весом", callback_data="приседания_с_весом_дома"
def home_train_legs_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Приседания с весом", callback_data="приседания_с_весом_дома")],
        [InlineKeyboardButton("Мини - становая (узко)", callback_data="мини_становая_узко_дома")],
        [InlineKeyboardButton("Хип траст(прогибы с весом)", callback_data="хип_траст_дома")],
        [InlineKeyboardButton("назад", callback_data="тренировки_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# "Взрыв с низов", callback_data="поднятие_веса_на_подобии_гири_дома"
def home_train_fulbody_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Взрыв с низов", callback_data="поднятие_веса_на_подобии_гири_дома")],
        [InlineKeyboardButton("Берпи", callback_data="берпи_дома")],
        [InlineKeyboardButton("назад", callback_data="тренировки_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# "Взрыв с низов", callback_data="поднятие_веса_на_подобии_гири_дома"
def home_train_kardio_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Гусеница", callback_data="гусеница_дома")],
        [InlineKeyboardButton("Прыжки", callback_data="прыжки_дома")],
        [InlineKeyboardButton("Лестница", callback_data="лестница_дома")],
        [InlineKeyboardButton("Берпи", callback_data="берпи_дома")],
        [InlineKeyboardButton("назад", callback_data="тренировки_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# endregion
"""***********************************  РАБОТА С УПРАЖНЕНИЯМИ HOME **************************************"""


# region РАБОТА С УПРАЖНЕНИЯМИ ДОМА
####### HOME TRAIN UPPERBODY   # "Отжимания", callback_data="отжимания_дома"
def home_train_triceps_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Отжимания", callback_data="отжимания_дома")],
        [InlineKeyboardButton("Отжимание с опорой сзади", callback_data="отжимания_сзади_дома")],
        [InlineKeyboardButton("Алмазные отжимания", callback_data="алмазные_отжимания_дома")],
        [InlineKeyboardButton("назад", callback_data="верх_тела_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# "Изоляция на бицепс", callback_data="изоляция_бицепс_дома"
def home_train_biceps_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Изоляция на бицепс", callback_data="изоляция_бицепс_дома")],
        [InlineKeyboardButton("Упражнение 'Молоты'", callback_data="упражнение_молоты_дома")],
        [InlineKeyboardButton("назад", callback_data="верх_тела_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# "Отжимания c хлопком", callback_data="отжимания_с_хлопком_дома"
def home_train_chest_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Отжимания c хлопком", callback_data="отжимания_с_хлопком_дома")],
        [InlineKeyboardButton("Пуловер", callback_data="пуловер_дома")],
        [InlineKeyboardButton("Базовые отжимания", callback_data="базовые_отжимания_дома")],
        [InlineKeyboardButton("назад", callback_data="верх_тела_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


##### HOME TRAIN BACK           # "Тяга с опорой", callback_data="тяга_с_опорой_дома"
def home_train_upperBACK_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Тяга с опорой", callback_data="тяга_с_опорой_дома")],
        [InlineKeyboardButton("Пуловер", callback_data="пуловер_спины_дома")],
        [InlineKeyboardButton("назад", callback_data="спина_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# "Гиперэкстензия", callback_data="гиперэкстензия_дома"
def home_train_downBACK_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Гиперэкстензия", callback_data="гиперэкстензия_дома")],
        [InlineKeyboardButton("Мини - становая", callback_data="мини_становая_дома")],
        [InlineKeyboardButton("назад", callback_data="спина_дома")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# endregion


"""************БЛОК С КЛАВИАТУРАМИ ДЛЯ ТРЕНИРОВОК В ЗАЛЕ ***************"""


# region БЛОК С КЛАВИАТУРАМИ ДЛЯ ТРЕНИРОВОК В ЗАЛЕ
def gym_train_menu_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Верх тела", callback_data="верх_тела_зал")],
        [InlineKeyboardButton("Спина", callback_data="спина_зал")],
        [InlineKeyboardButton("Пресс", callback_data="пресс_зал")],
        [InlineKeyboardButton("Ноги", callback_data="ноги_зал")],
        [InlineKeyboardButton("Фулбади", callback_data="всё_тело_зал")],
        [InlineKeyboardButton("Кардио", callback_data="кардио_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# endregion
"""***********************************  РАБОТА С КАТЕГОРИЯМИ  **************************************"""


# region РАБОТА С КАТЕГОРИЯМИ
def gym_train_upperbody_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Трицепс", callback_data="трицепс_зал")],
        [InlineKeyboardButton("Бицепс", callback_data="бицепс_зал")],
        [InlineKeyboardButton("Грудные мышцы", callback_data="грудные_зал")],
        [InlineKeyboardButton("Плечи", callback_data="плечи_зал")],
        [InlineKeyboardButton("назад", callback_data="тренировки_в_зале")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


# "Верх спины", callback_data="верх_спины_дома"
def gym_train_back_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Верх спины", callback_data="верх_спины_зал")],
        [InlineKeyboardButton("Нижняя часть спины", callback_data="низ_спины_зал")],
        [InlineKeyboardButton("назад", callback_data="тренировки_в_зале")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb





def gym_train_legs_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Квадрицепс", callback_data="квадрицепс_зал")],
        [InlineKeyboardButton("Задняя часть бедра", callback_data="задняя_часть_бедра_зал")],
        [InlineKeyboardButton("Икроножные мышцы", callback_data="икроножные_мышцы_зал")],
        [InlineKeyboardButton("Бедра", callback_data="бедра_зал")],
        [InlineKeyboardButton("назад", callback_data="тренировки_в_зале")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb





# endregion
"""***********************************  РАБОТА С УПРАЖНЕНИЯМИ  **************************************"""

#region УПРАЖНЕНИЯ ЗАЛ
def gym_train_triceps_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Французкий жим изогнутого грифа", callback_data="франнузский_жим_зал")],
        [InlineKeyboardButton("Жим лежа узким хватом", callback_data="жим_лежа_узким_хватом_зал")],
        [InlineKeyboardButton("Жим лежа классика", callback_data="жим_лежа_классика_зал")],
        [InlineKeyboardButton("Брусья", callback_data="брусья_зал")],
        [InlineKeyboardButton("Кроссовер", callback_data="кроссовер_зал")],
        [InlineKeyboardButton("назад", callback_data="верх_тела_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


def gym_train_biceps_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Подъем изогнутого грифа", callback_data="подъем_изогнутого_грифа_зал")],
        [InlineKeyboardButton("Подъем штанги на бицепс", callback_data="подъем_штанги_на_бицепс_зал")],
        [InlineKeyboardButton("Гантели развернутым хватом'", callback_data="гантели_развернутым_хватом_зал")],
        [InlineKeyboardButton("Гантели 'МОЛОТЫ'", callback_data="упражнение_молоты_зал")],
        [InlineKeyboardButton("назад", callback_data="верх_тела_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


def gym_train_chest_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Жим штанги лежа", callback_data="жим_лежа_классика_зал")],
        [InlineKeyboardButton("Жим гантелей лежа", callback_data="жим_гантелей_лежа_зал")],
        [InlineKeyboardButton("Жим гантелей на наклонной скамье", callback_data="гантели_наклонная_скамья_зал")],
        [InlineKeyboardButton("Жим штанги на наклонной скамье", callback_data="штанга_наклонная_скамья_зал")],
        [InlineKeyboardButton("Брусья", callback_data="брусья_зал")],
        [InlineKeyboardButton("назад", callback_data="верх_тела_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


def gym_train_upperBACK_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Подтягивания", callback_data="подтягивания_зал")],
        [InlineKeyboardButton("Тяга гантелей на наклонной скамье", callback_data="тяга_на_наклонной_скамье_зал")],
        [InlineKeyboardButton("Тяга штанги в наклоне", callback_data="тяга_штанги_в_наклоне_зал")],
        [InlineKeyboardButton("Тяга одной рукой с упором", callback_data="тяга_одной_с_упором_зал")],
        [InlineKeyboardButton("назад", callback_data="спина_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


def gym_train_downBACK_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Становая тяга", callback_data="становая_тяга_зал")],
        [InlineKeyboardButton("Гиперэкстензия", callback_data="гиперэкстензия_зал")],
        [InlineKeyboardButton("Тяга штанги в наклоне", callback_data="тяга_штанги_в_наклоне_зал")],
        [InlineKeyboardButton("назад", callback_data="спина_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


def gym_train_quadLEGS_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Присед со штангой", callback_data="присед_со_штангой_зал")],
        [InlineKeyboardButton("Присед с гантелями", callback_data="присед_с_гантелями_зал")],
        [InlineKeyboardButton("назад", callback_data="ноги_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
        ])
    return kb

def gym_train_bicepsLEGS_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Становая тяга", callback_data="становая_тяга_зал")],
        [InlineKeyboardButton("Присед на одной ноге", callback_data="присед_на_одной_ноге_зал")],
        [InlineKeyboardButton("назад", callback_data="ноги_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
        ])
    return kb

def gym_train_icriLEGS_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Подъем на носки со штангой", callback_data="на_носки_штанга_зал")],
        [InlineKeyboardButton("Подъем на носки с гантелями", callback_data="на_носки_гантели_зал")],
        [InlineKeyboardButton("назад", callback_data="ноги_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
        ])
    return kb

def gym_train_assLEGS_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Мостик со штангой", callback_data="мостик_со_штангой_зал")],
        [InlineKeyboardButton("Мостик", callback_data="мостик_зал")],
        [InlineKeyboardButton("назад", callback_data="ноги_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
        ])
    return kb

def gym_train_press_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Прямые скручивания", callback_data="прямые_скручивания_зал")],
        [InlineKeyboardButton("Боковые скручивания", callback_data="боковые_скручивания_зал")],
        [InlineKeyboardButton("Боковые скручивания с доп весом", callback_data="боковые_с_доп_весом_зал")],
        [InlineKeyboardButton("Подъем ног на брусьх", callback_data="подъем_ног_на_брусьях_зал")],
        [InlineKeyboardButton("назад", callback_data="тренировки_в_зале")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


def gym_train_shoulders_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Жим Арнольда", callback_data="жим_арнольда_зал")],
        [InlineKeyboardButton("Жим гантелей вверх", callback_data="жим_гантелей_вверх_зал")],
        [InlineKeyboardButton("Протяжка гантелей", callback_data="протяжка_гантелей_зал")],
        [InlineKeyboardButton("Махи гантелями", callback_data="махи_гантелями_зал")],
        [InlineKeyboardButton("Подъем штанги над головой", callback_data="подъем_штанги_над_головой_зал")],
        [InlineKeyboardButton("Тяга лежа на скамье", callback_data="тяга_лежа_на_скамье_зал")],
        [InlineKeyboardButton("назад", callback_data="верх_тела_зал")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb

def gym_train_fulbody_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Взрыв с низов со штангой", callback_data="взрыв_со_штангой_зал")],
        [InlineKeyboardButton("Толкание гири с низкого положения", callback_data="толкание_гири_зал")],
        [InlineKeyboardButton("назад", callback_data="тренировки_в_зале")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb


def gym_train_kardio_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Бокс", callback_data="бокс_зал")],
        [InlineKeyboardButton("Скакалка", callback_data="скакалка_зал")],
        [InlineKeyboardButton("Ходьба", callback_data="Ходьба_зал")],
        [InlineKeyboardButton("Берпи", callback_data="берпи_зал")],
        [InlineKeyboardButton("Бег", callback_data="бег_зал")],
        [InlineKeyboardButton("Прыжки", callback_data="прыжки_зал")],
        [InlineKeyboardButton("назад", callback_data="тренировки_в_зале")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb
#endregion