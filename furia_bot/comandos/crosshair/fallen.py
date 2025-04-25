from telegram import Update
from telegram.ext import ContextTypes

async def fallen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🎯 *Mira do Fallen:*\n\n"
        "`cl_crosshairsize 3`\n"
        "`cl_crosshairthickness 1`\n"
        "`cl_crosshaircolor 5`\n"
        "`cl_crosshairdot 0`\n"
        "`cl_crosshairgap -2`\n"
        "`cl_crosshair_drawoutline 1`\n"
        "`cl_crosshair_outlinethickness 1`"
    )
    await update.message.reply_text(texto, parse_mode="Markdown")