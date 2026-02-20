from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandStart, Command

import database.requests as rq
import keyboards as kb

user = Router()


@user.message(CommandStart())
async def command_start_handler(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer("Добро пожаловать в наш магазин!", reply_markup=kb.menu)


@user.message(F.text == "Каталог")
async def msg_catalog(message: Message):
    await message.answer("Выберите Категорию товара", reply_markup=await kb.producers())


@user.callback_query(F.data.startswith("producer_"))
async def call_producer(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию!")
    await callback.message.answer(
        "Выберите товар по категории",
        reply_markup=await kb.items(callback.data.split("_")[1]),
    )


@user.callback_query(F.data.startswith("item_"))
async def check_brand(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split("_")[1])
    await callback.answer(f"Вы выбрали товар!")
    await callback.message.answer(
        f"название {item_data.name}\nОписание {item_data.description}\nЦена {item_data.price}!",
        reply_markup=await kb.items(callback.data.split("_")[1]),
    )



@user.message(F.text == "Способ оплаты")
async def msg_payment(message: Message):
    await message.answer("Выберите Категорию товара", reply_markup=kb.menu)


@user.message(Command("assort"))
async def assortiment_handler(message: Message):
    await message.answer("Элегет нахуй ээй")


# @user.message()
# async def echo_handler(message: Message) -> None:
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")
