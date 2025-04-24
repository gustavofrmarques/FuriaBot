from telegram import Update
from telegram.ext import ContextTypes

async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🚨 ÚLTIMAS NOTICIAS 🚨\n\n"
        # deverá ser atualizado com as ultimas noticias da FURIA
    )
    await update.message.reply_text(texto)