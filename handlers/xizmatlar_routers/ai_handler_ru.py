from aiogram import Router, F
from aiogram.types import CallbackQuery

from buttons.menu_buttons import back_call_ru

ai_router_ru = Router()

# 🤖 AI integratsiyasi
@ai_router_ru.callback_query(F.data == "AI_ru")
async def AI_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "🤖 Интеграция ИИ — повышение эффективности с помощью искусственного интеллекта:\n\n"
        "✅ Сегментация клиентов\n"
        "✅ Рекомендательный движок\n"
        "✅ Прогнозирование продаж на основе ИИ",
        reply_markup=back_call_ru()
    )