from paranoid import __version__

from paranoid.modules import util


def test_version():
    assert __version__ == "0.1.0"


def test_util_encrypt_decrypt():
    password = "mypassword123"
    message = "some data"

    print("\nmessage:", message)
    print("password:", password)

    encrypted_message = util.encrypt(password, message)
    print("encrpyted_message:-->", encrypted_message)

    decrpyted_message = util.decrypt(password, encrypted_message)
    print("decrypted_message:-->", decrpyted_message)

    assert message == decrpyted_message
