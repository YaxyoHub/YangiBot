from aiogram import Router, F
from aiogram.types import CallbackQuery

from buttons.menu_buttons import back_call

ai_router = Router()

# 🤖 AI integratsiyasi
@ai_router.callback_query(F.data == "AI")
async def AI_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "🤖 AI integratsiyasi — sun’iy intellekt yordamida samaradorlikni oshiring:\n\n"
        "✅ Mijozlar segmentatsiyasi\n"
        "✅ Tavsiyalar tizimi (Recommendation engine)\n"
        "✅ AI asosida savdo prognozlari",
        reply_markup=back_call()
    )