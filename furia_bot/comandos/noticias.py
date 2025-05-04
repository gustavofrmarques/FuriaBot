import json
import os
from telegram import Update
from telegram.ext import ContextTypes

async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Caminho absoluto baseado na localização deste arquivo
        caminho_arquivo = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),  # /furia_bot/comandos
            "..",  # sobe para /furia_bot
            "dados",
            "noticias.json"
        )
        caminho_arquivo = os.path.abspath(caminho_arquivo)

        with open(caminho_arquivo, encoding="utf-8") as f:
            dados = json.load(f)

        texto = "📰 *Últimas notícias da FURIA:*\n\n"
        for noticia in dados:
            texto += f"📌 *{noticia['titulo']}*\n_{noticia['resumo']}_\n🔗 {noticia['link']}\n\n"

        await update.message.reply_text(texto, parse_mode="Markdown")

    except Exception as e:
        await update.message.reply_text("⚠️ Erro ao carregar as notícias.")
        print(f"Erro ao abrir arquivo: {e}")
