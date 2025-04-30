from telegram import Update
from dotenv import load_dotenv
import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from comandos.resultados import resultados
from comandos.lineup import lineup
from comandos.noticias import noticias
from comandos.ranking import ranking
from comandos.configs.configs import configsLine
from comandos.configs.fallen import fallen
from comandos.configs.yuurih import yuurih
from comandos.configs.yekindar import yekindar  
from comandos.configs.kscerato import kscerato
from comandos.configs.molody import molodoy

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salve! Eu sou o bot da FURIA! 🐆 Digite /comandos para ver o que posso fazer.")

async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🔥 Comandos disponíveis:\n"
        "/noticias - Últimas noticias da FURIA\n"
        "/lineup - Atual LineUp da FURIA\n"
        "/resultados - Jogos recentes\n"
        "/ranking - Ranking da FURIA\n"
        "/ConfigsDaLine - Configurações\n"
        "/quiz - Desafie seus conhecimentos\n"

    )
    await update.message.reply_text(texto)

app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("comandos", comandos))
app.add_handler(CommandHandler("resultados", resultados))
app.add_handler(CommandHandler("lineup", lineup)) 
app.add_handler(CommandHandler("noticias", noticias))  
app.add_handler(CommandHandler("ranking", ranking))
app.add_handler(CommandHandler("ConfigsDaline", configsLine))
app.add_handler(CommandHandler("fallen", fallen))
app.add_handler(CommandHandler("yuurih", yuurih))
app.add_handler(CommandHandler("yekindar", yekindar))
app.add_handler(CommandHandler("kscerato", kscerato))
app.add_handler(CommandHandler("molody", molodoy))


app.run_polling()
