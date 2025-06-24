from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from loader import bot, ADMIN_ID

# admin_id = int(ADMIN_ID)

from states.state import ContactForm
from buttons.menu_buttons import ortga_button, main_menu, cancel_button, phone_btn

boglanish_router = Router()

@boglanish_router.callback_query(F.data == "cancel")
async def boglanish(message: CallbackQuery):
    await message.message.delete()
    await message.message.answer("Bekor qilindi", reply_markup=main_menu())

@boglanish_router.callback_query(F.data == "call")
async def call_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer("""Admin bilan bog'lanish: 

👤 Ismi: Amriddin
📞 Telefon raqami: +998919710197
🇺🇿 Telegram: @Kholmatov_amriddin

Agar hohlasangiz ismingizni kiriting:""", reply_markup=cancel_button)
    await state.set_state(ContactForm.name)

@boglanish_router.message(ContactForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamingizni kiriting (masalan: +998901234567):", reply_markup=phone_btn)
    await state.set_state(ContactForm.phone)


@boglanish_router.message(ContactForm.phone, F.contact)
async def get_phone_contact(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    if not phone.startswith("+"):
        phone = f"+{phone}"

    await state.update_data(phone=phone)
    data = await state.get_data()

    msg = (
        f"📥 Yangi bog'lanish so'rovi:\n\n"
        f"👤 Ismi: {data['name']}\n"
        f"📞 Telefon: {data['phone']}\n"
        f"🇺🇿 Telegram: @{message.from_user.username or 'yo‘q'}\n"
        f"🆔 Telegram ID: {message.from_user.id}"
    )

    for i in ADMIN_ID:
        await bot.send_message(chat_id=i, text=msg)


@boglanish_router.message(ContactForm.phone)
async def get_phone_text(message: Message, state: FSMContext):
    text = message.text.strip()

    if len(text) == 13 and text.startswith('+998') and text[1:].isdigit():
        await state.update_data(phone=text)
        data = await state.get_data()
        await message.answer("✅ So'rovingiz yuborildi", reply_markup=main_menu())

        msg = (
            f"📥 Yangi bog'lanish so'rovi:\n\n"
            f"👤 Ismi: {data['name']}\n"
            f"📞 Telefon: {data['phone']}\n"
            f"🇺🇿 Telegram: @{message.from_user.username or 'None'}\n"
            f"🆔 Telegram ID: {message.from_user.id}"
        )

        for i in ADMIN_ID:
            print(i)
            await bot.send_message(chat_id=i, text=msg)
        

    else:
        await message.answer("❌ Telefon raqami noto‘g‘ri formatda. Qayta kiriting (masalan: +998901234567):")
