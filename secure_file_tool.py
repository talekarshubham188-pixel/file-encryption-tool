from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

def encrypt_file(file_name):
    with open(file_name, "rb") as f:
        data = f.read()

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open(file_name + ".enc", "wb") as f:
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

    print("File encrypted successfully")

file_name = input("Enter file name to encrypt: ")
encrypt_file(file_name)