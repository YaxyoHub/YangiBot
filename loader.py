import os
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from database.sql import get_admin


from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("API_TOKEN")
bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# raw_admin_ids = os.getenv("ADMIN_ID")
# ADMIN_ID = [int(i) for i in raw_admin_ids.split(",")]

NEWS = get_admin()
# print(ADMIN_ID)
# print(type(ADMIN_ID))

ADMIN_ID = []
for i in NEWS:
    ADMIN_ID.append(i[0])

print(ADMIN_ID)

dp = Dispatcher()

from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

class IsBotAdminFilter(BaseFilter):
    def __init__(self, admin_ids: list[int]):
        self.admin_ids = admin_ids

    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.from_user.id in self.admin_ids
