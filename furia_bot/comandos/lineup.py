from telegram import Update
from telegram.ext import ContextTypes

async def lineup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🖥️ LINE DA FURIA 🖥️\n\n"
        "🇧🇷 Fallen 🇧🇷\n"
        "🇧🇷 Yuurih 🇧🇷\n"
        "🇱🇻 Yekindar 🇱🇻\n"
        "🇧🇷 KSCERATO 🇧🇷\n"
        "🇷🇺 Molodoy 🇷🇺\n"
    )
    await update.message.reply_text(texto)