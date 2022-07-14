import asyncio
import logging
from http import client

import aiogram.utils.markdown as fmt
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.types.message import ContentType
from aiogram.utils import executor

from create_bot import dp, lilabred_bot
from handlers import client

logging.basicConfig(filename="LilaBred.log", level=logging.DEBUG)


async def on_startup(_):
    print("LilaBred bot online")


# client.register_handlers_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
