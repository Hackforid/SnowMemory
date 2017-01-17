# -*- coding: utf-8 -*-

from views.api.user import UserHandler, UsersHandler
from views.api.store import UploadHandler
from views.api.post import  PostHandler
from views.api.auth import RegisterHandler, AuthHandler

handlers = [
    (r"/api/user/(?P<id>\d+)/?", UserHandler),
    (r"/api/user/?", UserHandler),
    (r"/api/users/?", UsersHandler),
    (r"/api/store/upload_token/?", UploadHandler),
    (r"/api/post/?", PostHandler),
    (r"/api/register/?", RegisterHandler),
    (r"/api/auth/?", AuthHandler),
        ]
