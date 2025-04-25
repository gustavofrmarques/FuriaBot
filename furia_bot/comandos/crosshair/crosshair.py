from telegram import Update
from telegram.ext import ContextTypes

async def crosshair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🎯 *Configurações de Mira dos Jogadores da FURIA:*\n\n"
        "🔫 /fallen\n"
        "🔫 /yuurih\n"
        "🔫 /yekindar\n"
        "🔫 /kscerato\n"
        "🔫 /molodoy"
    )
    await update.message.reply_text(texto, parse_mode="Markdown")
