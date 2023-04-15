from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from config import *
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import ReplyKeyboardRemove
from sqlite import *
from func import *
from keybaord import *



async def on_startup(_):
    await db_start()


storage = MemoryStorage()
bot = Bot(Api_token_telegramm_bot)
dp = Dispatcher(bot, storage=storage)

ADMIN = 558110480

class CustomMiddleware(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict):

        if message.from_user.id != ADMIN:
            print("Другой аккаунт")
            raise CancelHandler()



"""************************************************** REGISTER PROFILE *******************************************************************"""


class ProfileStatesGroup(StatesGroup):
    user_id = State()
    name = State()
    surname = State()
    age = State()
    sex = State()
    height = State()
    weight = State()
    calory = State()


# region REGISTERS USER
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("""Добро пожаловать в бота для тренировок!
Чтобы создать профиль нажми - /create """, reply_markup=start_kb())
    print("world")
    await create_profile(user_id=message.from_user.id)


@dp.message_handler(commands="create")
async def cmd_create(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["user_id"] = message.from_user.id
        data["username"] = message.from_user.username

    await message.answer("Ваше имя: ", reply_markup=register_kb())
    await ProfileStatesGroup.name.set()


@dp.message_handler(lambda message: message.text == "выйти", state="*")
async def exist_register(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.answer("Вы прервали регистрацию\nЧтобы создать профиль нажми - /create ", reply_markup=start_kb())


@dp.message_handler(lambda message: message.text.isdigit(), state=ProfileStatesGroup.name)
async def check_name(message: types.Message):
    await message.answer("Это число число а не имя!")


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text

    await message.reply("Теперь отправь свою фамилию")
    await ProfileStatesGroup.next()


@dp.message_handler(lambda message: message.text.isdigit(), state=ProfileStatesGroup.surname)
async def check_surname(message: types.Message):
    await message.answer("Это число число а не имя!")


@dp.message_handler(state=ProfileStatesGroup.surname)
async def load_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["surname"] = message.text

    await message.reply("Теперь отправь свой возраст")
    await ProfileStatesGroup.next()


@dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) > 99 or float(message.text) < 5,
                    state=ProfileStatesGroup.age)
async def check_age(message: types.Message):
    await message.answer("Ввеидите реальный возраст")


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = int(message.text)

    await message.reply("Выберите ваш пол", reply_markup=register_sex_kb())
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.sex)
async def load_sex(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["sex"] = message.text

    await message.reply("Укажите ваш рост", reply_markup=register_kb())
    await ProfileStatesGroup.next()


@dp.message_handler(
    lambda message: not message.text.isdigit() or float(message.text) > 240 or float(message.text) < 100,
    state=ProfileStatesGroup.height)
async def check_age(message: types.Message):
    await message.answer("Введите реальный рост")


@dp.message_handler(state=ProfileStatesGroup.height)
async def load_height(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["height"] = int(message.text)

    await message.reply("Сообщите ваш вес, обещаю это будет секретом 🤫 ", reply_markup=register_kb())
    await ProfileStatesGroup.next()


@dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) > 240 or float(message.text) < 20,
                    state=ProfileStatesGroup.weight)
async def check_age(message: types.Message):
    await message.answer("Введите настоящий вес)")


@dp.message_handler(state=ProfileStatesGroup.weight)
async def load_weight(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["weight"] = int(message.text)

        data["calory"] = calculate_calory(data["age"], data['weight'], data['height'], data['sex'])
        await message.answer(f"""
Ваше имя: {data['name']}
Ваша фамилия: {data['surname']}
Ваш возраст: {data['age']}
Базовый обмен: {round(data["calory"])} калорий

Ваш id: {data['user_id']}
""")

    await edit_profile(state, user_id=message.from_user.id)
    await message.answer("Регистрация закончена", reply_markup=main_menu_kb())
    await state.finish()


# endregion
"""************************************************** MAIN MENU *******************************************************************"""


# region main menu

@dp.message_handler(lambda message: message.text == "Профиль")
async def cmd_profiles(message: types.Message):
    profile_text = await get_profile(message.from_user.id)
    await message.answer(profile_text, parse_mode="HTML", reply_markup=main_menu_kb())
    await message.delete()


@dp.message_handler(lambda message: message.text == "Помощь")
async def cmd_profiles(message: types.Message):
    await message.answer("<b>Техподдержка: @kurilove_CRT</b>\n<b>Перезаписать профиль:</b> /create", parse_mode="HTML",
                         reply_markup=main_menu_kb())
    await message.delete()


@dp.message_handler(lambda message: message.text == "Справочник")
async def cmd_profiles(message: types.Message):
    await message.answer("""
Привет! Я - твой персональный помощник в спорте и здоровом питании.

С моей помощью ты сможешь получать рекомендации по выбору правильных продуктов, а также варианты тренировок, подходящих для твоей физической формы и целей.

Я предлагаю список упражнений для разных групп мышц и уровней сложности, а также рецепты сбалансированных блюд и десертов.

Ты можешь выбрать интересующий тебя раздел и получить полезную информацию,<b> а также подписаться на конкретный план похудения или набора за копеечку автору</b> 😊.

Не забывай следить за своим здоровьем и при желании консультироваться со специалистами. Я всегда готов помочь в твоих усилиях по достижению физической формы и здоровья.
""",
                         parse_mode="HTML", reply_markup=main_menu_kb())

    await message.delete()


@dp.message_handler(lambda message: message.text == "Тренировки")
async def cmd_train(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo="""https://musclefit.info/wp-content/uploads/2021/02/programma-trenirovok-na-5-dnej.jpg""",
                         caption="""Отлично, выбери как хочешь заниматься """,
                         reply_markup=main_train_ikb())

    await message.delete()


# endregion
"""************************************************** ТРЕНИРОВКИ ДОМА *******************************************************************"""


@dp.callback_query_handler(lambda callback: callback.data == "тренировки_дома")
async def train_in_gym_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, photo="https://manfit.ru/local/img/home-fitness-600.jpg",
                         caption="Какую область хочешь прокачать?",
                         reply_markup=home_train_menu_ikb())
    await callback.message.delete()


# region muskle group home
@dp.callback_query_handler(lambda callback: callback.data == "верх_тела_дома")
async def home_train_upperbody_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://statusmen.ru/wp-content/uploads/2020/04/uprazhnenija-dlja-muzhchin-v-domashnih-uslovijah.jpg",
                         caption="Выбери группу мышц для тренировки",
                         reply_markup=home_train_upperbody_ikb())
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "спина_дома")
async def home_train_back_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.menslife.com/upload/iblock/287/kachaem_spinu_v_trenazhernom_zale.jpg",
                         caption="Выбери группу мышц для тренировки",
                         reply_markup=home_train_back_ikb())
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "пресс_дома")
async def home_train_back_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://fitseven.ru/wp-content/uploads/2019/03/uprajneniya-na-press-doma-900x600.jpg",
                         caption="Выбери упражнения для тренировки",
                         reply_markup=home_train_press_ikb())
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "ноги_дома")
async def home_train_legs_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://avatars.dzeninfra.ru/get-zen_doc/164147/pub_5ca39c0e8f7b6100b3fd0a17_5ca39d183f197100b3e9b8bd/scale_1200",
                         caption="Выбери упражнения для тренировки",
                         reply_markup=home_train_legs_ikb())
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "фулбади_дома")
async def home_train_legs_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://luna-askmen-images.askmen.com/1080x540/2018/03/08-044252-the_date_night_workout.jpg",
                         caption="Выбери упражнения для тренировки",
                         reply_markup=home_train_fulbody_ikb())
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "кардио_дома")
async def home_train_legs_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.nastroy.net/pic/images/202004/78415-1586881406.jpg",
                         caption="Выбери упражнения для тренировки",
                         reply_markup=home_train_kardio_ikb())
    await callback.message.delete()


# endregion
"""************************************************** Обработка мышц ДОМА *******************************************************************"""


# region обработка мышц верха тела HOME
@dp.callback_query_handler(lambda callback: callback.data == "трицепс_дома")
async def home_train_triceps_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://img.championat.com/c/1200x900/news/big/m/w/domashnjaja-trenirovka-uprazhnenija-dlja-muzhchin_15859067672068727188.jpg",
                         caption="Выбери упражнение",
                         reply_markup=home_train_triceps_ikb())
    await callback.answer()
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "бицепс_дома")
async def home_train_triceps_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://sportishka.com/uploads/posts/2022-11/1667579842_1-sportishka-com-p-krasivii-bitseps-krasivo-1.jpg",
                         caption="Выбери упражнение",
                         reply_markup=home_train_biceps_ikb())
    await callback.answer()
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "грудные_дома")
async def home_train_triceps_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://pic.sport.ua/images/media/orig/74/16035.jpg",
                         caption="Выбери упражнение",
                         reply_markup=home_train_chest_ikb())
    await callback.answer()
    await callback.message.delete()


# endregion
# region обработка мышц спины HOME
@dp.callback_query_handler(lambda callback: callback.data == "верх_спины_дома")
async def home_train_upperBACK_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.mentoday.ru/upload/img_cache/520/520660d70d1a56ed1f587fc62d3febab_ce_2800x1862x0x2_cropped_666x444.jpg",
                         caption="Выбери упражнение",
                         reply_markup=home_train_upperBACK_ikb())
    await callback.answer()
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "низ_спины_дома")
async def home_train_upperBACK_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://vashsport.com/wp-content/uploads/kak-nakachat-spinu-doma.jpg",
                         caption="Выбери упражнение",
                         reply_markup=home_train_downBACK_ikb())
    await callback.answer()
    await callback.message.delete()


# endregion
"""****************************************** ДОМА УПРАЖНЕНИЯ *******************************************************"""


# region triceps exersize HOME
@dp.callback_query_handler(lambda callback: callback.data == "отжимания_дома")
async def home_train_triceps_PUSH(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение:  отжимания')


@dp.callback_query_handler(lambda callback: callback.data == "отжимания_сзади_дома")
async def home_train_triceps_backPUSH(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение:\nотжимание с опорой сзади')


@dp.callback_query_handler(lambda callback: callback.data == "алмазные_отжимания_дома")
async def home_train_triceps_almazPUSH(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение:\nалмазные отжимания')


# endregion
# region biceps exeresize HOME
@dp.callback_query_handler(lambda callback: callback.data == "изоляция_бицепс_дома")
async def home_train_biceps_ispalte(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение:  изоляция бицепс')


@dp.callback_query_handler(lambda callback: callback.data == "упражнение_молоты_дома")
async def home_train_bicepse_molot(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение:  молотки')


# endregion
# region chest exersize HOME
@dp.callback_query_handler(lambda callback: callback.data == "отжимания_с_хлопком_дома")
async def home_train_chest_clapPUSH(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение:  отжимания с хлопком')


@dp.callback_query_handler(lambda callback: callback.data == "пуловер_дома")
async def home_train_chest_pulover(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение:  пуловер')


@dp.callback_query_handler(lambda callback: callback.data == "базовые_отжимания_дома")
async def home_train_triceps_basePUSH(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение:  базовые отжимания')


# endregion


# region uper back exersize HOME
@dp.callback_query_handler(lambda callback: callback.data == "тяга_с_опорой_дома")
async def home_train_upperback_pull_opora(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: тяга с упором')


@dp.callback_query_handler(lambda callback: callback.data == "пуловер_спины_дома")
async def home_train_upperback_pulover(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: пуловер спины')


# endregion
# region DOWNback exersize HOME
@dp.callback_query_handler(lambda callback: callback.data == "гиперэкстензия_дома")
async def home_train_downback_hyperextension(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: гиперэкстензия')


@dp.callback_query_handler(lambda callback: callback.data == "мини_становая_дома")
async def home_train_downback_miniDEADLIFT(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: мини становая')


# endregion


# region press exersize HOME
@dp.callback_query_handler(lambda callback: callback.data == "прямые_скручивания_дома")
async def home_train_press_curl(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Прямые скручивания')


@dp.callback_query_handler(lambda callback: callback.data == "боковые_скручивания_дома")
async def home_train_press_sideCURL(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Боковые скручивания')


@dp.callback_query_handler(lambda callback: callback.data == "подъем_ног_на_боку_дома")
async def home_train_press_side_legs(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Подъем ног лежа на боку')


@dp.callback_query_handler(lambda callback: callback.data == "скручивания_до_носков_дома")
async def home_train_press_touch_leg(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Касание носков')


# endregion


# region LEGS exersize HOME
@dp.callback_query_handler(lambda callback: callback.data == "приседания_с_весом_дома")
async def home_train_legs_squats(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Приседания с весом')


@dp.callback_query_handler(lambda callback: callback.data == "мини_становая_узко_дома")
async def home_train_legs_miniDEADLIFT(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: мини - становая узко')


@dp.callback_query_handler(lambda callback: callback.data == "хип_траст_дома")
async def home_train_legs_miniDEADLIFT(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Хип - Траст ')


# endregion


# region FULBODY exersize HOME
@dp.callback_query_handler(lambda callback: callback.data == "поднятие_веса_на_подобии_гири_дома")
async def home_train_fulbody_girya(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Взрыв снизу ')


@dp.callback_query_handler(lambda callback: callback.data == "берпи_дома")
async def home_train_fulbody_berpi(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Просто берпи')


# endregion


# region kardio HOME
@dp.callback_query_handler(lambda callback: callback.data == "гусеница_дома")
async def home_train_cardio_caterpillar(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Просто гусеница')


@dp.callback_query_handler(lambda callback: callback.data == "прыжки_дома")
async def home_train_cardio_jump(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Попрыгушки')


@dp.callback_query_handler(lambda callback: callback.data == "лестница_дома")
async def home_train_cardio_ladder(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: любимая лестница')


# endregion

"""************************************************** ТРЕНИРОВКИ В ЗАЛЕ *******************************************************************"""


@dp.callback_query_handler(lambda callback: callback.data == "тренировки_в_зале")
async def train_in_gym_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.goldsgym.ru/upload/medialibrary/4c0/4c05e8b013f2804d7beca4a07267698d.jpg",
                         caption="Какую область хочешь прокачать?",
                         reply_markup=gym_train_menu_ikb())
    await callback.message.delete()


# region muskle group GYM
@dp.callback_query_handler(lambda callback: callback.data == "верх_тела_зал")
async def gym_train_upperbody_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://builderbody.ru/wp-content/uploads/2017/12/1-10-850x599.jpg",
                         caption="Выбери группу мышц для тренировки",
                         reply_markup=gym_train_upperbody_ikb())
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "спина_зал")
async def home_train_back_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://xage.ru/media/posts/2015/2/24/pochemu-stoit-zanimatsja-v-trenazhernom-zale.jpg",
                         caption="Выбери группу мышц для тренировки",
                         reply_markup=gym_train_back_ikb())
    await callback.message.delete()


# endregion


"""************************************************** Обработка мышц GYM *******************************************************************"""


# region мышцы верха тела
@dp.callback_query_handler(lambda callback: callback.data == "трицепс_зал")
async def gym_train_triceps_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://img.championat.com/c/1200x900/news/big/m/w/domashnjaja-trenirovka-uprazhnenija-dlja-muzhchin_15859067672068727188.jpg",
                         caption="Выбери упражнение",
                         reply_markup=gym_train_triceps_ikb())
    await callback.answer()
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "бицепс_зал")
async def gym_train_biceps_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://sportishka.com/uploads/posts/2022-11/1667579842_1-sportishka-com-p-krasivii-bitseps-krasivo-1.jpg",
                         caption="Выбери упражнение",
                         reply_markup=gym_train_biceps_ikb())
    await callback.answer()
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "грудные_зал")
async def gym_train_chest_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://pic.sport.ua/images/media/orig/74/16035.jpg",
                         caption="Выбери упражнение",
                         reply_markup=gym_train_chest_ikb())
    await callback.answer()
    await callback.message.delete()


# endregion
# region мышцы спины
@dp.callback_query_handler(lambda callback: callback.data == "верх_спины_зал")
async def gym_train_upperBACK_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://vashsport.com/wp-content/uploads/uprazhneniya-dlya-spiny-v-trenazhernom-zale-640x480.jpg",
                         caption="Выбери упражнение",
                         reply_markup=gym_train_upperBACK_ikb())
    await callback.answer()
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "низ_спины_зал")
async def gym_train_downBACK_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://gercules.fit/wp-content/uploads/2018/12/Screenshot.png",
                         caption="Выбери упражнение",
                         reply_markup=gym_train_downBACK_ikb())
    await callback.answer()
    await callback.message.delete()


# endregion
# region мышцы НОГ
@dp.callback_query_handler(lambda callback: callback.data == "квадрицепс_зал")
async def gym_train_qvadriveps_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://builderbody.ru/wp-content/uploads/2016/09/1-2-850x487.jpg",
                         caption="Выбери упражнение",
                         reply_markup=gym_train_quadLEGS_ikb())
    await callback.answer()
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "задняя_часть_бедра_зал")
async def gym_train_bicepsLEGS_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://vashsport.com/wp-content/uploads/uprazhneniya-na-biceps-bedra.jpg",
                         caption="Выбери упражнение",
                         reply_markup=gym_train_bicepsLEGS_ikb())
    await callback.answer()
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "икроножные_мышцы_зал")
async def gym_train_icriLEGS_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.iphones.ru/wp-content/uploads/2017/05/01-Calf-and-Buttocks-Training.jpg",
                         caption="Выбери упражнение",
                         reply_markup=gym_train_icriLEGS_ikb())
    await callback.answer()
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "бедра_зал")
async def gym_train_assLEGS_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://img.championat.com/s/735x490/news/big/v/x/kachaem-vnutrennyuyu-poverhnost-bedra_16657512771904848910.jpg",
                         caption="Выбери упражнение",
                         reply_markup=gym_train_assLEGS_ikb())
    await callback.answer()
    await callback.message.delete()


# endregion
# region остальные мышцы
@dp.callback_query_handler(lambda callback: callback.data == "пресс_зал")
async def gym_train_press_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://the-challenger.ru/wp-content/uploads/2017/05/shutterstock_598276976.jpg",
                         caption="Выбери упражнения для тренировки",
                         reply_markup=gym_train_press_ikb())
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "плечи_зал")
async def gym_train_shoulders_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://www.muscleandfitness.com/wp-content/uploads/2018/05/1109-shoulders.jpg?quality=86&strip=all",
                         caption="Выбери упражнения для тренировки",
                         reply_markup=gym_train_shoulders_ikb())
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "ноги_зал")
async def gym_train_legs_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://musclefit.info/wp-content/uploads/2021/08/trenazhery-dlya-nog-v-trenazhernom-zale-min.jpg",
                         caption="Выбери упражнения для тренировки",
                         reply_markup=gym_train_legs_ikb())
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "всё_тело_зал")
async def gym_train_fulbody_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://musclefit.info/wp-content/uploads/2021/09/full-body-min.jpg",
                         caption="Выбери упражнения для тренировки",
                         reply_markup=gym_train_fulbody_ikb())
    await callback.message.delete()


@dp.callback_query_handler(lambda callback: callback.data == "кардио_зал")
async def gym_train_cardio_menu(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id,
                         photo="https://images.thevoicemag.ru/upload/img_cache/d0e/d0e39276def92ea645a041273703fa4a_cropped_666x445.jpg",
                         caption="Выбери упражнения для тренировки",
                         reply_markup=gym_train_kardio_ikb())
    await callback.message.delete()


# endregion

"""****************************************** GYM УПРАЖНЕНИЯ *******************************************************"""


# region ВЕРХ ТЕЛА ЗАЛ
@dp.callback_query_handler(lambda callback: callback.data == "франнузский_жим_зал")
async def gym_train_triceps_francePush(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: французкий жим')


@dp.callback_query_handler(lambda callback: callback.data == "жим_лежа_узким_хватом_зал")
async def gym_train_triceps_uzkoPUSH(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: жим лежа узким хватом')


@dp.callback_query_handler(lambda callback: callback.data == "жим_лежа_классика_зал")
async def gym_train_triceps_classicPUSH(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: жим лежа classic')


@dp.callback_query_handler(lambda callback: callback.data == "брусья_зал")
async def gym_train_triceps_brusiya(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: брусья')


@dp.callback_query_handler(lambda callback: callback.data == "кроссовер_зал")
async def gym_train_triceps_crossover(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: кроссовер')


@dp.callback_query_handler(lambda callback: callback.data == "подъем_изогнутого_грифа_зал")
async def gym_train_biceps_curlGRif(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: изогнутый на бицепс')


@dp.callback_query_handler(lambda callback: callback.data == "подъем_штанги_на_бицепс_зал")
async def gym_train_biceps_grif(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: штанга на бицепс')


@dp.callback_query_handler(lambda callback: callback.data == "гантели_развернутым_хватом_зал")
async def gym_train_biceps_gantel_ISOLATE(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Гантели изоляция')


@dp.callback_query_handler(lambda callback: callback.data == "упражнение_молоты_зал")
async def gym_train_biceps_molot(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Молоточки')


@dp.callback_query_handler(lambda callback: callback.data == "жим_гантелей_лежа_зал")
async def gym_train_chest_gantelPUSH(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Жим гантелей')


@dp.callback_query_handler(lambda callback: callback.data == "гантели_наклонная_скамья_зал")
async def gym_train_chest_gantel_curl_PUSH(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Жим гантелей на наклонной скамье')


@dp.callback_query_handler(lambda callback: callback.data == "штанга_наклонная_скамья_зал")
async def gym_train_chest_grif_curl_PUSH(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Жим штанги на наклонной скамье')


# endregion

# region СПИНА ЗАЛ
@dp.callback_query_handler(lambda callback: callback.data == "подтягивания_зал")
async def gym_train_upperBACK_grif_pull_ups(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: подтягивания')


@dp.callback_query_handler(lambda callback: callback.data == "тяга_на_наклонной_скамье_зал")
async def gym_train_upperBACK_lift_na_scamie(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: тяга на наклонной скамье')


@dp.callback_query_handler(lambda callback: callback.data == "тяга_на_наклонной_скамье_зал")
async def gym_train_upperBACK_grif_v_naklone(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: тяга штанги в наклоне')


@dp.callback_query_handler(lambda callback: callback.data == "тяга_одной_с_упором_зал")
async def gym_train_upperBACK_ift_one_hand(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: тяга одной рукой')


@dp.callback_query_handler(lambda callback: callback.data == "становая_тяга_зал")
async def gym_train_downBACK_deadlift(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Становая тяга')


@dp.callback_query_handler(lambda callback: callback.data == "гиперэкстензия_зал")
async def gym_train_downBACK_hyperextensy(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Гиперэкстензия')


# endregion

# region НОГИ ЗАЛ
@dp.callback_query_handler(lambda callback: callback.data == "присед_со_штангой_зал")
async def gym_train_quadLEGS_prised_grif(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Присед со штангой')


@dp.callback_query_handler(lambda callback: callback.data == "присед_с_гантелями_зал")
async def gym_train_quadLEGS_prised_gantel(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Присед с гантелями')


@dp.callback_query_handler(lambda callback: callback.data == "присед_на_одной_ноге_зал")
async def gym_train_bicepsLEGS_prised_one_legs(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Присед на одной ноге')


@dp.callback_query_handler(lambda callback: callback.data == "на_носки_штанга_зал")
async def gym_train_icriLEGS_na_noski_grif(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Подъемы на носки со штангой')


@dp.callback_query_handler(lambda callback: callback.data == "на_носки_гантели_зал")
async def gym_train_icriLEGS_na_noski_gantel(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Подъемы на носки со гантелями')


@dp.callback_query_handler(lambda callback: callback.data == "мостик_со_штангой_зал")
async def gym_train_assLEGS_most_grif(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Возьми эту дуру')


@dp.callback_query_handler(lambda callback: callback.data == "мостик_зал")
async def gym_train_assLEGS_most(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Возьми эту дуру')


# endregion

# region ПРЕСС ЗАЛ
@dp.callback_query_handler(lambda callback: callback.data == "прямые_скручивания_зал")
async def gym_train_press_right_curl(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Обычные скручивания')


@dp.callback_query_handler(lambda callback: callback.data == "боковые_скручивания_зал")
async def gym_train_press_bokoviy_curl(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Боковые скручивания')


@dp.callback_query_handler(lambda callback: callback.data == "боковые_с_доп_весом_зал")
async def gym_train_press_bokoviy_curl_dop(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Боковые скручивания с доп весом')


@dp.callback_query_handler(lambda callback: callback.data == "подъем_ног_на_брусьях_зал")
async def gym_train_press_bokoviy_curl_dop(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Подъем ног на брусьях')


# endregion

# region ПЛЕЧИ ЗАЛ
@dp.callback_query_handler(lambda callback: callback.data == "жим_арнольда_зал")
async def gym_train_shoulders_arnold_push(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Жим Арнольда')


@dp.callback_query_handler(lambda callback: callback.data == "жим_гантелей_вверх_зал")
async def gym_train_shoulders_up_push(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Жим на плечи')


@dp.callback_query_handler(lambda callback: callback.data == "протяжка_гантелей_зал")
async def gym_train_shoulders_protagca(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Протяжка')


@dp.callback_query_handler(lambda callback: callback.data == "махи_гантелями_зал")
async def gym_train_shoulders_mahi_gantel(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Махи гантелями')


@dp.callback_query_handler(lambda callback: callback.data == "подъем_штанги_над_головой_зал")
async def gym_train_shoulders_grif_up_head(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Подъем штанги над головой')


@dp.callback_query_handler(lambda callback: callback.data == "тяга_лежа_на_скамье_зал")
async def gym_train_shoulders_grif_up_head(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Тяга на задние дельты')


# endregion

# region ФУЛБАДИ ЗАЛ
@dp.callback_query_handler(lambda callback: callback.data == "взрыв_со_штангой_зал")
async def gym_train_fulbody_grif_boon(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Взрыв со штангой')


@dp.callback_query_handler(lambda callback: callback.data == "толкание_гири_зал")
async def gym_train_fulbody_girya(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Толкание гири')


# endregion

# region КАРДИО ЗАЛ
@dp.callback_query_handler(lambda callback: callback.data == "бокс_зал")
async def gym_train_cardio_box(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Бокс')


@dp.callback_query_handler(lambda callback: callback.data == "скакалка_зал")
async def gym_train_cardio_scacalka(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Скакалка')


@dp.callback_query_handler(lambda callback: callback.data == "Ходьба_зал")
async def gym_train_cardio_hodba(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Ходьба')


@dp.callback_query_handler(lambda callback: callback.data == "берпи_зал")
async def gym_train_cardio_berpi(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Берпи')


@dp.callback_query_handler(lambda callback: callback.data == "бег_зал")
async def gym_train_cardio_run(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Бег')


@dp.callback_query_handler(lambda callback: callback.data == "прыжки_зал")
async def gym_train_cardio_jump(callback: types.CallbackQuery):
    await callback.message.answer(
        "По ссылке можешь просмотреть правильную технику выполнения и советы для данного упражнения:\nместо для ссылки  ")
    await callback.answer('Упражнение: Попрыгушки')


# endregion

"""******************************************  *******************************************************"""


######## return handlers
@dp.callback_query_handler(lambda callback: callback.data == "главное_меню")
async def return_main_menu(callback: types.CallbackQuery):
    await callback.message.answer("Вы вернулись в главное меню", reply_markup=main_menu_kb())
    await callback.answer("Возврат в главное меню")
    await callback.message.delete()


if __name__ == "__main__":
    dp.middleware.setup(CustomMiddleware())
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
