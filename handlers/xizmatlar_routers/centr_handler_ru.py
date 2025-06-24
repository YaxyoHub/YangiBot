from aiogram import Router, F
from aiogram.types import CallbackQuery

from buttons.menu_buttons import back_call_ru

centr_router_ru = Router()

# ☎️ Call-Center
@centr_router_ru.callback_query(F.data == "centr_ru")
async def centr_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "📞 Системы Call-Center — для эффективной коммуникации с вашими клиентами:\n\n"
        "✅ IP-телефония (Zadarma, Binotel)\n"
        "✅ IVR (автоматическое меню)\n"
        "✅ Полная интеграция с CRM\n"
        "✅ Контроль работы операторов",
        reply_markup=back_call_ru()
    )