import base64
import datetime

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256


def encrypt(key: str, source: str, encode: bool = True) -> str:
    key = key.encode("UTF-8")
    source = source.encode("UTF-8")
    key = SHA256.new(key).digest()
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding
    data = IV + encryptor.encrypt(source)
    return base64.b64encode(data).decode("latin-1") if encode else data


def decrypt(key: str, source: str, decode: bool = True) -> str:
    key = key.encode("UTF-8")
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(key).digest()
    IV = source[: AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size :])  # noqa:E203
    padding = data[-1]
    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding...")
    return data[:-padding].decode("UTF-8")


def read(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def write(filename: str, content: str) -> None:
    with open(filename, "w") as file:
        file.write(content)


def get_ymd():
    dt = datetime.datetime.today()
    return f"{dt.year}{dt.month:0>2d}{dt.day:0>2d}"
