import logging
from http import client

from aiogram.utils import executor

from create_bot import dp, lilabred_bot
from handlers import client

import asyncio

import aiogram.utils.markdown as fmt
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from aiogram.types.message import ContentType

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(filename="LilaBred.log", level=logging.DEBUG)


async def on_startup(_):
    print("LilaBred bot online")

#client.register_handlers_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
