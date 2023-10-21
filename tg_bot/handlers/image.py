# -*- coding: utf-8 -*-

from typing import List

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tg_bot.misc import ImageTransfer
from tg_bot.filters import OnlyPhoto
from aiogram.types import ContentType

router = Router()


@router.message(OnlyPhoto(), ImageTransfer.transfer_start, flags={"transfer_image": "transfer_image"})
async def image(message: Message, state: FSMContext):
    if message.content_type == ContentType.PHOTO:
        photo = message.photo[-1]
        data = await state.get_data()
        images: List = data["images"]
        images.append(photo)
        await state.update_data({"images": images})
        date = await state.get_data()
        print(date)
    else:
        doc = message.document.mime_type
        if "image" in doc:
            data = await state.get_data()
            images: List = data["images"]
            images.append(message.document)
            await state.update_data({"images": images})
            date = await state.get_data()
            print(date)
        else:
            await message.answer("<b>Не подходящий тип документа!</b>", parse_mode="HTML")
            await message.delete()
