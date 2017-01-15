import hashlib
from models.auth import salt

def password_hash(password):
    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return password_hash

def auth_login(fn):
    def _(self, *args, **kwargs):

        if self.current_user:
            return fn(self, *args, **kwargs)
        else:
            self.finish_json(errcode=3000, errmsg="need login")
    return _

