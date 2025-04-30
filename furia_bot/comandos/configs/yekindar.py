from telegram import Update
from telegram.ext import ContextTypes

async def yekindar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🎯 Configurações do Yekindar: \n\n"
        "DPI: 800\n"
        "Sensibilidade: 1.00\n"
        "Resolução: 1280x960\n"
        "Crosshair code:\n" 
        "`CSGO-QfwiU-kcYxq-2YKHq-jVOkc-abBAA`\n"
        "`CSGO-X9vtt-LwP2a-5ZqtO-LmpVX-bCSZQ`\n" 
        "`CSGO-JKyBM-UYLuG-bUyuL-uPkEJ-CuSyL`\n"
        "`CSGO-f5rTN-9ZXae-25YoE-7Bfnp-QQSFE`\n"
    )
    await update.message.reply_text(texto, parse_mode="Markdown")