import logging

import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

from agente_telegram.config.settings import settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

bot = telebot.TeleBot(settings.token_telegram.get_secret_value())


@bot.message_handler(commands=['start', 'hello'])
def welcome(message: Message):
    markup = ReplyKeyboardMarkup(
        one_time_keyboard=True,
        resize_keyboard=True
        )

    botao_contato = KeyboardButton(
        "Você aceita compartilhar o seu telefone?",
        request_contact=True)

    markup.add(botao_contato)

    bot.send_message(
        message.chat.id,
        "Olá, para continuar faça a confirmação abaixo:",
        reply_markup=markup
    )


@bot.message_handler(content_types=['contact'])
def handle_contact(message: Message):
    if message.contact is not None:
        phone = message.contact.phone_number

        first_name = message.from_user.first_name

        logging.info(f'Contado recebido: {first_name} - {phone}')


@bot.message_handler(func=lambda msg: True)
def echo(message: Message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
