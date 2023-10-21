# -*- coding: utf-8 -*-

from typing import Callable
from typing import Any
from typing import Awaitable
from typing import Dict

from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types.message import ContentType


def check_content_type(message: Message):
    content_type = message.content_type
    is_photo = content_type == ContentType.PHOTO
    is_document = content_type == ContentType.DOCUMENT
    return is_document or is_photo


class ImageLimitMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        state: FSMContext = data["state"]
        current_state = await state.get_state()
        if current_state == "ImageTransfer:transfer_start" and check_content_type(event):
            state_data = await state.get_data()
            limit = state_data["limit"] - 1
            await state.update_data({"limit": limit})
            if limit < 0:
                await event.delete()
                return
            return await handler(event, data)

        else:
            await handler(event, data)
