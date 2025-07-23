import zipfile
import os

# Define the file names and content
files_content = {
    "main.py": """
from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(BOT_TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Hello from bot!")
""",
    "requirements.txt": """
python-telegram-bot==13.15
python-dotenv
""",
    "config.env": """
BOT_TOKEN=7670193260:AAETwqRN6dWiWfT3wdA7Ht1Z4m9pDbGtUYQ
CHAT_ID=your_chat_id_here
"""
}

# Create a directory to store the files before zipping
os.makedirs('bot_files', exist_ok=True)

# Save content to corresponding files
for filename, content in files_content.items():
    with open(f"bot_files/{filename}", 'w') as f:
        f.write(content)

# Creating a zip file from the files
zip_filename = "bot_files.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, dirs, files in os.walk('bot_files'):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=file)

print(f"Created ZIP file: {zip_filename}")
