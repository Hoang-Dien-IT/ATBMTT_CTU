#Nguyen Hoang Dien
#B2113329
#4
from tkinter import *
# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")
# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHUONG TRINH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)	
lb2 = Label(window, text="MAT MA AFFINE",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)
plainlb3 = Label(window, text="PLAIN TEXT",font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window,width=20)
plaintxt.grid(column=1, row=3)
KEYlb4 = Label(window, text="KEY PAIR",font=("Arial", 14))
KEYlb4.grid(column=2, row=3)
KEYA1 = Entry(window,width=3)
KEYA1.grid(column=3, row=3)
KEYB1 = Entry(window,width=5)
KEYB1.grid(column=4, row=3)

cipher3 = Label(window, text="CIPHER TEXT",font=("Arial", 14))
cipher3.grid(column=0, row=4)
ciphertxt3 = Entry(window,width=20)
ciphertxt3.grid(column=1, row=4)

def Char2Num(c):
	if c == ' ':
		return 52  # Dấu cách được gán là 52
	if c.islower():
		return ord(c) - 97 + 26  # Chữ thường (26 ký tự sau chữ hoa)
	return ord(c) - 65  # Chữ hoa

def Num2Char(n):
	if n == 52:
		return ' '  # Trả về dấu cách cho số 52
	if n >= 26:  # Chữ thường
		return chr(n - 26 + 97)
	return chr(n + 65)  # Chữ hoa

def encryptAF(txt,a,b,m):
	r = ""
	for c in txt:
		e = (a*Char2Num(c)+b) % m
		r = r+Num2Char(e)
	return r
	
def mahoa():
	a = int(KEYA1.get())
	b = int(KEYB1.get())
	m = 53
	entxt = encryptAF(plaintxt.get(),a,b,m)
	ciphertxt3.delete(0,END)
	ciphertxt3.insert(INSERT,entxt)
	
	
def xgcd(a,m):
	temp = m;
	x0, x1, y0, y1 = 1, 0, 0, 1
	while m!=0:
		q, a, m = a // m, m, a % m
		x0, x1 = x1, x0 - q * x1
		y0, y1 = y1, y0 - q * y1
	if x0 < 0: x0 = temp + x0
	return x0
	
def decryptAF(txt,a,b,m):
	r = ""
	a1 = xgcd(a,m)
	for c in txt:
		e = (a1*(Char2Num(c)-b))%m
		r =r+Num2Char(e)
	return r
	
def giaima():
	a = int(KEYA1.get())
	b = int(KEYB1.get())
	m = 53
	entxt = decryptAF(ciphertxt3.get(),a,b,m)
	plaintxt2.delete(0,END)
	plaintxt2.insert(INSERT,entxt)
	

AFbtn = Button(window, text="Mã Hóa", command=mahoa)
AFbtn.grid(column=5, row=3)

DEAFbtn = Button(window, text="Giai Ma", command=giaima)
DEAFbtn.grid(column=2, row=4)
plaintxt2 = Entry(window,width=20)
plaintxt2.grid(column=4, row=4)

window.geometry('800x600')
window.mainloop()


