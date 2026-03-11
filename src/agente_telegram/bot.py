import logging

import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

from agente_telegram.config.settings import settings
from agente_telegram.service.user_telegram import UserTelegram


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

    user_telegram = UserTelegram()

    full_name = message.from_user.full_name

    id_telegram = message.from_user.id

    try:
        user_telegram.consulta_existencia_usuario(id_telegram)

    except ValueError:
        logging.error(f'Usuário {id_telegram} não encontrado')

        logging.info("Iniciando o cadastro do usuário")

        confirmacao = user_telegram.insert_new_user(id_telegram, full_name)

        if confirmacao:
            logging.info("Cadastro realizado com sucesso")
        else:
            logging.error("Erro ao cadastrar o usuário")


@bot.message_handler(content_types=['contact'])
def handle_contact(message: Message):
    if message.contact is not None:
        phone = message.contact.phone_number

        id_telegram = message.from_user.id

        user_telegram = UserTelegram()

        confirmacao = user_telegram.update_user_phone(id_telegram, phone)

        if confirmacao:
            logging.info("Atualização realizada com sucesso")
        else:
            logging.error("Erro ao atualizar o usuário")


@bot.message_handler(func=lambda msg: True)
def echo(message: Message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
