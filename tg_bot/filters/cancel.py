# -*- coding: utf-8 -*-

from aiogram.filters import BaseFilter
from aiogram.types import Message


class CancelCommand(BaseFilter):
    async def __call__(self, message: Message):
        return message.text == "отмена"
