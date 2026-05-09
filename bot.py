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
    [InlineKeyboardButton("📈 Open Demat Account", callback_data='demat')],
    [InlineKeyboardButton("💳 Apply Credit Card", callback_data='card')],
    [InlineKeyboardButton("💰 Personal Loan", callback_data='loan')],
    [InlineKeyboardButton("👥 Become Agent", callback_data='agent')],
]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
    """👋 Welcome To Multi7Hub

🔥 Premium Subscriptions
⚡ Instant Delivery
💎 Trusted Service

Choose Your Product Below 👇""",
    reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()
    if query.data == 'demat':
    await query.edit_message_text(
        "📈 Open Demat Account\n\n✅ Earn From Stock Market\n💰 Zero Account Opening\n📲 Send Your Name & Mobile Number."
    )

elif query.data == 'card':
    await query.edit_message_text(
        "💳 Credit Card Apply\n\n✅ Instant Process\n💰 High Limit Cards\n📲 Send Your Name & Mobile Number."
    )

elif query.data == 'loan':
    await query.edit_message_text(
        "💰 Personal Loan\n\n✅ Fast Approval\n🏦 Trusted Finance Partners\n📲 Send Your Name & Mobile Number."
    )

elif query.data == 'agent':
    await query.edit_message_text(
        "👥 Become Agent\n\n💸 Earn Commission On Every Referral\n📈 Work From Mobile\n📲 Send Your Name To Join."
    )
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot Running...")

app.run_polling()
