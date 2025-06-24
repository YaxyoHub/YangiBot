from aiogram import Router, F
from aiogram.types import CallbackQuery

from buttons.menu_buttons import back_call

centr_router = Router()

# ☎️ Call-Center
@centr_router.callback_query(F.data == "centr")
async def centr_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "📞 Call-Center tizimlari — mijozlaringiz bilan samarali aloqa uchun:\n\n"
        "✅ IP telefoniya (Zadarma, Binotel)\n"
        "✅ IVR (avtomatik menyu)\n"
        "✅ CRM bilan to‘liq integratsiya\n"
        "✅ Operatorlar monitoring",
        reply_markup=back_call()
    )