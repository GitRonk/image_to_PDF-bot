# -*- coding: utf-8 -*-

from aiogram.filters import Filter
from aiogram.types import Message


class TrComplete(Filter):
    async def __call__(self, message: Message):
        text = message.text
        return text == "Завершить передачу изображений"

