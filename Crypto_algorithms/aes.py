from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt(plaintext, key):
    backend = default_backend()

    # Padding process
    padder = padding.PKCS7(128).padder()
    plaintext = padder.update(plaintext) + padder.finalize()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()

    # Encryption process
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return iv + ciphertext

def decrypt(ciphertext, key):
    backend = default_backend()
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()

    # Decryption process
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(plaintext) + unpadder.finalize()

    return plaintext

# Generate a key (128, 192, or 256 bits)
key = os.urandom(32)

# Data to be encrypted
data_to_encrypt = b"Hello, AES!"

encrypted_data = encrypt(data_to_encrypt, key)
print("Encrypted text:", encrypted_data)

decrypted_data = decrypt(encrypted_data, key)
print("Decrypted text:", decrypted_data.decode())
