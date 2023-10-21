# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram import Dispatcher
from aiogram.types import Message

router = Router()


@router.message()
async def other(message: Message):
    await message.answer("Прочитайте инструкцию. Что- то явно пошло "
                         "не так как планировалось!")
    await message.delete()
