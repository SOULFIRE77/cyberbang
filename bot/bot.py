
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.reply("Привет! Я бот Cyberbang. Скоро ты получишь NFT.")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)
