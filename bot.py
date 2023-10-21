# -*- coding: utf-8 -*-

import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from environs import Env

from tg_bot import handlers
from tg_bot.middlewares import ThrottlingMiddleware
from tg_bot.middlewares import ImageLimitMiddleware

env = Env()
env.read_env()
BOT_TOKEN = env.str("BOT_TOKEN")


def register_all_middleware(dp: Dispatcher) -> None:
    dp.message.outer_middleware(ThrottlingMiddleware())
    dp.message.outer_middleware(ImageLimitMiddleware())


def register_all_handlers(dp: Dispatcher) -> None:
    dp.include_router(handlers.start.router)
    dp.include_router(handlers.instruction.router)
    dp.include_router(handlers.start_image_transfer.router)
    dp.include_router(handlers.image.router)
    dp.include_router(handlers.image_transfer_complete.router)
    dp.include_router(handlers.cancel_operation.router)

    dp.include_router(handlers.other.router)


async def main():
    logging.basicConfig(filename="log_file.log",
                        format="%(asctime)s %(levelname)s %(message)s",
                        level=logging.INFO,
                        encoding="utf-8")

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    register_all_middleware(dp)
    register_all_handlers(dp)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as ex:
        logging.warning(ex, exc_info=True)
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped!")
