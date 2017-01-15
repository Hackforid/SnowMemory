import hashlib
from models.auth import salt

def password_hash(password):
    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return password_hash
