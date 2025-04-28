# Họ và tên sinh viên: Nguyễn Hoàng Điển
# Mã số sinh viên: B2113329
# STT: 20

import base64
from tkinter import *
from tkinter import filedialog
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
import os
import csv
import hashlib
import random
from tkinter import messagebox

window = Tk()
window.title("Welcome to Demo AT&BMTT")
lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="TAO TAI KHOAN", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

plainlb = Label(window, text="Tên đăng nhập", font=("Arial", 14))
plainlb.grid(column=0, row=3)
plaintxt = Entry(window, width=40)
plaintxt.grid(column=1, row=3)

plainlb1 = Label(window, text="Mât Khẩu", font=("Arial", 14))
plainlb1.grid(column=0, row=4)
plaintxt1 = Entry(window, width=40)
plaintxt1.grid(column=1, row=4)


def hash_password(password):
    hash_methods = [MD5, SHA1, SHA256, SHA512]
    hash_method = random.choice(hash_methods)
    h = hash_method.new()
    h.update(password.encode('utf-8'))
    return h.hexdigest()


def create_account():
    username = plaintxt.get()
    password = plaintxt1.get()
    if not username or not password:
        messagebox.showwarning("Warning", "Tên đăng nhập và mật khẩu không được để trống!")
        return

    file_exists = os.path.isfile('CSDL.csv')
    if file_exists:
        with open('CSDL.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == username:
                    messagebox.showwarning("Warning", "Tên đăng nhập đã tồn tại!")
                    return

    hashed_password = hash_password(password)
    with open('CSDL.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, hashed_password])

    messagebox.showinfo("Success", "Tạo tài khoản thành công!")


TaoTaiKhoan = Button(window, text="Tạo tài khoản", command=create_account)
TaoTaiKhoan.grid(column=1, row=5)

window.geometry('450x200')
window.mainloop()