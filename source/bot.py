import telebot
import logging
from source.config import TOKEN, CHAT
from source.log import log
from source.variables import *


def initial_bot(use_logging=True, level_name='DEBUG'):
    bot = telebot.TeleBot(TOKEN)
    logger = log('bot', 'bot.log')

    @bot.message_handler(commands=['start'])
    def start_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, start_mess)
        logger.debug(f"It's start handler. Message from {message.from_user.id}")

    @bot.message_handler(commands=['help'])
    def help_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, help_mess)
        logger.debug(f"It's help handler. Message from {message.from_user.id}")

    @bot.message_handler(func=lambda message: True)
    def forward_handler(message: telebot.types.Message):
        logger.debug(f"It's forward handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                bot.send_message(message.reply_to_message.forward_from.id, message.text)
                logger.debug(f"In CHAT. Info: {message}")
            else:
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                logger.debug(f"Message from a user. Info: {message}")
        except Exception as error:
            logger.debug(f"Exception in forward handler. Info: {error}")

    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))
    return bot
