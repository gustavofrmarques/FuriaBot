# 🤖 Bot da FURIA para Telegram

Este é um bot para fãs do time de CS\:GO da FURIA! Com ele, você pode acompanhar notícias, lineup, ranking, resultados, configurações de mira dos jogadores e muito mais, diretamente pelo Telegram.

## 📦 Funcionalidades

* `/start`: Inicia a conversa com o bot
* `/comandos`: Mostra os comandos disponíveis
* `/noticias`: Exibe as últimas notícias da FURIA
* `/lineup`: Mostra a lineup atual com nacionalidades e emojis
* `/resultados`: Exibe os últimos jogos e seus resultados
* `/ranking`: Informa a posição atual no ranking mundial
* `/ConfigsDaLine`: Menu com as configurações individuais dos jogadores
* `/fallen`, `/yuurih`, `/yekindar`, `/kscerato`, `/molodoy`: Mostram as configurações de mira de cada jogador

## 🚀 Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/furia-telegram-bot.git
cd furia-telegram-bot
```

2. Crie um ambiente virtual (opcional mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto e adicione o token do seu bot:

```
TELEGRAM_BOT_TOKEN=seu_token_aqui
```

5. Execute o bot:

```bash
python bot.py
```

## 🛠️ Como obter o token do bot

1. Abra o Telegram e pesquise por [@BotFather](https://t.me/BotFather)
2. Envie o comando `/newbot`
3. Dê um nome e um username (que termine com `bot`)
4. Copie o token gerado e cole no seu arquivo `.env` conforme mostrado acima

## 📁 Estrutura do Projeto

```
furia-telegram-bot/
│
├── bot.py                     # Arquivo principal do bot
├── .env                      # Token do bot (não versionado)
├── requirements.txt          # Dependências do projeto
├── dados/
│   └── noticias.json         # Notícias em formato JSON
└── comandos/
    ├── noticias.py
    ├── resultados.py
    ├── lineup.py
    ├── ranking.py
    ├── configs/
    │   ├── configs.py        # Menu de configurações
    │   ├── fallen.py
    │   ├── yuurih.py
    │   ├── yekindar.py
    │   ├── kscerato.py
    │   └── molodoy.py
```

## 🧪 Exemplo de conteúdo do `noticias.json`

```json
[
  {
    "titulo": "Entrevista com o FalleN",
    "resumo": "FalleN sobre momento difícil da FURIA",
    "link": "https://www.hltv.org/news/41491"
  },
  {
    "titulo": "Troca de LineUP",
    "resumo": "FURIA coloca Skullz no banco e traz Yekindar como substituto",
    "link": "https://www.hltv.org/news/41512"
  }
]
```

## ✅ Contribuição

Sinta-se livre para abrir issues e pull requests com melhorias ou novas ideias!


