# -*- coding: utf-8 -*-

from views.api.user import UserHandler

handlers = [
    (r"/api/user/(?P<id>\d+)/?", UserHandler),
    (r"/api/user/?", UserHandler),
        ]
