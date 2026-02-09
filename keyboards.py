from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Католог")],
        [KeyboardButton(text="Contacts")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню"
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Waka 10k", callback_data="brand_waka-10k")],
        [InlineKeyboardButton(text="Waka 35k", callback_data="brand_waka-35k")],
        [InlineKeyboardButton(text="Lost Merry 20k", callback_data="brand_Lost Merry-20k")]
    ]
)