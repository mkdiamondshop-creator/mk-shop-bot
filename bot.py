from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8995347085:AAG91a2AB7jX_LFJ98MQuuJdvDgI1Nqlxk8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Welcome to MK Gaming Shop\n\n"
        "💎 MLBB Diamonds\n"
        "🔥 PUBG UC\n"
        "⚡ Fast Top-Up Service"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Running...")
app.run_polling()
