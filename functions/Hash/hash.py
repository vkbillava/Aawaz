import hashlib
import rsa

publicKey, privateKey = rsa.newkeys(512)

def get_hash(name):
    with open(name, "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.md5(bytes).hexdigest()
    return readable_hash

def pass_hash(pswd):
    text = hashlib.md5(pswd.encode())

    return text.hexdigest()

def store_pass_hash(paswd):
    return rsa.encrypt(paswd.encode(), publicKey)

def hash_decode(pswd):
    return rsa.decrypt(pswd, privateKey).decode()