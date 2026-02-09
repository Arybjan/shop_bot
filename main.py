from aiogram import Bot, Dispatcher
from handlers import user
from os import getenv
from dotenv import load_dotenv

import asyncio
import logging
import sys

load_dotenv()

TOKEN = getenv("BOT_TOKEN")


# setup
async def main() -> None:
    dp = Dispatcher()
    bot = Bot(token=TOKEN)
    dp.include_router(user)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
