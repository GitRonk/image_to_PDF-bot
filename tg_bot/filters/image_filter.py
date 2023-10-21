# -*- coding: utf-8 -*-

from aiogram.types import ContentType
from aiogram.filters import Filter
from aiogram.types import Message


class OnlyPhoto(Filter):
    async def __call__(self, message: Message):
        check_photo = message.content_type == ContentType.PHOTO
        check_doc = message.content_type == ContentType.DOCUMENT
        if check_doc or check_photo:
            return True
        return False
