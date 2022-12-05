import hashlib
import base64
import uuid

def hash(password, salt):
    sha = hashlib.sha256()
    sha.update((password+salt).encode("utf-8"))
    hashed=base64.urlsafe_b64encode(sha.digest()).decode("utf-8")
    return hashed

def genHash(password):
    salt = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8")
    hashed = hash(password,salt)
    return salt+"."+hashed

def vfyPassword(password, vfyPassword):
    parts = vfyPassword.split(".")
    salt = parts[0]
    vfyHash = parts[1]
    verified = vfyHash == hash(password, salt)
    return verified
   

