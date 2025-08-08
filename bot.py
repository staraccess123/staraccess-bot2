from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8084310003:AAHc8DOzHID7qat_GySraKm-E8pd1e_OSCk"
GROUP_LINK = "https://t.me/+mUplWOzJ10c2Mzcx"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\nTo access the premium content, click below to make payment.\n\nAfter payment, you’ll be redirected back here to receive your access link.\n\n🔗 https://whop.com/backstage-vault-x/starfanshub-36/"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("For access, use the link above. Questions? Just reply here.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()