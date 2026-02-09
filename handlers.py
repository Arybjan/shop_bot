from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandStart, Command
import keyboards as kb

user = Router()


@user.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("hello", reply_markup=kb.menu)


@user.message(F.text == "Каталог")
async def msg_catalog(message: Message):
    await message.answer("Выберите Категорию товара", reply_markup=kb.catalog)


@user.message(Command("assort"))
async def assortiment_handler(message: Message):
    await message.answer("Элегет нахуй ээй")


@user.callback_query(F.data.startswith("brand_"))
async def check_brand(callback: CallbackQuery):
    brand_name = callback.data.split("_")[1]
    await callback.answer(f"Вы выбрали {brand_name.capitalize()}!")
    await callback.message.answer(f"Вы выбрали {brand_name.capitalize()}!")


@user.message()
async def echo_handler(message: Message) -> None:
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
