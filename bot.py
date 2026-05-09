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
        [InlineKeyboardButton("☑️ Open Demat Account", callback_data='demat')],
        [InlineKeyboardButton("💳 Apply Credit Card", callback_data='card')],
        [InlineKeyboardButton("💰 Personal Loan", callback_data='loan')],
        [InlineKeyboardButton("👥 Become Agent", callback_data='agent')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome To Multi7Hub\n\n"
        "✅ Financial Services\n"
        "⚡ Instant Process\n"
        "💎 Trusted Platform\n\n"
        "Choose Your Service Below 👇",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == 'demat':
       if query.data == 'demat':
    await query.edit_message_text(
        "📈 Open 5paisa Demat Account\n\n"
        "✅ Free Demat & Trading Account\n"
        "✅ Flat ₹20 Brokerage\n"
        "✅ Stocks, IPO, Mutual Funds & More\n"
        "✅ Trusted By Millions Of Users\n\n"
        "👉 Sign Up Here:\n"
        "https://www.5paisa.com/demat-account?ReferralCode=55356194&ReturnUrl=invest-open-account"
    )

    elif query.data == 'card':
        await query.edit_message_text(
            "💳 Apply Credit Card\n\n"
            "✅ Instant Process\n"
            "✅ High Approval Chance\n\n"
            "Send Your Name & Mobile Number."
        )

    elif query.data == 'loan':
        await query.edit_message_text(
            "💰 Personal Loan\n\n"
            "✅ Quick Loan Approval\n"
            "✅ Trusted Finance Partners\n\n"
            "Send Your Name & Mobile Number."
        )

    elif query.data == 'agent':
        await query.edit_message_text(
            "👥 Become Agent\n\n"
            "💸 Earn Commission On Every Referral\n"
            "📱 Work From Mobile\n\n"
            "Send Your Name & Mobile Number."
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
