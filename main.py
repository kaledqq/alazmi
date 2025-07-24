import telebot
import requests

# التوكن مضاف هنا مباشرة
TOKEN = "7670193260:AAETwqRN6dWiWfT3wdA7Ht1Z4m9pDbGtUYQ"
bot = telebot.TeleBot(TOKEN)

user_states = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, "أرسل الرابط الآن لتحميل الفيديو.")
    user_states[user_id] = "awaiting_link"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    if user_states.get(user_id) == "awaiting_link":
        url = message.text.strip()
        bot.send_message(message.chat.id, f"جاري التحميل من الرابط: {url}")
        # هنا مكان تحميل الفيديو وإرساله
        bot.send_message(message.chat.id, "✅ تم التحميل (وهمياً).")
        user_states[user_id] = None
    else:
        bot.send_message(message.chat.id, "اكتب /start للبدء.")

bot.polling()
