# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from tg_bot.keyboards import main_menu

router = Router()


@router.message(CommandStart())
async def start_(message: Message):
    text = ("<em>Приветствую. Данный бот может конвертировать картинки в PDF файлы. "
            "Для получения инструкции нажмите на клавиатуре кнопку</em> <b>инструкция</b>.")
    await message.answer(text=text, parse_mode="HTML", reply_markup=main_menu)
    await message.delete()
