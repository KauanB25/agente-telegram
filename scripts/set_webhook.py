import telebot
from agente_telegram.config.settings import settings

bot = telebot.TeleBot(settings.token_telegram.get_secret_value())


bot.remove_webhook()

url_webhook = settings.url_webhook

# Define o novo webhook
sucesso = bot.set_webhook(url=url_webhook, secret_token=settings.secret_token.get_secret_value())

if sucesso:
    print(f"✅ Webhook configurado com sucesso para: {url_webhook}")
else:
    print("❌ Falha ao configurar o webhook.")
