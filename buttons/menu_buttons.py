from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# 🔙 Ortga tugmasi
def ortga_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Ortga", callback_data="go_back")]
    ])
def ortga_button_ru():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="go_back_ru")]
    ])


# 📞 Bog‘lanish tugmasi
def call_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📞 Biz bilan bog'lanish", callback_data="call")]
    ])
def call_button_ru():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📞 Cвязаться с нами", callback_data="call_ru")]
    ])

def back_call_ru():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_ru"), InlineKeyboardButton(text="📞 Cвязаться с нами", callback_data="call_ru")]
    ])
def back_call():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Ortga", callback_data="back"), InlineKeyboardButton(text="📞 Biz bilan bog'lanish", callback_data="call")]
    ])

def main_menu_ru():
    builder = InlineKeyboardBuilder()
    builder.button(text="📋 Список услуг", callback_data="xizmatlar_ru")
    builder.button(text="📞 Связаться с нами", callback_data="call_ru")
    builder.button(text="ℹ️ О компании", callback_data="info_ru")
    builder.adjust(1)
    return builder.as_markup()

# 🏠 Asosiy menyu
def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="📝 Xizmatlar ro'yxati", callback_data="xizmatlar")
    builder.button(text="📞 Biz bilan bog'lanish", callback_data="call")
    builder.button(text="ℹ️ Kompaniya haqida", callback_data="info")
    builder.adjust(1)
    return builder.as_markup()


cancel_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='❌ Bekor qilish', callback_data='cancel')]
    ]
)
cancel_button_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='❌ Отмена', callback_data='cancel_ru')]
    ]
)

xizmatlar_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1️⃣ CRM tizimlari", callback_data="crm")],
        [InlineKeyboardButton(text="2️⃣ Call-Center yechimlari", callback_data="centr")],
        [InlineKeyboardButton(text="3️⃣ Biznes avtomatlashtirish", callback_data="biznes")],
        [InlineKeyboardButton(text="4️⃣ Marketing avtomatizatsiyasi", callback_data="marketing")],
        [InlineKeyboardButton(text="5️⃣ AI integratsiyasi", callback_data="AI")],
        [InlineKeyboardButton(text="⬅️ Ortga", callback_data="go_back"), InlineKeyboardButton(text="📞 Biz bilan bog'lanish", callback_data="call")]
    ]
)
xizmatlar_button_ru = InlineKeyboardMarkup(
    inline_keyboard= [ 
        [InlineKeyboardButton(text="1️⃣ CRM системы", callback_data="crm_ru")],
        [InlineKeyboardButton(text="2️⃣ Решения Call-центра", callback_data="centr_ru")],
        [InlineKeyboardButton(text="3️⃣ Автоматизация бизнеса", callback_data="biznes_ru")],
        [InlineKeyboardButton(text="4️⃣ Автоматизация маркетинга", callback_data="marketing_ru")],
        [InlineKeyboardButton(text="5️⃣ Интеграция ИИ", callback_data="AI_ru")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="go_back_ru"), InlineKeyboardButton(text="📞 Связаться с нами", callback_data="call_ru")]
])

admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📢 Reklama yuborish", callback_data="send_ad")],
        [InlineKeyboardButton(text="👀 Foydalanuvchilarni ko'rish", callback_data="see_users")]
    ]
)

til_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 O'zbek tili"), KeyboardButton(text="🇷🇺 Русский язык")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

phone_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Telefon raqam ulashish", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

phone_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Поделитесь номером телефона", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)