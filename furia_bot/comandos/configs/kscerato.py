from telegram import Update
from telegram.ext import ContextTypes

async def kscerato(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🎯 Configurações do KSCERATO: \n\n"
        "DPI: 400\n"
        "Sensibilidade: 4.20\n"
        "Resolução: 1280x960\n"
        "Crosshair code:\n" 
        "`CSGO-8fzkO-nCvOi-FKNjN-qoXpf-3kYbD`"
    )
    await update.message.reply_text(texto, parse_mode="Markdown")