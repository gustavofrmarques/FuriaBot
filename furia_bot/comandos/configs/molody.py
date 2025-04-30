from telegram import Update
from telegram.ext import ContextTypes

async def molodoy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🎯 Configurações do Molodoy: \n\n"
        "DPI: 400\n"
        "Sensibilidade: 2.0\n"
        "Resolução: 1280x960\n"
        "Crosshair code:\n" 
        "`CSGO-p5e7d-GARJ3-hNu3u-rM5JO-MUopQ`\n"
    )
    await update.message.reply_text(texto, parse_mode="Markdown")