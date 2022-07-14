import asyncio

import aiogram.utils.markdown as fmt
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from aiogram.types.message import ContentType
from aiogram.dispatcher.filters import Command
import handlers.keyboard as kb
from create_bot import dp, lilabred_bot
from aiogram.dispatcher.filters import Text
from handlers.text_courses import courses
from handlers.text_contacts import contacts
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Привет! Выбери нужную опцию:",
        reply_markup=kb.first_choice_button,
    )


# ____________________________________________Выбор опции___________________________________________________________


@dp.message_handler(lambda message: message.text and "курсы" in message.text.lower())
# Выбираем курсы
async def course_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        f"{courses}",
        reply_markup=kb.first_choice_button,
    )


@dp.message_handler(lambda message: message.text and "контакты" in message.text.lower())
# Выбираем контакты
async def contacts_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        f"{contacts}",
        reply_markup=kb.first_choice_button,
    )


@dp.message_handler(lambda message: message.text and "прайс" in message.text.lower())
# Выбираем прайс
async def price_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Какая прическа тебя интересует?",
        reply_markup=kb.price_choice_button,
    )


@dp.message_handler(
    lambda message: message.text and "назад к выбору опций" in message.text.lower()
)
# Курсы/Контакты/Прайс < Возвращаемся к выбору между курсы/контакты/прайс
async def options_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери нужную опцию:",
        reply_markup=kb.first_choice_button,
    )


# ____________________________________________Выбран прайс___________________________________________________________


@dp.message_handler(
    lambda message: message.text and "афрокосички точечно" in message.text.lower()
)
# Опции > Прайс > Выбираем афрокосички - предоставлен выбор зоны
async def afro_zone_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери зону прически:",
        reply_markup=kb.afro_zone_choice_button,
    )


@dp.message_handler(lambda message: message.text and "брейды" in message.text.lower())
# Опции > Прайс > Выбираем брейды - предоставлен выбор зоны
async def breds_zone_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери зону прически:",
        reply_markup=kb.breds_zone_choice_button,
    )


@dp.message_handler(
    lambda message: message.text and "афрохвост" in message.text.lower()
)
# Опции > Прайс > Выбираем афрохвост
async def tail_length_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери длину афрохвоста:",
        reply_markup=kb.tail_length_button,
    )


@dp.message_handler(
    lambda message: message.text and "назад к выбору прически" in message.text.lower()
)
# Опции > Прайс < Возвращаемся в Прайс (выбор между афрокосички/брейды/афрохвост)
async def price_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Какая прическа тебя интересует?",
        reply_markup=kb.price_choice_button,
    )


# ___________________________________________Выбраны афрокосички > выбор зоны______________________________________________________


@dp.message_handler(
    lambda message: message.text and "на всю голову" in message.text.lower()
)
# Опции > Прайс > Афрокосички точечно > Выбор зоны - Выбираем афрокосички на всю голову - предоставлен выбор толщины
async def afro_head_value_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери толщину/количество косичек:",
        reply_markup=kb.afro_head_thickness_button,
    )


@dp.message_handler(
    lambda message: message.text and "на андеркат(макушка)" in message.text.lower()
)
# Опции > Прайс > Афрокосички точечно > Выбор зоны - Выбираем афрокосички на макушку - предоставлен выбор толщины
async def afro_undercut_value_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери толщину/количество косичек:",
        reply_markup=kb.afro_undercut_thickness_button,
    )


@dp.message_handler(
    lambda message: message.text
    and "назад к выбору зоны для афрокосичек" in message.text.lower()
)
# Опции > Прайс > Афрокосички точечно > Выбор зоны < Возвращаемся к выбору зоны для афрокосичек
async def afro_zone_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери зону прически:",
        reply_markup=kb.afro_zone_choice_button,
    )


# ___________________________________________Выбраны афрокосички > зона: на всю голову______________________________________________________


@dp.message_handler(
    lambda message: message.text and "крупные(20-40 шт.)" in message.text.lower()
)
async def afro_head_big(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Afro_head_big.JPG", "rb"),
        caption="Крупные(20-40 шт.) – 16 500 руб.",
    )


@dp.message_handler(
    lambda message: message.text and "толстые(40-60 шт.)" in message.text.lower()
)
async def afro_head_thick(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Afro_head_thick.JPG", "rb"),
        caption="Толстые(40-60 шт.) – 18 500 руб.",
    )


@dp.message_handler(
    lambda message: message.text and "средние(60-80 шт.)" in message.text.lower()
)
async def afro_head_middle(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Afro_head_middle.JPG", "rb"),
        caption="Средние(60-80 шт.) – 20 000 руб.",
    )


@dp.message_handler(
    lambda message: message.text and "мелкие(80-100 шт.)" in message.text.lower()
)
async def afro_head_small(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Afro_head_small.JPG", "rb"),
        caption="Мелкие(80-100 шт.) – 23 500 руб.",
    )


# ___________________________________________Выбраны афрокосички > зона: на макушку______________________________________________________


@dp.message_handler(
    lambda message: message.text and "крупные(10-20 шт.)" in message.text.lower()
)
async def afro_undercut_big(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Afro_undercut_big.JPG", "rb"),
        caption="Крупные(10-20 шт.) – 6 500 руб.",
    )


@dp.message_handler(
    lambda message: message.text and "толстые(30-40 шт.)" in message.text.lower()
)
async def afro_undercut_thick(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Afro_undercut_thick.JPG", "rb"),
        caption="Толстые(30-40 шт.) – 8 500 руб.",
    )


@dp.message_handler(
    lambda message: message.text and "средние(40-60 шт.)" in message.text.lower()
)
async def afro_undercut_small(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Afro_undercut_middle.JPG", "rb"),
        caption="Средние(40-60 шт.) – 10 000 руб.",
    )


"""
@dp.message_handler(lambda message: message.text and 'назад к выбору количества косичек' in message.text.lower())
async def afro_head_value_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери толщину/количество косичек:",
        reply_markup=kb.afro_head_thickness_button,
    )
"""
# ___________________________________________Выбраны брейды > выбор зоны______________________________________________________


@dp.message_handler(lambda message: message.text and "брейды" in message.text.lower())
async def breds_zone_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери зону прически:",
        reply_markup=kb.breds_zone_choice_button,
    )


@dp.message_handler(
    lambda message: message.text and "вся голова" in message.text.lower()
)
async def breds_head_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери количество брейдов с учетом указания необходимости материалов:",
        reply_markup=kb.breds_head_thickness_button,
    )


@dp.message_handler(
    lambda message: message.text and "андеркат(макушка)" in message.text.lower()
)
async def breds_undercut_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери количество брейдов с учетом указания необходимости материалов:",
        reply_markup=kb.breds_undercut_thickness_button,
    )


@dp.message_handler(
    lambda message: message.text and "назад к выбору прически" in message.text.lower()
)
# Опции > Прайс < Возвращаемся в Прайс (выбор между афрокосички/брейды/афрохвост)
async def price_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Какая прическа тебя интересует?",
        reply_markup=kb.price_choice_button,
    )


# ___________________________________________Выбраны зоны брейдов: вся голова > выбор количества косичек______________________________________________________


@dp.message_handler(
    lambda message: message.text and "с материалом: 2-4 шт." in message.text.lower()
)
async def breds_head_material_1(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Breds_head_materials_middle.JPG", "rb"),
        caption="Брейды: 2-4 шт. – 4 500 руб.",
    )


@dp.message_handler(
    lambda message: message.text and "с материалом: 5-7 шт." in message.text.lower()
)
async def breds_head_material_2(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Breds_head_materials_thick.JPG", "rb"),
        caption="Брейды: 5-7 шт. – 6 500 руб.",
    )


@dp.message_handler(
    lambda message: message.text and "с материалом: 8-10 шт." in message.text.lower()
)
async def breds_head_material_3(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Breds_head_materials_big.JPG", "rb"),
        caption="Брейды: 8-10 шт. – 7 500 руб.",
    )


@dp.message_handler(
    lambda message: message.text and "без материала: 5-7 шт." in message.text.lower()
)
async def breds_head_2(message: types.Message):
    await lilabred_bot.send_photo(
        chat_id=message.from_user.id,
        photo=open("photos/Breds_head_thick.jpg", "rb"),
        caption="Брейды: 5-7 шт. – 4 500 руб.",
    )


@dp.message_handler(
    lambda message: message.text and "без материала: 8-10 шт." in message.text.lower()
)
async def breds_head_3(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "6 000 руб.")


@dp.message_handler(
    lambda message: message.text and "без материала: 2-4 шт." in message.text.lower()
)
async def breds_head_1(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "2 000 руб.")


""" КОГДА ПОЯВЯТСЯ ФОТКИ


@dp.message_handler(lambda message: message.text and 'без материала: 8-10 шт.' in message.text.lower())
async def afro_zone_head_choice(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Breds_head_big.JPG", "rb"), caption = "8-10 шт. – 6 000 руб.")

@dp.message_handler(lambda message: message.text and 'без материала: 2-4 шт.' in message.text.lower())
async def afro_zone_head_choice(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Breds_head_middle.JPG", "rb"), caption = "2-4 шт. – 2 000 руб.")

"""

# ___________________________________________Выбраны зоны брейдов: андеркат(макушка) > выбор количества косичек______________________________________________________


@dp.message_handler(
    lambda message: message.text and "с матeриалом: 2-4 шт." in message.text.lower()
)
async def breds_undercut_material_1(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "3 500 руб.")


@dp.message_handler(
    lambda message: message.text and "с матeриалом: 5-7 шт." in message.text.lower()
)
async def breds_undercut_material_2(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "4 500 руб.")


@dp.message_handler(
    lambda message: message.text and "с матeриалом: 8-10 шт." in message.text.lower()
)
async def breds_undercut_material_3(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "5 500 руб.")


@dp.message_handler(
    lambda message: message.text and "без матeриала: 2-4 шт." in message.text.lower()
)
async def breds_undercut_1(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "3 500 руб.")


@dp.message_handler(
    lambda message: message.text and "без матeриала: 5-7 шт." in message.text.lower()
)
async def breds_undercut_2(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "4 500 руб.")


@dp.message_handler(
    lambda message: message.text and "без матeриала: 8-10 шт." in message.text.lower()
)
async def breds_undercut_3(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "4 500 руб.")


""" КОГДА ПОЯВЯТСЯ ФОТКИ

@dp.message_handler(lambda message: message.text and 'с материалом: 2-4 шт. ' in message.text.lower())
async def breds_undercut_material_1(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Breds_undercut_materials_middle.JPG", "rb"), caption = "2-4 шт. – 4 500 руб.")

@dp.message_handler(lambda message: message.text and 'с материалом: 5-7 шт. ' in message.text.lower())
async def breds_undercut_material_2(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Breds_undercut_materials_thick.JPG", "rb"), caption = "5-7 шт. – 6 500 руб.")


@dp.message_handler(lambda message: message.text and 'с материалом: 8-10 шт. ' in message.text.lower())
async def breds_undercut_material_3(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Breds_undercut_materials_big.JPG", "rb"), caption = "8-10 шт. – 7 500 руб.")


@dp.message_handler(lambda message: message.text and 'без материала: 2-4 шт. ' in message.text.lower())
async def breds_undercut_1(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Breds_undercut_middle.JPG", "rb"), caption = "8-10 шт. – 2 000 руб.")

@dp.message_handler(lambda message: message.text and 'без материала: 5-7 шт. ' in message.text.lower())
async def breds_undercut_2(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Breds_undercut_thick.JPG", "rb"), caption = "8-10 шт. – 4 500 руб.")

@dp.message_handler(lambda message: message.text and 'без материала: 8-10 шт. ' in message.text.lower())
async def breds_undercut_3(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Breds_undercut_big.JPG", "rb"), caption = "8-10 шт. – 6 000 руб.")

"""


@dp.message_handler(
    lambda message: message.text
    and "назад к выбору зоны для брейдов" in message.text.lower()
)
# Опции > Прайс > Афрокосички точечно > Выбор зоны < Возвращаемся к выбору зоны для афрокосичек
async def breds_zone_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Выбери зону прически:",
        reply_markup=kb.breds_zone_choice_button,
    )


# ___________________________________________Выбран афрохвост > выбор длины______________________________________________________


@dp.message_handler(
    lambda message: message.text and "длинный хвост(75-80 см.)" in message.text.lower()
)
# Опции > Прайс > Афрохвост > Выбор длины - длинный хвост
async def tail_lenght_long(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "5 000руб.")


@dp.message_handler(
    lambda message: message.text and "средний хвост(55-60 см.)" in message.text.lower()
)
# Опции > Прайс > Афрохвост > Выбор длины - средний хвост
async def tail_lenght_middle(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "4 000руб.")


@dp.message_handler(
    lambda message: message.text and "короткий хвост(40-45 см.)" in message.text.lower()
)
# Опции > Прайс > Афрохвост > Выбор длины - короткий хвост
async def tail_lenght_short(message: types.Message):
    await lilabred_bot.send_message(message.from_user.id, "3 000руб.")


@dp.message_handler(
    lambda message: message.text and "назад к выбору прически" in message.text.lower()
)
# Опции > Прайс < Возвращаемся в Прайс (выбор между афрокосички/брейды/афрохвост)
async def price_choice(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Какая прическа тебя интересует?",
        reply_markup=kb.price_choice_button,
    )


"""
КОГДА ПОЯВЯТСЯ ФОТКИ

@dp.message_handler(lambda message: message.text and 'длинный хвост(75-80 см.)' in message.text.lower())
# Опции > Прайс > Афрохвост > Выбор длины - длинный хвост
async def tail_lenght_long(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Tail_long.JPG", "rb"), caption = "Длинный хвост(75-80 см.) – 5 000руб.")


@dp.message_handler(lambda message: message.text and 'средний хвост(55-60 см.)' in message.text.lower())
# Опции > Прайс > Афрохвост > Выбор длины - средний хвост
async def tail_lenght_middle(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Tail_middle.JPG", "rb"), caption = "Средний хвост(55-60 см.) – 4 000руб.")


@dp.message_handler(lambda message: message.text and 'короткий хвост(40-45 см.)' in message.text.lower())
# Опции > Прайс > Афрохвост > Выбор длины - короткий хвост
async def tail_lenght_short(message: types.Message):
    await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Tail_short.JPG", "rb"), caption = "Короткий хвост(40-45 см.) – 3 000руб.")

"""

# ___________________________________________UNKNOWN_MESSAGE______________________________________________________


@dp.message_handler(content_types=types.ContentType.ANY)
async def unknown_message(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Я не понимаю это сообщение. Введи:\nПрайс - если хочешь узнать прайс по прическам,\nКурсы - если хочешь узнать информацию о курсах,\nКонтакты - и я покажу тебе как связаться с LilaBred.\n/start - и мы начнем общение заново.",
    )


# ___________________________________________CANCEL______________________________________________________


@dp.message_handler(state="*", commands="cancel")
@dp.message_handler(Text(equals="cancel", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return


"""
@dp.message_handler(lambda message: message.text and 'прайс' in message.text.lower())
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Выполнение команды прервано")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start"])

    dp.register_message_handler(price_choice, commands=["Прайс"], commands_prefix='!/')

    # dp.register_message_handler(start_game, commands=["startgame"])

    # dp.register_message_handler(search_step_1, commands=["search"])

    dp.register_message_handler(cmd_cancel, commands=["cancel"], state="*")

    # dp.register_message_handler(Ellis_step_1, commands=["Опросить_администратора"])

    # dp.register_message_handler(Robert_kill, commands=["Убийца-Роберт."])

    #dp.register_message_handler(unknown_message, content_types=ContentType.ANY)
"""

"""

async def first_choise(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Привет! Выбери нужную опцию:",
        reply_markup=kb.first_choise_button,
    )
"""
'''
async def start_game(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        fmt.text(
            fmt.text(
                "Холодный осенний вечер. Почти полночь. Вы только что пришли домой с работы, присели в кресло, открыли бутылку виски, включили телевизор, и, предвкушая спокойный вечер, закуриваете сигарету."
            ),
            fmt.text("Вдруг телефон зазвонил. Звонок от вашего начальника."),
            fmt.hitalic("...Черт, ну что там опять???"),
            sep="\n",
        ),
        parse_mode="HTML",
    )
    await asyncio.sleep(5)
    await lilabred_bot.send_message(
        message.from_user.id,
        fmt.text(
            fmt.hbold("Начальник:"),
            fmt.text(
                "-Добрый вечер, детектив... Извини за поздний звонок, но нужно подъехать на пристань. У нас новое дело, и оно не терпит отлагательств."
            ),
            sep="\n",
        ),
        parse_mode="HTML",
    )
    await asyncio.sleep(3)
    await lilabred_bot.send_message(
        message.from_user.id,
        """Вы с нехотой собираетесь, что ж, долг зовет, нельзя отказываться, тем более, что раз уж позвонили Вам...
    Такси быстро примчало Вас к пристани, поднявшись на борт, Вы оцениваете обстановку. 
    Ваши коллеги докладывают Вам, что сегодня, ровно в три часа ночи, на лайнере «Олимпик», во время вечеринки, был убит мужчина.""",
    )
    await asyncio.sleep(5)

    async def send_photo():
        chat_id = message.from_user.id
        await lilabred_bot.send_photo(chat_id=message.from_user.id, photo=open("photos/Mark.jpg", "rb"))

    await send_photo()
    await asyncio.sleep(10)

    await lilabred_bot.send_message(
        message.from_user.id,
        """
    Мужчину нашли в каюте администратора палубы, с травмой головы.
    Ваш коллега, который будет расследовать с Вами дело, выяснил, что тело Марка обнаружила администратор палубы, но он еще не успел ее опросить. Разгадайте загадку и найдите убийцу. Раскрыть дело нужно максимально тихо, дабы не тревожить покой остальных гостей лайнера.""",
    )
    await asyncio.sleep(5)
    await lilabred_bot.send_message(
        message.from_user.id, "Начнем раскрывать убийство? Введи команду /search"
    )


async def search_step_1(message: types.Message):
    await lilabred_bot.send_message(
        message.from_user.id,
        "Так как о теле в полицию сообщила администратор - Вы решили начать опрос с нее, как с главного свидетеля этого убийства.",
        reply_markup=kb_M.kb_client_Ellis_1,
    )

async def you_win(chat_id):
    async def send_photo_done(chat_id):
        await bot_game.send_photo(chat_id=chat_id, photo=open("photos/Close.jpg", "rb"))
        await asyncio.sleep(10)

    async def send_confession(chat_id):
        await bot_game.send_photo(
            chat_id=chat_id, photo=open("photos/Confession.jpg", "rb")
        )
        await asyncio.sleep(10)

    async def send_win(chat_id):
        await bot_game.send_photo(chat_id=chat_id, photo=open("photos/Win.jpg", "rb"))
        await asyncio.sleep(10)

    await send_photo_done(chat_id)
    await send_win(chat_id)
    await send_confession(chat_id)


async def Robert_kill(message: types.Message):
    chat_id = message.from_user.id
    await you_win(chat_id)

    await bot_game.send_message(
        message.from_user.id,
        "Поздравляю, детектив, Вы блестяще раскрыли дело! Шикарная работа, снимаю перед Вами шляпу! До новых встреч)",
        reply_markup=types.ReplyKeyboardRemove(),
    )
'''
