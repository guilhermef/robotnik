#!/usr/bin/python
# -*- coding: utf-8 -*-


import tornado.web
from tornado.httpclient import AsyncHTTPClient
from tornado.web import url
from robotnik.handlers.egg import EggHandler


def configure_app(self, config=None, log_level='INFO', debug=False, main_loop=None):
    self.config = config
    self.main_loop = main_loop

    handlers = [
        url(r'/', EggHandler, name="egg_handler"),
    ]

    options = {}

    self.project_keys = {}

    if debug:
        options['debug'] = True
        config.NUMBER_OF_FORKS = 1

    AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    self.http_client = AsyncHTTPClient()

    return handlers, options


class RobotnikApp(tornado.web.Application):

    def __init__(self, config=None, log_level='INFO', debug=False, main_loop=None):
        handlers, options = configure_app(self, config, log_level, debug, main_loop)
        super(RobotnikApp, self).__init__(handlers, **options)
