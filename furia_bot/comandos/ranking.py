from telegram import Update
from telegram.ext import ContextTypes

async def ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🏅 RANKING da FURIA \n\n"
        "Valve Ranking: #20\n"
        "HLTV Ranking: #17\n"
    )
    await update.message.reply_text(texto)