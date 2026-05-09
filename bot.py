from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7981776122:AAEZ_xQDj6daf26otl-ckVWnFkNv2Zqe3ag"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("YouTube Premium", callback_data='yt')],
        [InlineKeyboardButton("Spotify Premium", callback_data='spotify')],
        [InlineKeyboardButton("Netflix Premium", callback_data='netflix')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome To Multi7Hub!",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == 'yt':
        await query.edit_message_text("You Selected YouTube Premium")

    elif query.data == 'spotify':
        await query.edit_message_text("You Selected Spotify Premium")

    elif query.data == 'netflix':
        await query.edit_message_text("You Selected Netflix Premium")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot Running...")

app.run_polling()
