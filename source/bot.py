import telebot
import logging
from source.config import TOKEN, CHAT
from source.variables import *


def initial_bot(use_logging=True, level_name='DEBUG'):
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def start_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, start_mess)

    @bot.message_handler(commands=['help'])
    def help_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, help_mess)

    @bot.message_handler(func=lambda message: True)
    def forward_handler(message: telebot.types.Message):
        print(message)
        bot.forward_message(CHAT, message.chat.id, message.message_id)

    if use_logging:
        logger = telebot.logger
        telebot.logger.setLevel(logging.getLevelName(level_name))
    return bot
