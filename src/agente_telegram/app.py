"""Aplicação FastAPI com endpoint de webhook para o Telegram."""

from fastapi import FastAPI, Request, Header, HTTPException
from telebot.types import Update

from agente_telegram.bot import bot
from agente_telegram.config.settings import settings


app = FastAPI()


@app.post("/webhook")
async def webhook(request: Request, x_telegram_secret: str | Header(default = None)):
    """Recebe updates do Telegram via webhook e os processa no bot.

    Args:
        request: Requisição HTTP contendo o payload JSON do Telegram.

    Returns:
        Dicionário com status de confirmação.
    """
    if x_telegram_secret != settings.secret_token.get_secret_value():
        raise HTTPException(status_code=401, detail="Unauthorized")
        
    json_string = await request.json()

    update = Update.de_json(json_string)

    bot.process_new_updates([update])

    return {"status": "ok"}
