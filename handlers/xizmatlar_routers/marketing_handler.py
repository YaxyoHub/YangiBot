from aiogram import Router, F
from aiogram.types import CallbackQuery

from buttons.menu_buttons import back_call

marketing_router = Router()

# 📣 Marketing
@marketing_router.callback_query(F.data == "marketing")
async def marketing_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        "📣 Marketing avtomatizatsiyasi — mijozlarni avtomatik jalb qilish:\n\n"
        "✅ Email, SMS, Telegram kampaniyalari\n"
        "✅ Chatbotlar (ChatGPT asosida)\n"
        "✅ Lead generation tizimlari",
        reply_markup=back_call()
    )