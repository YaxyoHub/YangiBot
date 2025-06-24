from aiogram import Router, F
from aiogram.types import CallbackQuery


from buttons.menu_buttons import xizmatlar_button

from handlers.xizmatlar_routers.crm_handler import crm_router
from handlers.xizmatlar_routers.centr_handler import centr_router
from handlers.xizmatlar_routers.biznes_handler import biznes_router
from handlers.xizmatlar_routers.marketing_handler import marketing_router
from handlers.xizmatlar_routers.ai_handler import ai_router


xizmatlar_router = Router()

@xizmatlar_router.callback_query(F.data == "xizmatlar")
async def xizmatlar_cmd(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("📋 Xizmatlar ro'yxati:", reply_markup=xizmatlar_button)


xizmatlar_router.include_router(crm_router)
xizmatlar_router.include_router(centr_router)
xizmatlar_router.include_router(biznes_router)
xizmatlar_router.include_router(marketing_router)
xizmatlar_router.include_router(ai_router)