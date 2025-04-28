#Nguyễn Hoàng Điển
#B2113329
#20

from tkinter import *
from Crypto.Cipher import DES
import base64

window = Tk()
window.title("Welcome to Demo AT&BMTT")
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHUONG TRINH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MAT MA DOI XUNG DES",font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

plainlb = Label(window, text="Van ban goc",font=("Arial", 14))
plainlb.grid(column=0, row=3)
plaintxt = Entry(window,width=100)
plaintxt.grid(column=1, row=3)

KEYlb = Label(window, text="Khoa",font=("Arial", 14))
KEYlb.grid(column=0, row=4)
KEYAL = Entry(window,width=100)
KEYAL.grid(column=1, row=4)

cipher = Label(window, text="Van ban duoc ma hoa",font=("Arial", 14))
cipher.grid(column=0, row=5)
ciphertxt = Entry(window,width=100)
ciphertxt.grid(column=1, row=5)

plainl1 = Label(window, text="Van ban duoc giai ma",font=("Arial", 14))
plainl1.grid(column=0, row=6)
plaintxt1 = Entry(window,width=100)
plaintxt1.grid(column=1, row=6)

def pad(s):
    # Thêm vào cuối số còn thiếu cho đủ bội của 8
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def mahoa_DES():
    txt = pad(plaintxt.get()).encode("utf8")
    key = pad(KEYAL.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)


def giaima_DES():
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    key = pad(KEYAL.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    plaintxt1.delete(0, END)
    plaintxt1.insert(INSERT, detxt)

AFbtn = Button(window, text="Mã Hóa", command=mahoa_DES)
AFbtn.grid(column=0, row=7)

DEAFbtn = Button(window, text="Giải Mã", command=giaima_DES)
DEAFbtn.grid(column=1, row=7)


window.geometry('800x600')
window.mainloop()