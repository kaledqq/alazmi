import os
from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Client("my_bot", bot_token=BOT_TOKEN)

bot.start()
bot.send_message(chat_id=CHAT_ID, text="✅ Bot is now online.")
bot.stop()
