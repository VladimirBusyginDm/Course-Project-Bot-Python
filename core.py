from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import config

bot = Bot(token=config.ACCESS_TOKEN)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

