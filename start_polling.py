from core import dispatcher
from aiogram import executor
import importlib

importlib.import_module('handlers.user_data_handler')
importlib.import_module('handlers.message_handler')

if __name__ == '__main__':
    executor.start_polling(dispatcher)