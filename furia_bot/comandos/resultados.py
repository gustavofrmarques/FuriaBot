from telegram import Update
from telegram.ext import ContextTypes

async def resultados(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "📊 Resultados recentes da FURIA:\n\n"
        "🆚 FURIA 0 x 2 The MongolZ (Mirage 9-13, Nuke 11-13)\n"
        "🆚 FURIA 0 x 2 VirtusPro (Anubis 11-13, Dust2 8-13)\n"
        "🆚 FURIA 1 x 2 Complexity (Dust2 13-8, Train 1-13, Inferno 4-13)"
    )
    await update.message.reply_text(texto)
