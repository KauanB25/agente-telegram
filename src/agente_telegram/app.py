from fastapi import FastAPI, Request
from telebot.types import Update

from agente_telegram.bot import bot


app = FastAPI()


@app.post("/webhook")
async def webhook(request: Request):
    json_string = await request.json()

    update = Update.de_json(json_string)

    bot.process_new_updates([update])

    return {"status": "ok"}
