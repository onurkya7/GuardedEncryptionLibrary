from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_rc4(plaintext, key):
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(pad(plaintext, cipher.block_size))
    return ciphertext

def decrypt_rc4(ciphertext, key):
    cipher = ARC4.new(key)
    plaintext = unpad(cipher.decrypt(ciphertext), cipher.block_size)
    return plaintext

# RC4
rc4_key = get_random_bytes(16)
data_to_encrypt_rc4 = b"Hello, RC4!"

encrypted_data_rc4 = encrypt_rc4(data_to_encrypt_rc4, rc4_key)
print("Encrypted text (RC4):", encrypted_data_rc4)

decrypted_data_rc4 = decrypt_rc4(encrypted_data_rc4, rc4_key)
print("Decrypted text (RC4):", decrypted_data_rc4.decode())
