from telegram import Update
from telegram.ext import ContextTypes

async def yuurih(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🎯 Configurações do Yuurih: \n\n"
        "DPI: 400\n"
        "Sensibilidade: 2.50\n"
        "Resolução: 1980x1080\n"
        "Crosshair code:\n" 
        "`CSGO-tMcGZ-7dsrt-w7Mor-rZv2M-ey3JE`\n"
        "`CSGO-8fzkO-nCvOi-FKNjN-qoXpf-3kYbD`\n"     
    )
    await update.message.reply_text(texto, parse_mode="Markdown")