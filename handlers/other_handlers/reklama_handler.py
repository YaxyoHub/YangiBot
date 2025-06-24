import time
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from loader import IsBotAdminFilter, bot, ADMIN_ID

from states.state import Adverts
from database.sql import get_user

reklama_router = Router()


# ✅ Reklama holatiga o‘tish
@reklama_router.callback_query(F.data == "send_ad", IsBotAdminFilter(ADMIN_ID))
async def advert_dp(message: CallbackQuery, state: FSMContext):
    await state.set_state(Adverts.adverts)
    await message.message.answer(text="Reklama yuborishingiz mumkin!")


# ✅ Reklama yuborish
@reklama_router.message(Adverts.adverts)
async def send_advert(message: Message, state: FSMContext):
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = get_user()
    count = 0

    for user in users:
        try:
            await bot.copy_message(chat_id=user[2], from_chat_id=from_chat_id, message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)

    await message.answer(f"✅ Reklama {count} ta foydalanuvchiga yuborildi")
    await state.clear()
