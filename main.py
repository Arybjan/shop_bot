from aiogram import Bot, Dispatcher
from handlers import user
from os import getenv

import asyncio
import logging
import sys

TOKEN = getenv("BOT_TOKEN")

# setup
async def main() -> None:
    dp = Dispatcher()
    bot = Bot(token="8531573093:AAG06M4ufoAzjGxqTw8JIHuSiIlA47cbzsU")
    dp.include_router(user)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
