# -*- coding: utf-8 -*-

import os
import shutil
from typing import List

import img2pdf
from aiogram import Bot
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import FSInputFile

from tg_bot.keyboards import main_menu
from tg_bot.filters import TrComplete
from tg_bot.misc.states import ImageTransfer
from tg_bot.middlewares import LongOperationMiddleware

router = Router()
router.message.middleware(LongOperationMiddleware())


def create_folder(folder: str) -> str:
    current_dir = os.getcwd()
    def_directory = current_dir + r"\data"
    if not os.path.exists(def_directory):
        os.mkdir(def_directory)
    new_directory = os.path.join(def_directory, folder)
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)
    return new_directory


@router.message(TrComplete(), ImageTransfer.transfer_start, flags={"long_operation": "upload_document"})
async def wrapper(massage: Message, state: FSMContext, bot: Bot):
    await massage.answer(text="Передача изображений завершена", reply_markup=main_menu)

    user_data = await state.get_data()
    user_id = massage.from_user.id
    directory = create_folder(str(user_id))
    await massage.answer(text="Начинаю обработку...")
    images: List = user_data["images"]
    image_list = []
    for count, photo in enumerate(images):
        image_name = fr"\{count}.jpg"
        image_name = f"{directory}" + image_name
        await bot.download(file=photo.file_id, destination=image_name)
        image_list.append(image_name)

    pdf_doc = fr"{directory}\result.pdf"
    with open(pdf_doc, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(image_list))

    await massage.answer("Обработка завершена...")
    file = FSInputFile(path=pdf_doc, filename="result.pdf")
    await bot.send_document(document=file, chat_id=massage.chat.id)
    shutil.rmtree(directory)
    await state.clear()
