from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton("Тренировки"),
           KeyboardButton("Рецепты"),
           KeyboardButton("Справочник")).add(KeyboardButton("Подписка"),
                                             KeyboardButton("Профиль"),
                                             KeyboardButton("Помощь"))
    return kb


# "Тренировки в зале", callback_data="тренировки_в_зале"
def main_train_ikb():
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton("Тренировки в зале", callback_data="тренировки_в_зале"),
        InlineKeyboardButton("Тренировки дома", callback_data="тренировки_дома")], [
        InlineKeyboardButton("Подписка на тренировки", callback_data="подписка_на_тренировки")],
        [InlineKeyboardButton("Главное меню", callback_data="главное_меню")]
    ])
    return kb