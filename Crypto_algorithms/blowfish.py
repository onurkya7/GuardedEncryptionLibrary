from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt_blowfish(plaintext, key):
    backend = default_backend()
    padder = padding.PKCS7(64).padder()
    plaintext = padder.update(plaintext) + padder.finalize()
    iv = os.urandom(8)
    cipher = Cipher(algorithms.Blowfish(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()

    # Encryption process
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return iv + ciphertext

def decrypt_blowfish(ciphertext, key):
    backend = default_backend()
    iv = ciphertext[:8]
    ciphertext = ciphertext[8:]
    cipher = Cipher(algorithms.Blowfish(key), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()

    # Decryption process
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(64).unpadder()
    plaintext = unpadder.update(plaintext) + unpadder.finalize()

    return plaintext

# Generate a Blowfish key (variable length)
blowfish_key = os.urandom(16)

# Data to be encrypted
data_to_encrypt = b"Hello, Blowfish!"

encrypted_data_blowfish = encrypt_blowfish(data_to_encrypt, blowfish_key)
print("Encrypted text (Blowfish):", encrypted_data_blowfish)

decrypted_data_blowfish = decrypt_blowfish(encrypted_data_blowfish, blowfish_key)
print("Decrypted text (Blowfish):", decrypted_data_blowfish.decode())
