import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)
    DEBUG = False
    HOST = '127.0.0.1'
    PORT = 5003