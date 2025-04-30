from telegram import Update
from telegram.ext import ContextTypes

async def fallen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🎯 Configurações do Fallen: \n\n"
        "DPI: 400\n"
        "Sensibilidade: 2.20\n"
        "Resolução: 1024x768\n"
        "Crosshair code:\n" 
        "`CSGO-EFyBb-4Ubiz-QBpBi-JDRWV-WrybE`\n"
        "`CSGO-TpORA-p9Ley-TLQ3P-HzXJY-U9z6A`\n" 
        "`CSGO-JKyBM-UYLuG-bUyuL-uPkEJ-CuSyL`"
    )
    await update.message.reply_text(texto, parse_mode="Markdown")