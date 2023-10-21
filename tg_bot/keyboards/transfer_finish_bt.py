# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

finish_transfer = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Завершить передачу изображений")
        ],
        [
            KeyboardButton(text="отмена")
        ]
    ],
    resize_keyboard=True
)
