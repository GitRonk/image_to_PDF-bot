# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tg_bot.filters import TransferStart
from tg_bot.misc import ImageTransfer
from tg_bot.keyboards import finish_transfer

router = Router()


@router.message(TransferStart())
async def start_transfer(message: Message, state: FSMContext):
    await message.answer(
        text="Отправьте изображения в нужном порядке. Макс 20 шт",
        reply_markup=finish_transfer)
    await state.set_state(ImageTransfer.transfer_start)
    await state.update_data({"images": []})
    await state.update_data({"quantity": 0})
    await state.update_data(({"limit": 20}))
