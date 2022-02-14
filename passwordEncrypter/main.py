from email import message
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from rsa import decrypt

salt = b'\x0fJ\x18n\x80\x1a\x18S\xb2\x82\x9f|H\xbf\xaa\x0b\x94\xaf9\x93\xf0>\x90\x1es\xf0\x03\x18a\x7f`\xb4'
password = "mypassword"

key = PBKDF2(password, salt, dkLen = 32)

message = b"Hello World"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

print(ciphered_data)

with open('encrypted bin', 'wb') as f :
    f.write(cipher.iv)
    f.write(ciphered_data)

with open('encrypted bin', 'rb') as f :
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv = iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)

print(original)
