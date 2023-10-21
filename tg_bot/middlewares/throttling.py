# -*- coding: utf-8 -*-

from typing import Callable
from typing import Any
from typing import Awaitable
from typing import Dict

from cachetools import TTLCache
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from cachetools import TTLCache


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self):
        self.cache = TTLCache(maxsize=100, ttl=3)

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        state: FSMContext = data["state"]
        current_state = await state.get_state()
        if current_state == "ImageTransfer:transfer_start":
            return await handler(event, data)
        else:
            user = event.from_user.id
            if user in self.cache:
                return
            self.cache[user] = True
            await handler(event, data)
