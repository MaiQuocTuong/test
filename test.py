import math

def menu():
	print('----------Menu-----------')
	print('| 0_Thoát               |')
	print('| 1_Tính toán           |')
	print('| 2_Giải phương trình   |')
	print('| 3_Giải hệ phương trình|')
	print('-------------------------')
menu()
s = input("s = ")
if s == 1: 
	print('| 0_Thoát               |')
	print('| 1_Phép cộng           |')
	print('| 2_Phép trừ            |')
	print('| 3_Phép nhân           |')
	print('| 4_Phép chia           |')
	print('-------------------------')
	m = input("m = ")
	if m == 0:
		menu()
		if m == 1:
			w = input("w = ")
			k = input("k = ")
			c = w + k
			print("w + k = ", c)
		elif m == 2:
			w = input("w = ")
			k = input("k = ")
			c1 = w - k
			print("w - k = ", c1)
		elif m == 3:
			w = input("w = ")
			k = input("k = ")
			c3 = w * k
			print("w x k = ", c3)
		else :
			w = input("w = ")
			k = input("k = ")
			c2 = w / k
			print("w : k = ", c2)
		tinh_toan()
elif s == 2:
	print('-------Phương Trình-------')
	print('|0_Thoát                 |')
	print('|1_Phương Trình Bậc Nhất |')
	print('|2_Phương Trình Bậc Hai  |')
	print('|3_Phương Trình Bậc Ba   |')
	print('--------------------------')
	z = input("z = ")
	if z == 0:
		print(menu())
	elif z == 1:
		a = input("a = ")
		b = input("b = ")
		x = -b/a 
		print("x = ", x)
	elif z == 2 :
		a = input("a = ")
		b = input("b = ")
		c = input("c = ")
		denta = b**2 - 4*a*c
		if denta < 0:
			print("Phương trình vô nghiệm.")
		elif denta == 0:
			print("Phương trình có 1 nghiệm:", -b/2*a)
		else:
			x1 = (-b - sprt(denta))/(2*a)
			x2 = -b/a - x1
			print("x1 = ", x1)
			print("x2 = ", x2)
	else:
		a = input("a = ")
		b = input("b = ")
		c = input("c = ")
		d = input("d = ")

elif s == 3:
	g = input("g = ")
	h = input("h = ")
	r = input("r = ")
	d = input("d = ")
	e = input("e = ")
	f = input("f = ")

	if g/d == h/e == r/f :
		print("Hệ phương trình vô nghiệm.")
	elif g/d == h/e != r/f:
		print("Hệ phương trình có vô số nghiệm")
	else:
		x = (r - h/y)/g
		y = (f*g - d*r)/(g*e - h*d)

