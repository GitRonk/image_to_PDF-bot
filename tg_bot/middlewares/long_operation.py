# -*- coding: utf-8 -*-

from typing import Callable
from typing import Any
from typing import Dict
from typing import Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender


class LongOperationMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        long_operation_type = get_flag(data, "long_operation")
        if not long_operation_type:
            return await handler(event, data)

        async with ChatActionSender(
                action=long_operation_type,
                chat_id=event.chat.id,
                bot=data["bot"]
        ):
            return await handler(event, data)
