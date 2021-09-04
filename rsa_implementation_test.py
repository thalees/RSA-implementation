import base64
import binascii

from rsa_implementation import (encrypt, dencrypt)

def is_base64(s):
    try:
        base64.decodebytes(s)
        return True
    except binascii.Error:
        return False

public_key_mock = (15776038139088582906797, 66678275526824262145921)
private_key_mock = (51395388263817200503133, 66678275526824262145921)

def test_returns_the_encrypted_value_successfully():
    message = 'some message'
    response = encrypt(message, public_key_mock).encode()

    assert is_base64(response)

def test_returns_the_decrypted_value_successfully():
    message = 'test'
    encrypted_message = encrypt(message, public_key_mock)
    
    response = dencrypt(encrypted_message, private_key_mock)

    assert response == message
