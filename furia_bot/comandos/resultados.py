from telegram import Update
from telegram.ext import ContextTypes

async def resultados(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "📊 Resultados recentes da FURIA:\n\n"
        "🆚 FURIA 2 x 1 G2 (Inferno 16-10, Mirage 12-16, Nuke 16-13)\n"
        "🆚 FURIA 0 x 2 NAVI (Ancient 11-16, Overpass 9-16)\n"
        "🆚 FURIA 2 x 0 BIG (Vertigo 16-9, Mirage 16-8)"
    )
    await update.message.reply_text(texto)
