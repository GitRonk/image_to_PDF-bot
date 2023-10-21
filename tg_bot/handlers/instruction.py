# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.types import Message
from tg_bot.filters import Instruction

router = Router()


@router.message(Instruction())
async def instruction(message: Message):
    text = ("<em>Данный бот принимает изображения и создает из них <b>PDF</b> файл. "
            "Порядок формирования страниц совпадает с порядком передачи изображений. "
            "Если хотите получить на выходе файл хорошего качества, передавайте "
            "изображения в виде документов. Для избежания флуда бот реагирует "
            "на сообщения раз в 3 сек кроме режима передачи картинок. "
            "Ограничение размера файла 20 страниц(20 картинок)</em>.")
    await message.answer(text=text, parse_mode="HTML")
    await message.delete()
