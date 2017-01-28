# -*- coding: utf-8 -*-


import sys
import os

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver

from tornado.platform.asyncio import AsyncIOMainLoop
import asyncio

from tornado.options import define, options

from router import handlers


define("port", default=9501, help="run on the given port", type=int)


class Application(tornado.web.Application):

    def __init__(self):

        setting = dict(
            cookie_secret="123",
            autoreload=True,
            gzip=True,
            debug=True,
            # login_url='/login/',
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )

        tornado.web.Application.__init__(self, handlers, ** setting)


def main():
    tornado.options.parse_command_line()
    # http_server = tornado.httpserver.HTTPServer(Application())
    # http_server.listen(options.port, address="127.0.0.1")
    # tornado.ioloop.IOLoop.instance().start()
    AsyncIOMainLoop().install()
    loop = asyncio.get_event_loop()
    app = Application()
    app.listen(options.port)
    loop.run_forever()


if __name__ == "__main__":
    main()
