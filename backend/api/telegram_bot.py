
import os
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("TG_BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Welcome to Cyberbang bot!")

async def start_bot():
    asyncio.create_task(dp.start_polling())
