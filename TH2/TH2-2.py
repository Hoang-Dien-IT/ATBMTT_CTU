#Nguyễn Hoàng Điển
#B2113329
#20
from Crypto.Cipher import DES
import base64

def pad(s):
    # Add padding to ensure the length is a multiple of 8
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    # Remove padding
    return s[:-ord(s[len(s)-1:])]

def encrypt_file(input_file, key):
    # Read content from the input file
    with open(input_file, 'r') as file:
        plaintext = file.read()

    # Add padding and encrypt
    txt = pad(plaintext).encode("utf8")
    key = pad(key).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt).decode("utf8")

    return entxt

def decrypt_file(input_file, key):
    # Read encrypted content from the input file
    with open(input_file, 'r') as file:
        encrypted_text = file.read()

    # Decrypt and remove padding
    txt = base64.b64decode(encrypted_text)
    key = pad(key).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt)).decode("utf8")

    return detxt

# Input file path and key from the user
input_file = "test_DES.txt"
key = input("Enter key (8 characters): ")

# Encrypt the file
text = encrypt_file(input_file, key)
print("Encryption complete. Result:", text)

output_file = "encrypted_DES.txt"
with open(output_file, 'w') as file:
    file.write(text)

# Decrypt the file (if needed)
decrypt_input_file = "encrypted_DES.txt"
text1 = decrypt_file(decrypt_input_file, key)
print("Decryption complete. Result:", text1)

