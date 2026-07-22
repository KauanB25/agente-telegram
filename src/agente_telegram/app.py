"""Aplicação FastAPI com endpoint de webhook para o Telegram."""

from fastapi import FastAPI, Request
from telebot.types import Update

from agente_telegram.bot import bot


app = FastAPI()


@app.post("/webhook")
async def webhook(request: Request):
    """Recebe updates do Telegram via webhook e os processa no bot.

    Args:
        request: Requisição HTTP contendo o payload JSON do Telegram.

    Returns:
        Dicionário com status de confirmação.
    """
    json_string = await request.json()

    update = Update.de_json(json_string)

    bot.process_new_updates([update])

    return {"status": "ok"}
