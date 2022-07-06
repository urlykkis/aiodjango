import os
import django
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adminbot.settings')
#django.setup()

BOT_TOKEN = ""
bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
loop = asyncio.get_event_loop()
