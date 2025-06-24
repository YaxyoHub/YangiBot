from aiogram import Router, F
from aiogram.types import CallbackQuery


from buttons.menu_buttons import xizmatlar_button_ru

from handlers.xizmatlar_routers.crm_handler_ru import crm_router_ru
from handlers.xizmatlar_routers.centr_handler_ru import centr_router_ru
from handlers.xizmatlar_routers.biznes_handler_ru import biznes_router_ru
from handlers.xizmatlar_routers.marketing_handler_ru import marketing_router_ru
from handlers.xizmatlar_routers.ai_handler_ru import ai_router_ru


xizmatlar_router_ru = Router()

@xizmatlar_router_ru.callback_query(F.data == "xizmatlar_ru")
async def xizmatlar_cmd(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("📋 Список услуг:", reply_markup=xizmatlar_button_ru)


xizmatlar_router_ru.include_router(crm_router_ru)
xizmatlar_router_ru.include_router(centr_router_ru)
xizmatlar_router_ru.include_router(biznes_router_ru)
xizmatlar_router_ru.include_router(marketing_router_ru)
xizmatlar_router_ru.include_router(ai_router_ru)