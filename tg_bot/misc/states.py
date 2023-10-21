# -*- coding: utf-8 -*-

from aiogram.filters.state import StatesGroup
from aiogram.filters.state import State


class ImageTransfer(StatesGroup):
    transfer_start = State()
    converting = State()


