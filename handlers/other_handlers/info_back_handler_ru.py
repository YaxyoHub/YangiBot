from aiogram import F, Router
from aiogram.types import CallbackQuery
from buttons.menu_buttons import main_menu_ru, call_button_ru, ortga_button_ru, xizmatlar_button_ru


info_back_router_ru = Router()

@info_back_router_ru.callback_query(F.data == "back_ru")
async def go_back_menu(callback: CallbackQuery):
    await callback.message.edit_text("📋 Список услуг:", reply_markup=xizmatlar_button_ru)

@info_back_router_ru.callback_query(F.data == "go_back_ru")
async def go_back_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🏢 Добро пожаловать в бот компании 😊\n"
        "Наша компания предлагает услуги цифровой автоматизации",
        reply_markup=main_menu_ru()
    )

# info
@info_back_router_ru.callback_query(F.data == "info_ru")
async def info_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("🏢 SmartBiz Solutions\n \n"
    "SmartBiz Solutions — одна из ведущих компаний в области цифровой автоматизации\n"
    "и решений искусственного интеллекта в Узбекистане. \n \n"
    "🔹 Наши услуги:\n"
    "- CRM-системы\n"
    "- Решения для Call-центров\n"
    "- Автоматизация бизнес-процессов\n"
    "- Автоматизация маркетинга\n"
    "- Интеграция ИИ\n \n"
    "🎯 Наша цель: Упростить и технологически модернизировать ваш бизнес.\n"
    "📍 Адрес: г. Ташкент, Юнусабадский район, ул. Амира Темура, дом 107\n"
    "🕒 График работы: понедельник - пятница (09:00 - 18:00)\n"
    "📞 Контакты:\n"
    "📱 Телефон: +998 90 123 45 67\n"
    "✉️ Электронная почта: info@smartbiz.uz \n"
    "📱 Телеграмма: @smartbiz_admin \n"
    "📸 Instagram: @smartbiz_uz \n"
    "📍 Локация: https://maps.google.com/?q=Amir+Temur+ko'chasi+107,+Tashkent",reply_markup=ortga_button_ru())
    reply_markup=call_button_ru()

