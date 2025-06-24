from aiogram import Router, F
from aiogram.types import CallbackQuery

from buttons.menu_buttons import back_call

crm_router = Router()

# 🧠 CRM
@crm_router.callback_query(F.data == "crm")
async def crm_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "📌 CRM tizimlari — mijozlaringizni tartibli boshqarish uchun:\n\n"
        "✅ AMO CRM, Bitrix24, Zoho CRM\n"
        "✅ Telegram, WhatsApp, Instagram bilan integratsiya\n"
        "✅ Avtomatik savdo hunari (sales funnel)\n"
        "✅ Segmentatsiya va tahliliy hisobotlar",
        reply_markup=back_call()
        
    )