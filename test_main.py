import unittest
from main import *

class TestMorse(unittest.TestCase):
    def test_roundtrip(self):
        plaintext = "WHAT HATH GOD WROUGHT"
        self.assertEqual(plaintext, decode_morse(encode_morse(plaintext)))

    def test_encode(self):
        plaintext = "WHAT HATH GOD WROUGHT"
        self.assertEqual(encode_morse(plaintext), '.-- .... .- - / .... .- - .... / --. --- -.. / .-- .-. --- ..- --. .... -')
    def test_decode(self):
        encoded = '.-- .... .- - / .... .- - .... / --. --- -.. / .-- .-. --- ..- --. .... -'
        self.assertEqual(decode_morse(encoded), "WHAT HATH GOD WROUGHT")

    def test_errors(self):
        plaintext = "!&*() - not in our morse dictionary"
        self.assertEqual(encode_morse(plaintext), "ERROR: ! cannot be encoded in Morse")
        encoded = "not dots and dashes"
        self.assertEqual(decode_morse(encoded), "ERROR: not cannot be decoded in Morse")

class TestBase64(unittest.TestCase):
    def test_roundtrip(self):
        plaintext = "base64 is really a family of related functions"
        self.assertEqual(plaintext, decode_base64(encode_base64(plaintext)))

    def test_encode(self):
        plaintext = "base64 is really a family of related functions"
        self.assertEqual(encode_base64(plaintext), 'YmFzZTY0IGlzIHJlYWxseSBhIGZhbWlseSBvZiByZWxhdGVkIGZ1bmN0aW9ucw==')

    def test_decode(self):
        encoded = "YmFzZTY0IGlzIHJlYWxseSBhIGZhbWlseSBvZiByZWxhdGVkIGZ1bmN0aW9ucw=="
        self.assertEqual(decode_base64(encoded), "base64 is really a family of related functions")

class TestEncrypt(unittest.TestCase):
    def test_roundtrip(self):
        plaintext = "Fernet is an Italian type of amaro, a bitter, aromatic spirit."
        self.assertEqual(plaintext, decrypt(encrypt(plaintext)))

if __name__ == "__main__":
    unittest.main()

