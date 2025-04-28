#Nguyễn Hoàng Điển
#B2113329
#20

import random
import math

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n %i == 0:
            return False
    return True

#Hàm tìm số nguyên tố
def generate_large_prime():
    while True:
        num = random.randint(100, 10000000)
        if is_prime(num):
            return num

# Hàm tìm ước chung lớn nhất
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

# Hàm tìm nghịch đảo modulo
def mod_inverse(e, phi):
    for d in range (2, phi):
        if(e*d) % phi == 1:
            return d
    return None

def generate_key():
    p = generate_large_prime()
    q = generate_large_prime()
    while p == q:
        q = generate_large_prime()

    n = p*q
    phi = (p-1)*(q-1)
    e = random.randint(2, phi - 1)
    while gcd(e , phi) != 1:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(plaitext, pub_key):
    e, n = pub_key
    cipher_text = [pow(ord(char), e, n) for char in plaitext]
    return cipher_text

def decrypt(cipher_text, pri_key):
    d, n = pri_key
    plain_text = ''.join(chr(pow(char, d, n)) for char in cipher_text)
    return plain_text

public_key, private_key = generate_key()
print("Public Key:", public_key)
print("Private Key:", private_key)

message = "HELLO, I'M NGUYEN HOANG DIEN, NICE TO MEET YOU"
cipher_text = encrypt(message, public_key)
print("Văn bản mã hóa:", cipher_text)

decrypted_text = decrypt(cipher_text, private_key)
print("Văn bản giải mã:", decrypted_text)