import random
import math


def is_prime(n, k=5):
    if n < 2:
        return False
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True


def generate_prime(bits=16):
    while True:
        num = random.getrandbits(bits) | 1
        if is_prime(num):
            return num


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

    g, x, _ = egcd(e, phi)
    if g != 1:
        raise Exception("Không tìm thấy nghịch đảo modular")
    return x % phi


def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(message, pub_key):
    e, n = pub_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher


def decrypt(cipher, priv_key):
    d, n = priv_key
    message = ''.join(chr(pow(char, d, n)) for char in cipher)
    return message



public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

message = "HELLO, I'M NGUYEN HOANG DIEN, NICE TO MEET YOU"
cipher_text = encrypt(message, public_key)
print("Văn bản mã hóa:", cipher_text)

decrypted_text = decrypt(cipher_text, private_key)
print("Văn bản giải mã:", decrypted_text)
