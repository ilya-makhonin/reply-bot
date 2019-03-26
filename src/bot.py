import telebot
import logging
from config import TOKEN, CHAT, admins_id
from log import log
from variables import *


def initial_bot(use_logging=True, level_name='DEBUG'):
    bot = telebot.TeleBot(TOKEN)
    logger = log('bot', 'bot.log', 'INFO')
    working = {'disable': False}
    hidden_forward = {}

    @bot.message_handler(commands=['start'])
    def start_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, start_mess)
        logger.info(f"It's start handler. Message from {message.from_user.id}")

    @bot.message_handler(commands=['help'])
    def help_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, help_mess)
        logger.info(f"It's help handler. Message from {message.from_user.id}")

    @bot.message_handler(commands=['disable'])
    def toggle_handler(message: telebot.types.Message):
        logger.info(f"It's disable handler. Message from {message.from_user.id}. Hidden_forward is {hidden_forward}")
        if message.chat.id in admins_id:
            hidden_forward.clear()
            working['disable'] = not working['disable']
            if working.get('disable'):
                bot.send_message(message.from_user.id, disable_mess)
            else:
                bot.send_message(message.from_user.id, enable_mess)
            logger.info(f"Disable mode is {working['disable']}")

    @bot.message_handler(func=lambda message: working.get('disable'))
    def check_working(message: telebot.types.Message):
        if message.chat.id == int(CHAT):
            bot.send_message(CHAT, none_mess)
            logger.info(f"It's check_working handler. Message from CHAT")
        else:
            bot.send_message(message.from_user.id, none_mess)
            logger.info(f"It's check_working handler. Message from {message.from_user.id}")

    # ***********************************************************************************************************
    @bot.message_handler(content_types=['text'])
    def text_handler(message: telebot.types.Message):
        logger.info(f"It's text handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                if message.reply_to_message.forward_from is None:
                    bot.send_message(hidden_forward.get(message.reply_to_message.date), message.text)
                else:
                    bot.send_message(message.reply_to_message.forward_from.id, message.text)
                    hidden_forward.pop(message.reply_to_message.date)
                logger.info(f"In CHAT (text_handler). Hidden_forward is {hidden_forward}. Info: {message}")
            else:
                hidden_forward[message.date] = message.from_user.id
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                bot.reply_to(message, success_mess)
                logger.info(f"Text handler. Message from a user. Hidden_forward is {hidden_forward} Info: {message}")
        except Exception as error:
            logger.info(f"Exception in text handler. Info: {error.with_traceback(None)}")

    @bot.message_handler(content_types=['sticker'])
    def sticker_handler(message: telebot.types.Message):
        logger.info(f"It's sticker handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                if message.reply_to_message.forward_from is None:
                    bot.send_sticker(hidden_forward.get(message.reply_to_message.date), message.sticker.file_id)
                else:
                    bot.send_sticker(message.reply_to_message.forward_from.id, message.sticker.file_id)
                    hidden_forward.pop(message.reply_to_message.date)
                logger.info(f"In CHAT (sticker_handler). Hidden_forward is {hidden_forward}. Info: {message}")
            else:
                hidden_forward[message.date] = message.from_user.id
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                bot.reply_to(message, success_mess)
                logger.info(f"Sticker handler. Message from a user. Hidden_forward is {hidden_forward}. Info: {message}")
        except Exception as error:
            logger.info(f"Exception in sticker handler. Info: {error.with_traceback(None)}")

    @bot.message_handler(content_types=['photo'])
    def images_handler(message: telebot.types.Message):
        logger.info(f"It's images handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                if message.reply_to_message.forward_from is None:
                    bot.send_photo(hidden_forward.get(message.reply_to_message.date), message.photo[-1].file_id)
                else:
                    bot.send_photo(message.reply_to_message.forward_from.id, message.photo[-1].file_id)
                    hidden_forward.pop(message.reply_to_message.date)
                logger.info(f"In CHAT (images_handler). Hidden_forward is {hidden_forward}. Info: {message}")
            else:
                hidden_forward[message.date] = message.from_user.id
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                bot.reply_to(message, success_mess)
                logger.info(f"Image handler. Message from a user. Hidden_forward is {hidden_forward}. Info: {message}")
        except Exception as error:
            logger.info(f"Exception in image handler. Info: {error.with_traceback(None)}")

    @bot.message_handler(content_types=['document'])
    def file_handler(message: telebot.types.Message):
        logger.info(f"It's file handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                if message.reply_to_message.forward_from is None:
                    bot.send_document(hidden_forward.get(message.reply_to_message.date), message.document.file_id)
                else:
                    bot.send_document(message.reply_to_message.forward_from.id, message.document.file_id)
                    hidden_forward.pop(message.reply_to_message.date)
                logger.info(f"In CHAT (file_handler). Hidden_forward is {hidden_forward}. Info: {message}")
            else:
                hidden_forward[message.date] = message.from_user.id
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                bot.reply_to(message, success_mess)
                logger.info(f"File handler. Message from a user. Hidden_forward is {hidden_forward}. Info: {message}")
        except Exception as error:
            logger.info(f"Exception in file handler. Info: {error.with_traceback(None)}")

    @bot.message_handler(content_types=['audio'])
    def audio_handler(message: telebot.types.Message):
        logger.info(f"It's audio handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                if message.reply_to_message.forward_from is None:
                    bot.send_audio(hidden_forward.get(message.reply_to_message.date), message.audio.file_id)
                else:
                    bot.send_audio(message.reply_to_message.forward_from.id, message.audio.file_id)
                    hidden_forward.pop(message.reply_to_message.date)
                logger.info(f"In CHAT (audio_handler). Hidden_forward is {hidden_forward}. Info: {message}")
            else:
                hidden_forward[message.date] = message.from_user.id
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                bot.send_message(message.from_user.id, success_mess)
                logger.info(f"Audio handler. Message from a user. Hidden_forward is {hidden_forward}. Info: {message}")
        except Exception as error:
            logger.info(f"Exception in audio handler. Info: {error.with_traceback(None)}")

    @bot.message_handler(content_types=['voice'])
    def voice_handler(message: telebot.types.Message):
        logger.info(f"It's voice handler. Message from {message.from_user.id}")
        try:
            if message.chat.id == int(CHAT):
                if message.reply_to_message.forward_from is None:
                    bot.send_voice(hidden_forward.get(message.reply_to_message.date), message.voice.file_id)
                else:
                    bot.send_voice(message.reply_to_message.forward_from.id, message.voice.file_id)
                    hidden_forward.pop(message.reply_to_message.date)
                logger.info(f"In CHAT (voice_handler). Hidden_forward is {hidden_forward}. Info: {message}")
            else:
                hidden_forward[message.date] = message.from_user.id
                bot.forward_message(CHAT, message.chat.id, message.message_id)
                bot.send_message(message.from_user.id, success_mess)
                logger.info(f"Voice handler. Message from a user. Hidden_forward is {hidden_forward}. Info: {message}")
        except Exception as error:
            logger.info(f"Exception in voice handler. Info: {error.with_traceback(None)}")

    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))
    return bot
