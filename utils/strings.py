import random
import string
import hashlib

def gen_password(length):
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for i in range(length)])

def md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()
