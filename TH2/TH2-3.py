#Nguyễn Hoàng Điển
#B2113329
#20
import base64
import pandas as pd

from Crypto.Cipher import DES


# Hàm pad để thêm padding cho văn bản
def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

# Hàm unpad để loại bỏ padding sau khi giải mã
def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

# Mã hóa DES
def mahoa_DES(text, key):
    text = pad(text)  # Pad văn bản dưới dạng chuỗi
    key = pad(key)  # Pad key nếu cần
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)  # Chuyển key thành bytes
    entxt = cipher.encrypt(text.encode('utf-8'))  # Chuyển text thành bytes
    return base64.b64encode(entxt).decode('utf-8')

# Giải mã DES
def giaima_DES(input_text, key):

    encrypted_text = input_text
    # Decrypt and remove padding
    txt = base64.b64decode(encrypted_text)
    key = pad(key).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt)).decode("utf8")

    return detxt  # Unpad văn bản đã giải mã

if __name__ == '__main__':
    data = pd.read_csv("country.csv", quotechar='"', skipinitialspace=True)

    countries = data.iloc[:, -1].values.tolist()
    print(countries)
    original_text = 'The treasure is under the coconut tree'
    encrypted_text = 'lIZg7tB/NvuG4MXsCDFUsRjvQrjw/UuUGzZw+QMMDF4nGjQCGzY0Uw=='
    key = ""
    for country in countries:
        if len(country) <= 8:
            try:
                encrypt_try = giaima_DES(encrypted_text, country)
                if encrypt_try == original_text:
                    print(f"Tìm thấy khóa: {country}")
                    key = country
                    break
            except:
                pass

    encrypted_text_2 = "LsmDvf9t1pLPn+NZ99+cVx+V1ROl2/9KNqk9PLTe5uRii/aNc/X3tw=="
    print("row2: ",giaima_DES(encrypted_text_2, key))

    encrypted_text_3 = "5cdbWs00vXghkBLECplG8ClNQ2Da5R/9KZ0bAKRs+bPvhwOwIt7Sh2ZZFtxHBAK9"
    print("row3: ",giaima_DES(encrypted_text_3, key))
