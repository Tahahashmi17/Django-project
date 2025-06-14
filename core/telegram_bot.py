import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from django.conf import settings
from asgiref.sync import sync_to_async

from core.models import TelegramUser

@sync_to_async
def check_and_save_user(username, chat_id):
    if not TelegramUser.objects.filter(username=username).exists():
        TelegramUser.objects.create(username=username, chat_id=chat_id)
        return "new"
    return "exists"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username
    chat_id = update.message.chat_id

    if username is None:
        username = f"user_{chat_id}"

    status = await check_and_save_user(username, chat_id)

    if status == "new":
        await update.message.reply_text(f"Welcome, {username}! You’ve been registered.")
    else:
        await update.message.reply_text(f"Hey {username}, you're already registered.")

def run_bot():
    app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Telegram bot is running...")
    app.run_polling()

if __name__ == '__main__':
    run_bot()
