import telebot
import logging
from source.config import TOKEN, CHAT
from source.log import log
from source.variables import *


def initial_bot(use_logging=True, level_name='DEBUG'):
    bot = telebot.TeleBot(TOKEN)
    logger = log('bot', 'bot.log', level_name)

    @bot.message_handler(commands=['start'])
    def start_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, start_mess)
        logger.debug(f"It's start handler. Message from {message.from_user.id}")

    @bot.message_handler(commands=['help'])
    def help_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, help_mess)
        logger.debug(f"It's help handler. Message from {message.from_user.id}")

    @bot.message_handler(content_types=['sticker'])
    def sticker_handler(message: telebot.types.Message):
        logger.debug(f"It's sticker handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                bot.send_sticker(message.reply_to_message.forward_from.id, message.sticker.file_id)
                logger.debug(f"In CHAT. Info: {message}")
            else:
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                logger.debug(f"Sticker handler. Message from a user. Info: {message}")
        except Exception as error:
            logger.debug(f"Exception in sticker handler. Info: {error.with_traceback(None)}")

    @bot.message_handler(content_types=['photo'])
    def images_handler(message: telebot.types.Message):
        logger.debug(f"It's images handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                bot.send_photo(message.reply_to_message.forward_from.id, message.photo.file_id)
                logger.debug(f"In CHAT. Info: {message}")
            else:
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                logger.debug(f"Image handler. Message from a user. Info: {message}")
        except Exception as error:
            logger.debug(f"Exception in image handler. Info: {error.with_traceback(None)}")

    @bot.message_handler(content_types=['document'])
    def file_handler(message: telebot.types.Message):
        logger.debug(f"It's file handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                bot.send_document(message.reply_to_message.forward_from.id, message.document.file_id)
                logger.debug(f"In CHAT. Info: {message}")
            else:
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                logger.debug(f"File handler. Message from a user. Info: {message}")
        except Exception as error:
            logger.debug(f"Exception in file handler. Info: {error.with_traceback(None)}")

    @bot.message_handler(content_types=['audio'])
    def audio_handler(message: telebot.types.Message):
        logger.debug(f"It's audio handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                bot.send_audio(message.reply_to_message.forward_from.id, message.audio.file_id)
                logger.debug(f"In CHAT. Info: {message}")
            else:
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                logger.debug(f"Audio handler. Message from a user. Info: {message}")
        except Exception as error:
            logger.debug(f"Exception in audio handler. Info: {error.with_traceback(None)}")

    @bot.message_handler(content_types=['voice'])
    def voice_handler(message: telebot.types.Message):
        logger.debug(f"It's voice handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                bot.send_voice(message.reply_to_message.forward_from.id, message.voice.file_id)
                logger.debug(f"In CHAT. Info: {message}")
            else:
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                logger.debug(f"Voice handler. Message from a user. Info: {message}")
        except Exception as error:
            logger.debug(f"Exception in voice handler. Info: {error.with_traceback(None)}")

    @bot.message_handler(func=lambda message: True)
    def text_handler(message: telebot.types.Message):
        logger.debug(f"It's text handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                bot.send_message(message.reply_to_message.forward_from.id, message.text)
                logger.debug(f"In CHAT. Info: {message}")
            else:
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                logger.debug(f"Text handler. Message from a user. Info: {message}")
        except Exception as error:
            logger.debug(f"Exception in text handler. Info: {error.with_traceback(None)}")

    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))
    return bot
