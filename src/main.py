#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cherrypy
import telebot
import time
from log import log
from config import *
from bot import initial_bot


WEB_HOOK_URL_BASE = "https://%s:%s" % (WEB_HOOK_HOST, WEB_HOOK_PORT)
WEB_HOOK_URL_PATH = "/%s/" % (TOKEN, )

BOT = initial_bot(use_logging=True, level_name='INFO')
server_logger = log('server', 'server.log')


class WebHookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
           'content-type' in cherrypy.request.headers and \
           cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            BOT.process_new_updates([update])
            server_logger.debug(update)
            return ''
        else:
            server_logger.info(f"Server error! Error status 403")
            raise cherrypy.HTTPError(403)


def main():
    server_logger.info("Start main function")
    BOT.remove_webhook()
    time.sleep(1)
    BOT.set_webhook(url=WEB_HOOK_URL_BASE + WEB_HOOK_URL_PATH, certificate=open(WEB_HOOK_SSL_CERT, 'r'))
    server_logger.info("Web hook has been set success")
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
    server_logger.info("Server is started success")
    cherrypy.quickstart(WebHookServer(), WEB_HOOK_URL_PATH, {'/': {}})


if __name__ == '__main__':
    server_logger.info("Bot is starting")
    try:
        main()
    except Exception as error:
        server_logger.info(f"Error in main function. Info: {error.with_traceback(None)}")
