from aiogram import Router, F
from aiogram.types import CallbackQuery

from buttons.menu_buttons import back_call_ru

crm_router_ru = Router()

# 🧠 CRM
@crm_router_ru.callback_query(F.data == "crm_ru")
async def crm_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "📌 CRM-системы — для упорядоченного управления вашими клиентами:\n\n"
        "✅ AMO CRM, Bitrix24, Zoho CRM\n"
        "✅ Интеграция с Telegram, WhatsApp, Instagram\n"
        "✅ Автоматическая воронка продаж (sales funnel)\n"
        "✅ Сегментация и аналитические отчеты",
        reply_markup=back_call_ru()
        
    )