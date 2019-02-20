#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cherrypy
import telebot
import time
from source.config import *
from source.bot import initial_bot


WEB_HOOK_URL_BASE = "https://%s:%s" % (WEB_HOOK_HOST, WEB_HOOK_PORT)
WEB_HOOK_URL_PATH = "/%s/" % (TOKEN, )

BOT = initial_bot()


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
            return ''
        else:
            raise cherrypy.HTTPError(403)


def main():
    BOT.remove_webhook()
    time.sleep(1)
    BOT.set_webhook(url=WEB_HOOK_URL_BASE + WEB_HOOK_URL_PATH, certificate=open(WEB_HOOK_SSL_CERT, 'r'))
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
