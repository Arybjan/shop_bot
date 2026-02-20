from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.requests import get_producers, get_producer_item

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог"), KeyboardButton(text="Способ оплаты")],
        [KeyboardButton(text="Связаться с нами")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)


async def producers():
    all_producers = await get_producers()
    keyboard = InlineKeyboardBuilder()
    for producer in all_producers:
        keyboard.add(
            InlineKeyboardButton(
                text=producer.name, callback_data=f"producer_{producer.id}"
            )
        )
    keyboard.add(InlineKeyboardButton(text="На главную", callback_data="to_main"))
    return keyboard.adjust(2).as_markup()


async def items(producer_id):
    all_items = await get_producer_item(producer_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(
            InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}")
        )
    keyboard.add(InlineKeyboardButton(text="На главную", callback_data="to_main"))
    return keyboard.adjust(2).as_markup()
