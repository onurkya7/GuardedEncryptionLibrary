from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_des(plaintext, key):
    cipher = DES.new(key, DES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
    return cipher.iv + ciphertext

def decrypt_des(ciphertext, key):
    iv = ciphertext[:DES.block_size]
    ciphertext = ciphertext[DES.block_size:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return plaintext

# Generate a DES key (8 bytes)
des_key = get_random_bytes(8)

# Data to be encrypted
data_to_encrypt = b"Hello, DES!"

encrypted_data_des = encrypt_des(data_to_encrypt, des_key)
print("Encrypted text (DES):", encrypted_data_des)

decrypted_data_des = decrypt_des(encrypted_data_des, des_key)
print("Decrypted text (DES):", decrypted_data_des.decode())
