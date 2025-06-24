from aiogram import Router, F
from aiogram.types import CallbackQuery

from buttons.menu_buttons import back_call_ru

biznes_router_ru = Router()

# ⚙️ Biznes avtomatlashtirish
@biznes_router_ru.callback_query(F.data == "biznes_ru")
async def biznes_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "⚙️ Автоматизация бизнеса — оптимизация внутренних процессов:\n\n"
        "✅ Управление проектами (ClickUp, Trello, Notion)\n"
        "✅ Мониторинг сотрудников (Clockify, Hubstaff)\n"
        "✅ Автоматические отчеты через Power BI и Excel",
        reply_markup=back_call_ru()
    )