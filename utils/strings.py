import random
import string

def gen_password(length):
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for i in range(length)])
