#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy
import logging
import telebot
import time

TOKEN = '782146814:AAGJ-8p8kvOXdurucHQRod1sfZs3JbOVa_4'
WEB_HOOK_HOST = '194.32.79.65'
WEB_HOOK_PORT = 88
WEB_HOOK_LISTEN = '0.0.0.0'
WEB_HOOK_SSL_CERT = './public_cert.pem'
WEB_HOOK_SSL_PRIV = './private_key.pem'
WEB_HOOK_URL_BASE = "https://%s:%s" % (WEB_HOOK_HOST, WEB_HOOK_PORT)
WEB_HOOK_URL_PATH = "/%s/" % (TOKEN, )

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TOKEN)


class WebHookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
           'content-type' in cherrypy.request.headers and \
           cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, I am EchoBot.\nI am here to echo your kind words back to you.")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


def main():
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=WEB_HOOK_URL_BASE + WEB_HOOK_URL_PATH, certificate=open(WEB_HOOK_SSL_CERT, 'r'))
    access_log = cherrypy.log.access_log
    for handler in tuple(access_log.handlers):
        access_log.removeHandler(handler)

    cherrypy.config.update({
        'server.socket_host': WEB_HOOK_LISTEN,
        'server.socket_port': WEB_HOOK_PORT,
        'server.ssl_module': 'builtin',
        'server.ssl_certificate': WEB_HOOK_SSL_CERT,
        'server.ssl_private_key': WEB_HOOK_SSL_PRIV
    })

    cherrypy.quickstart(WebHookServer(), WEB_HOOK_URL_PATH, {'/': {}})


if __name__ == '__main__':
    main()
