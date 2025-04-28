#Nguyễn Hoàng Điển
#B2113329
#20


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("Welcome to Demo AT&BMTT")
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHUONG TRINH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MAT MA BAT DOI XUNG RSA",font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

plainlb = Label(window, text="Van ban goc",font=("Arial", 14))
plainlb.grid(column=0, row=3)
plaintxt = Entry(window,width=90)
plaintxt.grid(column=1, row=3)

cipher = Label(window, text="Van ban duoc ma hoa",font=("Arial", 14))
cipher.grid(column=0, row=4)
ciphertxt = Entry(window,width=90)
ciphertxt.grid(column=1, row=4)

plainl1 = Label(window, text="Van ban duoc giai ma",font=("Arial", 14))
plainl1.grid(column=0, row=5)
plaintxt1 = Entry(window,width=90)
plaintxt1.grid(column=1, row=5)

pri_key = Label(window, text="Khoa ca nhan",font=("Arial", 14))
pri_key.grid(column=0, row=6)
pri_keyla = Text(window,width=65, height=10)
pri_keyla.grid(column=1, row=6)

pub_key = Label(window, text="Khoa cong khai",font=("Arial", 14))
pub_key.grid(column=0, row=7)
pub_keyla = Text(window,width=65, height=10)
pub_keyla.grid(column=1, row=7)

def save_file(content, _mode, _title, _filetypes, _defaultextension):
    f = filedialog.asksaveasfile(mode=_mode,
                                 initialdir="D:/ATBMTT/TH3",
                                 title=_title,
                                 filetypes=_filetypes,
                                 defaultextension=_defaultextension)
    if f:
        f.write(content)
        f.close()


def generate_key():
    key = RSA.generate(1024)
    save_file(key.exportKey('PEM'),
              'wb',
              'Lưu khóa cá nhân',
              (("All files", "*.*"), ("PEM files", "*.pem")),
              ".pem")
    save_file(key.publickey().exportKey('PEM'),
              'wb',
              'Lưu khóa công khai',
              (("All files", "*.*"), ("PEM files", "*.pem")),
              ".pem")
    pri_keyla.delete('1.0', END)
    pri_keyla.insert(END, key.exportKey('PEM'))
    pub_keyla.delete('1.0', END)
    pub_keyla.insert(END, key.publickey().exportKey('PEM'))


def get_key(key_style):
    filename = filedialog.askopenfilename(initialdir="D:/ATBMTT/TH3",
                                          title="Open " + key_style,
                                          filetypes=(("PEM files", "*.pem"), ("All files", "*.*")))
    if filename:
        with open(filename, "rb") as file:
            key = file.read()
        return RSA.importKey(key)
    return None


def mahoa_rsa():
    txt = plaintxt.get().encode()
    pub_key = get_key("Public Key")
    if not pub_key:
        return
    cipher = PKCS1_v1_5.new(pub_key)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt).decode()
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)


def giaima_rsa():
    entxt = ciphertxt.get()
    pri_key = get_key("Private Key")
    if not pri_key:
        return
    cipher = PKCS1_v1_5.new(pri_key)
    try:
        detxt = cipher.decrypt(base64.b64decode(entxt), None).decode()
        plaintxt1.delete(0, END)
        plaintxt1.insert(INSERT, detxt)
    except Exception as e:
        plaintxt1.delete(0, END)
        plaintxt1.insert(INSERT, "Giải mã thất bại!")


taokhoa = Button(window, text="Tạo khóa", command=generate_key)
taokhoa.grid(column=1, row=8)

AFbtn = Button(window, text="Mã Hóa", command=mahoa_rsa)
AFbtn.grid(column=1, row=9)

DEAFbtn = Button(window, text="Giải mã", command=giaima_rsa)
DEAFbtn.grid(column=1, row=10)

window.geometry('800x600')
window.mainloop()
