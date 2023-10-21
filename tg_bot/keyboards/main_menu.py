# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Начать передачу изображений")
        ],
        [
            KeyboardButton(text="Инструкция")
        ]
    ],
    resize_keyboard=True
)
