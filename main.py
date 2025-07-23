import os
import yt_dlp
import logging
from telegram import Update, InputFile, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# إعداد التوكن ومعرف القناة
TOKEN = "7670193260:AAETwqRN6dWiWfT3wdA7Ht1Z4m9pDbGtUYQ"
CHANNEL_ID = "@hwa171"

# إعداد نظام اللوجات
logging.basicConfig(level=logging.INFO)

# دالة التحقق من الاشتراك في القناة
async def is_user_subscribed(bot: Bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if await is_user_subscribed(context.bot, user_id):
        await update.message.reply_text("أرسل رابط الفيديو (يوتيوب - تيك توك - تويتر)...")
    else:
        await update.message.reply_text("يرجى الاشتراك في القناة أولاً: https://t.me/hwa171")

# دالة تحميل الفيديوهات
def download_video(url: str) -> str:
    ydl_opts = {
        "outtmpl": "video.%(ext)s",
        "format": "mp4",
        "noplaylist": True,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

# استجابة للروابط
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    user_id = update.effective_user.id

    if not await is_user_subscribed(context.bot, user_id):
        await update.message.reply_text("اشترك في القناة أولاً: https://t.me/hwa171")
        return

    await update.message.reply_text("جاري التحميل...")

    try:
        video_path = download_video(url)
        with open(video_path, "rb") as video:
            await update.message.reply_video(video=InputFile(video))
        os.remove(video_path)
    except Exception as e:
        await update.message.reply_text("حدث خطأ أثناء التحميل 😢")
        logging.error(f"Download error: {e}")

# تشغيل البوت
if name == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
