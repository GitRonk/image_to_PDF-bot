# -*- coding: utf-8 -*-

from aiogram.filters import Filter
from aiogram.types import Message


class Instruction(Filter):
    async def __call__(self, message: Message):
        return message.text == "Инструкция"
