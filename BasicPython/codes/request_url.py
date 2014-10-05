#!/usr/bin/env python
#coding:utf-8

import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="Please send email to me", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input_word):
        self.write(input_word[::-1])
    

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument("name")
        width = self.get_argument("width", 40)
        self.write(textwrap.fill(word, width))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [
            (r"/reverse/(\w+)", ReverseHandler),
            (r"/wrap/(/w+)", WrapHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
