from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(BOT_TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Hello from bot!")
