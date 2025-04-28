#Nguyen Hoang Dien
#B2113329
#4
def Char2Num(c):
	return ord(c)-65
def Num2Char(n):
	return chr(n+65)
	
def encryptAF(txt,a,b,m):
	r = ""
	for c in txt:
		e = (a*Char2Num(c)+b) % m
		r = r+Num2Char(e)
	return r
print(encryptAF("HELLO", 3, 5, 26))


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

print(decryptAF("HELLO", 3, 5, 26))