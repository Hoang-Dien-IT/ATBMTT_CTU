import math

def mod_inverse(a, m):  # Hàm tìm nghịch đảo của a modulo m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def Char2Num(c):  # Hàm chuyển ký tự thành số
    if c.isupper():  # Chữ hoa (A-Z)
        return ord(c) - 65  # 0-25
    elif c.islower():  # Chữ thường (a-z)
        return ord(c) - 97 + 26  # 26-51
    elif c == ' ':  # Khoảng trắng
        return 52  # 52
    elif c.isdigit():  # Số (0-9)
        return ord(c) - 48 + 53  # 53-62
    else:
        raise ValueError("Ký tự không hợp lệ!")


def Num2Char(n):  # Hàm chuyển số thành ký tự
    if n < 26:
        return chr(n + 65)  # A-Z
    elif n >= 26 and n < 52:
        return chr(n + 97 - 26)  # a-z
    elif n == 52:
        return ' '  # khoảng trắng
    elif n <= 62 and n >= 53:
        return chr(n + 48 - 53)  # 0-9
    else:
        raise ValueError("Giá trị không hợp lệ!")


def decrypt_affine(ciphertext, a, b):  # Hàm giải mã Affine
    m = 62  # Kích thước bảng chữ cái gồm A-Z, a-z, 0-9 và khoảng trắng
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None

    decrypted_text = ""
    for c in ciphertext:
        p = (a_inv * (Char2Num(c) - b)) % m
        decrypted_text += Num2Char(p)

    return decrypted_text


# Danh sách các giá trị a hợp lệ
valid_a_values = {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55,
                  57, 59, 61}

# Ciphertext đã cho
cipher_text = "gAdX5d6IXpvBX3XawdSLHIXIAdXCTITwdXL6XIPXHwdvIdXLI"

# Tìm ra cặp khóa (a, b) phù hợp và thông điệp
for a in valid_a_values:
    for b in range(62):  # b trong phạm vi 0 đến 61
        decrypted = decrypt_affine(cipher_text, a, b)
        if decrypted and "predict" in decrypted.lower():  # Kiểm tra nếu có từ "predict" trong thông điệp
            print(f"🔹 Tìm thấy khóa! (a={a}, b={b})")
            print(f"Thông điệp: {decrypted}")
            exit()