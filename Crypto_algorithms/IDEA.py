from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

def idea_encrypt(data, key):
    backend = default_backend()
    iv = urandom(8)
    cipher = Cipher(algorithms.IDEA(key), mode=modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    return encrypted_data

def idea_decrypt(encrypted_data, key):
    backend = default_backend()
    iv = encrypted_data[:8]  
    cipher = Cipher(algorithms.IDEA(key), mode=modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data[8:]) + decryptor.finalize()
    return decrypted_data

# Example usage
data = b"Hello World!1234"  # 64-bit plaintext
key = urandom(16)  # 128-bit key

encrypted_data = idea_encrypt(data, key)
print("Encrypted Data Block:", encrypted_data)

decrypted_data = idea_decrypt(encrypted_data, key)
print("Decrypted Data Block:", decrypted_data)
