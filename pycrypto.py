#Miniconda http://conda.pydata.org/miniconda.html

from Crypto.Vipher import AES
import base64

msg = "MSG"
password = "xxx"
iv = "xxxx"
mode = AES.MODE_CBS

def mkpad():
    s = s.encode()
    pad = b' ' * ()
    return s + pad

enc = encrypt(password, msg)
dec = decrypt(password, enc)

print("", enc)
print("", dec)

