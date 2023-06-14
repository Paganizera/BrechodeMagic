from cryptography.fernet import Fernet

 
key = Fernet.generate_key()
def encode(password):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode())
def decode(password):  
    fernet = Fernet(key)
    return fernet.decrypt(password).decode() 
