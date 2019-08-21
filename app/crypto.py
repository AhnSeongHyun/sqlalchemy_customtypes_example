from base64 import b64decode, b64encode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

DEFAULT_CHARSET = "utf-8"
DEFAULT_IV = bytes(AES.block_size)


def decrypt(enc):
    return AES256(key='0' * 32).decrypt_b64(enc)


def encrypt(raw):
    return AES256(key='0' * 32).encrypt_b64(raw)


class AES256:
    def __init__(self, key: str, initial_vector: bytes = DEFAULT_IV):
        self.key = key.encode(DEFAULT_CHARSET)
        self.initial_vector = initial_vector

    def create_cipher(self):
        return AES.new(self.key, AES.MODE_CBC, self.initial_vector)

    def encrypt_b64(self, value: str) -> str:
        cipher = self.create_cipher()
        value = pad(value.encode(DEFAULT_CHARSET), AES.block_size)
        return b64encode(cipher.encrypt(value)).decode(DEFAULT_CHARSET)

    def decrypt_b64(self, value: str) -> str:
        cipher = self.create_cipher()
        value = b64decode(value.encode(DEFAULT_CHARSET))
        return unpad(cipher.decrypt(value), AES.block_size).decode(
            DEFAULT_CHARSET
        )
