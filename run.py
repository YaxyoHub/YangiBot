import asyncio

from loader import dp, bot, IsBotAdminFilter, ADMIN_ID


from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from handlers.other_handlers.xizmatlar_handler import xizmatlar_router
from handlers.other_handlers.xizmatlar_handler_ru import xizmatlar_router_ru

from handlers.other_handlers.info_back_handler import info_back_router
from handlers.other_handlers.info_back_handler_ru import info_back_router_ru

from handlers.other_handlers.boglanish_handler import boglanish_router
from handlers.other_handlers.boglanish_ru import boglanish_router_ru

from handlers.other_handlers.reklama_handler import reklama_router

from handlers.other_handlers.users_handler import router

from buttons.menu_buttons import main_menu, main_menu_ru, admin_menu, til_menu
from database.sql import add_user



@dp.message(CommandStart())
async def cmd_start(message: Message):
    add_user(message.from_user.first_name, message.from_user.id)
    await message.answer("Til tanlang /// Выберите язык",
                         reply_markup=til_menu
    )

@dp.message(F.text == "🇺🇿 O'zbek tili")
async def uz_cmd(message: Message):
    await message.answer("🏢 Kompaniya botiga xush kelibsiz 😊\n"
                        "Kompaniyamiz raqamli avtomatlashtirish xizmatini taklif qiladi", reply_markup=main_menu())
    
@dp.message(F.text == "🇷🇺 Русский язык")
async def uz_cmd(message: Message):
    await message.answer("🏢 Добро пожаловать в бот компании 😊\n"
                        "Наша компания предлагает услуги цифровой автоматизации", reply_markup=main_menu_ru())
    


@dp.message(Command('admin'), IsBotAdminFilter(ADMIN_ID))
async def admin_panel(msg: Message):
    await msg.answer("Salom Admin", reply_markup=admin_menu)

"""Routerlar"""
dp.include_router(xizmatlar_router)
dp.include_router(xizmatlar_router_ru)
dp.include_router(info_back_router)
dp.include_router(info_back_router_ru)
dp.include_router(boglanish_router)
dp.include_router(boglanish_router_ru)
dp.include_router(reklama_router)
dp.include_router(router)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot is running...")
    asyncio.run(main())