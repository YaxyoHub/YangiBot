from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from database.sql import get_user
from buttons.menu_buttons import admin_menu
from loader import IsBotAdminFilter, ADMIN_ID
router = Router()

# 🔘 Foydalanuvchilarni ko‘rish
@router.callback_query(F.data == "see_users", IsBotAdminFilter(ADMIN_ID))
async def list_users(callback: CallbackQuery):
    users = get_user()
    await send_users_page(callback, users, page=0)

# 🔘 Sahifa almashtirish
@router.callback_query(F.data.startswith("next_page:"))
async def next_page_handler(callback: CallbackQuery):
    page = int(callback.data.split(":")[1])
    users = get_user()
    await send_users_page(callback, users, page)
    await callback.answer()

# 🔘 Admin menyuga qaytish
@router.callback_query(F.data == "back_to_admin")
async def back_to_admin(callback: CallbackQuery):
    await callback.message.edit_text("🔙 Asosiy admin menyu", reply_markup=admin_menu)

# 📄 Foydalanuvchilarni chiqarish sahifasi
async def send_users_page(callback: CallbackQuery, users: list, page: int):
    per_page = 10
    start = page * per_page
    end = start + per_page
    sliced_users = users[start:end]

    total_users = len(users)

    if not sliced_users:
        text = "📭 Boshqa foydalanuvchi yo‘q."
    else:
        text = f"👥 Umumiy foydalanuvchilar soni: <b>{total_users} ta</b>\n\n"
        text += "\n".join([
            f"{idx + 1 + start}. ID: <code>{user_id}</code>"
            for idx, user_id in enumerate(sliced_users)
        ])

    # 🔘 Navigatsiya tugmalari
    navigation_buttons = []
    if page > 0:
        navigation_buttons.append(
            InlineKeyboardButton(text="⬅️", callback_data=f"next_page:{page - 1}")
        )
    if end < len(users):
        navigation_buttons.append(
            InlineKeyboardButton(text="➡️", callback_data=f"next_page:{page + 1}")
        )

    # 🔙 Orqaga tugmasi
    back_button = [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_admin")]

    # 🔘 Klaviatura yig‘ish
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            navigation_buttons if navigation_buttons else [],
            back_button
        ]
    )

    await callback.message.edit_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )
