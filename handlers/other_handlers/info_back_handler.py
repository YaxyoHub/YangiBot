from aiogram import F, Router
from aiogram.types import CallbackQuery
from buttons.menu_buttons import main_menu, call_button, ortga_button, xizmatlar_button


info_back_router = Router()

@info_back_router.callback_query(F.data == "back")
async def go_back_menu(callback: CallbackQuery):
    await callback.message.edit_text("📋 Xizmatlar ro'yxati:", reply_markup=xizmatlar_button)

@info_back_router.callback_query(F.data == "go_back")
async def go_back_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🏢 Kompaniya botiga xush kelibsiz 😊\n"
        "Kompaniyamiz raqamli avtomatlashtirish xizmatini taklif qiladi",
        reply_markup=main_menu()
    )

# info
@info_back_router.callback_query(F.data == "info")
async def info_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("🏢 SmartBiz Solutions\n \n"
    "SmartBiz Solutions — bu O‘zbekistonda raqamli avtomatlashtirish\n"
    "va sun’iy intellekt yechimlari bo‘yicha yetakchi kompaniyalardan biri. \n \n"
    "🔹 Xizmatlarimiz:\n"
    "- CRM tizimlari\n"
    "- Call-Center yechimlari\n"
    "- Biznes jarayonlarni avtomatlashtirish\n"
    "- Marketing avtomatizatsiyasi\n"
    "- AI integratsiyasi\n \n"
    "🎯 Maqsadimiz: Biznesingizni soddalashtirish va texnologik yuksaltirish.\n"
    "📍 Manzil: Toshkent shahri, Yunusobod tumani, Amir Temur ko‘chasi, 107-uy\n"
    "🕒 Ish vaqti: Dushanba – Jum’a (09:00 – 18:00)\n"
    "📞 Aloqa:\n"
    "📱 Telefon: +998 90 123 45 67\n"
    "✉️ Email: info@smartbiz.uz  \n"
    "📱 Telegram: @smartbiz_admin  \n"
    "📸 Instagram: @smartbiz_uz  \n"
    "📍 Lokatsiya: https://maps.google.com/?q=Amir+Temur+ko'chasi+107,+Tashkent",reply_markup=ortga_button())
    reply_markup=call_button()

