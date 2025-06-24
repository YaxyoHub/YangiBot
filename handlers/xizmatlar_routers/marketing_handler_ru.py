from aiogram import Router, F
from aiogram.types import CallbackQuery

from buttons.menu_buttons import back_call_ru

marketing_router_ru = Router()

# 📣 Marketing
@marketing_router_ru.callback_query(F.data == "marketing_ru")
async def marketing_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "📣 Автоматизация маркетинга — автоматическое привлечение клиентов:\n\n"
        "✅ Кампании по электронной почте, СМС, Telegram\n"
        "✅ Чат-боты (на основе ChatGPT)\n"
        "✅ Системы генерации лидов",
        reply_markup=back_call_ru()
    )