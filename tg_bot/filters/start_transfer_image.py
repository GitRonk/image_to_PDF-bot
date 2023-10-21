# -*- coding: utf-8 -*-

from aiogram.filters import Filter
from aiogram.types import Message


class TransferStart(Filter):
    async def __call__(self, message: Message):
        return message.text == "Начать передачу изображений"
