import os
import telebot
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@hwa171"

bot = telebot.TeleBot(TOKEN)

user_states = {}

# التحقق من الاشتراك
def is_user_subscribed(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ['member', 'creator', 'administrator']
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if is_user_subscribed(user_id):
        bot.send_message(message.chat.id, "أرسل الرابط الآن لتحميل الفيديو.")
        user_states[user_id] = "awaiting_link"
    else:
        bot.send_message(message.chat.id, f"يرجى الاشتراك في القناة أولاً: {CHANNEL_USERNAME}")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    if user_states.get(user_id) == "awaiting_link":
        url = message.text.strip()
        bot.send_message(message.chat.id, f"جاري التحميل من الرابط: {url}")
        # هنا مكان تحميل الفيديو وإرساله
        # تقدر تضيف yt_dlp وتحط الكود
        # الآن مجرد رد وهمي
        bot.send_message(message.chat.id, "تم التحميل (وهمياً).")
        user_states[user_id] = None
    else:
        bot.send_message(message.chat.id, "اكتب /start للبدء.")

bot.polling()
