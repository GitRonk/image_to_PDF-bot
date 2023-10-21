# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from tg_bot.filters import CancelCommand
from tg_bot.keyboards import main_menu

router = Router()


@router.message(CancelCommand())
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text="<b>Отменено!</b>", reply_markup=main_menu, parse_mode="HTML")
    await message.delete()
