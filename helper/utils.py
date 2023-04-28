import hashlib


def create_pbkdf2(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 1000, 16).hex()
