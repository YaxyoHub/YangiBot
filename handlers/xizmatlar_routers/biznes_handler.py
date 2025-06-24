from aiogram import Router, F
from aiogram.types import CallbackQuery

from buttons.menu_buttons import back_call

biznes_router = Router()

# ⚙️ Biznes avtomatlashtirish
@biznes_router.callback_query(F.data == "biznes")
async def biznes_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "⚙️ Biznes avtomatlashtirish — ichki jarayonlarni soddalashtiring:\n\n"
        "✅ Loyiha boshqaruvi (ClickUp, Trello, Notion)\n"
        "✅ Ishchilar monitoringi (Clockify, Hubstaff)\n"
        "✅ Power BI va Excel orqali avtomatik hisobotlar",
        reply_markup=back_call()
    )