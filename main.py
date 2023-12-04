import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher

from src.commands import likvidirovat, start

dp = Dispatcher()
bot = Bot(token=getenv('TOKEN'), parse_mode='HTML')


async def main() -> None:
    dp.include_routers(start.router,
                       likvidirovat.router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    try:
        asyncio.run(main())
    except (SystemExit, KeyboardInterrupt):
        logging.warning('Bot stopped')
