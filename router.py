# -*- coding: utf-8 -*-

from views.api.user import UserHandler, UsersHandler, UserInfoHandler
from views.api.store import UploadHandler
from views.api.post import  PostHandler
from views.api.auth import RegisterHandler, AuthHandler
from views.api.comment import CommentHandler

handlers = [
    (r"/api/user/(?P<id>\d+)/?", UserHandler),
    (r"/api/user/?", UserHandler),
    (r"/api/users/?", UsersHandler),
    (r"/api/user/(?P<username>\S+)/info/?", UserInfoHandler),
    (r"/api/store/upload_token/?", UploadHandler),
    (r"/api/post/?", PostHandler),
    (r"/api/register/?", RegisterHandler),
    (r"/api/auth/?", AuthHandler),
    (r"/api/post/(?P<post_id>\d+)/comment/?", CommentHandler),
    (r"/api/post/(?P<post_id>\d+)/comment/(?P<comment_id>\d+)/?", CommentHandler),
]
