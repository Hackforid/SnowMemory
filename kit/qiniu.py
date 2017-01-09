# -*- coding: utf-8 -*-

from qiniu import Auth

access_key = 'Bt7H98BUkw91iol4ap8ZkhGtpyDDA7YKxzMK25mV'
secret_key = 'UZEgO0gINGW_7KP4LRbWZDyRsSLE9oW-ZsZorLee'

q = Auth(access_key, secret_key)
bucket_name = 'snowmemory'

def get_upload_token(file_name):
    token = q.upload_token(bucket_name, file_name, 3600)
    return token



