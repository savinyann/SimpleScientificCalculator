#!/usr/bin/python3
#from tkinter import * 
import tkinter
import time
import math
import random

dot = False
Seconde = False
calc_ended = True
value1 = None
value2 = None
value3 = None
par = []
par_value = -1
fenetre = tkinter.Tk()
value = tkinter.DoubleVar()
sin = tkinter.StringVar()
cos = tkinter.StringVar()
tan = tkinter.StringVar()
ln = tkinter.StringVar()
log = tkinter.StringVar()
sqrt = tkinter.StringVar()
power = tkinter.StringVar()
ans = tkinter.StringVar()
angle = tkinter.StringVar()
value.set(0)
sin.set('sin')
cos.set('cos')
tan.set('tan')
ln.set('ln')
log.set('log')
sqrt.set('√')
power.set('x^y')
ans.set('Ans')
angle.set("rad")

def display():
	print(value.get())

def updatetext():
	global Seconde, calc_ended
	Label0_0.config(text = value.get())
	if(Seconde == True):
		Seconde_func()
	calc_ended = False

def Seconde_func():
	global Seconde, sin
	Seconde = True if (Seconde == False) else False
	sin.set('sin' if (Seconde == False) else 'arcsin')
	cos.set('cos' if (Seconde == False) else 'arccos')
	tan.set('tan' if (Seconde == False) else 'arctan')
	ln.set('ln' if (Seconde == False) else 'e^x')
	log.set('log' if (Seconde == False) else '10^x')
	sqrt.set('√' if (Seconde == False) else 'x²')
	power.set('x^y' if (Seconde == False) else '(y)√x')
	ans.set('Ans' if (Seconde == False) else 'Rnd')
	Pannel2_1.winfo_children()[1].config(text = sin.get())
	Pannel2_2.winfo_children()[1].config(text = cos.get())
	Pannel2_3.winfo_children()[1].config(text = tan.get())
	Pannel2_1.winfo_children()[2].config(text = ln.get())
	Pannel2_2.winfo_children()[2].config(text = log.get())
	Pannel2_3.winfo_children()[2].config(text = sqrt.get())
	Pannel2_4.winfo_children()[2].config(text = power.get())
	Pannel2_4.winfo_children()[0].config(text = ans.get())
	Pannel2_0.winfo_children()[0].config(relief = tkinter.SUNKEN if (Seconde == True) else tkinter.RAISED)

def error():
	global value	
	value = tkinter.StringVar()
	value.set('ERROR')
	updatetext()


def add_0():
	global dot, calc_ended
	if(calc_ended == True):
		value.set(0)
	else:
		value.set((value.get() * 10))
		dot = dot-1 if(dot != False) else dot
	updatetext();
def add_1():
	global dot, calc_ended
	if(calc_ended == True):
		value.set(1)
	else:
		value.set((value.get() * 10 + 1 if (dot == False) else value.get() + 1 * math.pow(10, dot)))
		dot = dot-1 if(dot != False) else dot
	updatetext();
def add_2():
	global dot, calc_ended
	if(calc_ended == True):
		value.set(2)
	else:
		value.set((value.get() * 10 + 2 if (dot == False) else value.get() + 2 * math.pow(10, dot)))
		dot = dot-1 if(dot != False) else dot
	updatetext();
def add_3():
	global dot, calc_ended
	if(calc_ended == True):
		value.set(3)
	else:
		value.set((value.get() * 10 + 3 if (dot == False) else value.get() + 3 * math.pow(10, dot)))
		dot = dot-1 if(dot != False) else dot
	updatetext();
def add_4():
	global dot, calc_ended
	if(calc_ended == True):
		value.set(4)
	else:
		value.set((value.get() * 10 + 4 if (dot == False) else value.get() + 4 * math.pow(10, dot)))
		dot = dot-1 if(dot != False) else dot
	updatetext();
def add_5():
	global dot, calc_ended
	if(calc_ended == True):
		value.set(5)
	else:
		value.set((value.get() * 10 + 5 if (dot == False) else value.get() + 5 * math.pow(10, dot)))
		dot = dot-1 if(dot != False) else dot
	updatetext();
def add_6():
	global dot, calc_ended
	if(calc_ended == True):
		value.set(6)
	else:
		value.set((value.get() * 10 + 6 if (dot == False) else value.get() + 6 * math.pow(10, dot)))
		dot = dot-1 if(dot != False) else dot
	updatetext();
def add_7():
	global dot, calc_ended
	if(calc_ended == True):
		value.set(7)
	else:
		value.set((value.get() * 10 + 7 if (dot == False) else value.get() + 7 * math.pow(10, dot)))
		dot = dot-1 if(dot != False) else dot
	updatetext();
def add_8():
	global dot, calc_ended
	if(calc_ended == True):
		value.set(8)
	else:
		value.set((value.get() * 10 + 8 if (dot == False) else value.get() + 8 * math.pow(10, dot)))
		dot = dot-1 if(dot != False) else dot
	updatetext();
def add_9():
	global dot, calc_ended
	if(calc_ended == True):
		value.set(9)
	else:
		value.set((value.get() * 10 + 9 if (dot == False) else value.get() + 9 * math.pow(10, dot)))
		dot = dot-1 if(dot != False) else dot
	updatetext();

def add_pi():
	global calc_ended
	if(value.get() == 0):
		value.set(math.pi)
	else:
		value.set(value.get() * math.pi)
	updatetext();
	calc_ended = True

def add_e():
	global calc_ended
	if(value.get() == 0):
		value.set(math.exp(1))
	else:
		value.set(value.get() * math.exp(1))
	updatetext();
	calc_ended = True

def reset_func():
	global value1, value2, value3, value, dot, calc_ended
	value1 = None
	value2 = None
	value = tkinter.DoubleVar()
	value.set(0)
	dot = False
	updatetext()
	calc_ended = True

def equ_func():
	global value1, value2, value3, value, dot, calc_ended
	if(value1 != None and value2 != None):
		if(value2 == "+"):
			value.set(value1 + value.get())
		if(value2 == "-"):
			value.set(value1 - value.get())
		if(value2  == "*"):
			value.set(value1 * value.get())
		if(value2  == "/"):
			if(value.get() == 0):
				error()
			else:
				value.set(value1 / value.get())
		if(value2 == "^"):
			value.set(math.pow(value1, value.get()))
		if(value2 == "√"):
			value.set(math.pow(value1, (1 / value.get())))
		if(value2 == 'x10'):
			value.set(value1 * math.pow(10, value.get()))
		value1 = None
		value2 = None
		value3 = value.get()
		updatetext()
		calc_ended = True


def add_func():
	global value1, value2, value3, dot
	if(value1 != None):
		equ_func()
	value1 = value.get()
	value2 = "+"
	value.set(0)
	dot = False


def sub_func():
	global value1, value2, value3, dot
	if(value1 != None):
		equ_func()
	value1 = value.get()
	value2 = "-"
	value.set(0)
	dot = False


def mult_func():
	global value1, value2, value3, dot
	if(value1 != None):
		equ_func()
	value1 = value.get()
	value2 = "*"
	value.set(0)
	dot = False


def div_func():
	global value1, value2, value3, dot
	if(value1 == None):
		equ_func()
	value1 = value.get();
	value2 = '/'
	value.set(0)
	dot = False

def pow_func():
	global value1, value2, value3, dot
	if(Pannel2_4.winfo_children()[2].config()['text'][4] == 'x^y'):
		if(value1 == None):
			equ_func()
		value1 = value.get()
		value2 = "^"
	else:
		if(value1 == None):
			equ_func()
		value1 = value.get()
		value2 = "√"
	value.set(0)
	dot = False


def perc_func():
	global value, calc_ended
	if(value.get() > 1):
		error()
	else:
		temp = value.get() * 100
		value = tkinter.StringVar()
		value.set(str(temp) + "%")
		updatetext()
		value = tkinter.IntVar()
		value.set(temp)
		calc_ended = True

def add_coma():
	global dot, value
	temp = value.get()
	value = tkinter.DoubleVar()
	value.set(temp)
	dot = -1

def ans_func():
	global value3, value, dot, calc_ended
	if(Pannel2_4.winfo_children()[2].config()['text'][4] == 'Ans'):
		value.set(value3)
	else:
		if(value.get() == 0):
			value.set(random.random())
		else:
			value.set(value.get() * random.random())
	dot = False
	updatetext()
	calc_ended = True

def sqrt_func():
	global value, dot, calc_ended
	if(Pannel2_3.winfo_children()[2].config()['text'][4] == '√'):
		value.set(math.sqrt(value.get()))
	else:
		value.set(math.pow(value.get(), 2))
	dot = False
	updatetext()
	calc_ended = True

def tan_func():
	global value, dot, angle, calc_ended
	if(Pannel2_3.winfo_children()[1].config()['text'][4] == 'tan'):
		if(value.get()%math.pi == math.pi/2):
			error()
		else:
			value.set(math.tan(value.get()) if(angle.get() == "rad") else math.tan(math.radians(value.get())))
	else:
		value.set(math.atan(value.get()) if (angle.get() == "rad") else math.degrees(math.atan(value.get())))
	dot = False
	updatetext()
	calc_ended = True

def x10_func():
	global value1, value2, value, dot
	dot = False
	value1 = value.get()
	value2 = 'x10'
	value.set(0)

def log_func():
	global value, dot, calc_ended
	if(Pannel2_2.winfo_children()[2].config()['text'][4] == 'log'):
		if(value.get() == 0):
			error()
		else:
			value.set(math.log(value.get(), 10))
			updatetext()
			calc_ended = True
	else:
		value.set(math.pow(10, value.get()))
		updatetext()
		calc_ended = True
	dot = False

def cos_func():
	global value, dot, calc_ended
	if(Pannel2_2.winfo_children()[1].config()['text'][4] == 'cos'):
		value.set(math.cos(value.get()) if(angle.get() == "rad") else math.cos(math.radians(value.get())))
	else:
		value.set(math.acos(value.get()) if(angle.get() == "rad") else math.degrees(math.acos(value.get())))
	dot = False
	updatetext()
	calc_ended = True

def sin_func():
	global value, dot, calc_ended
	if(Pannel2_1.winfo_children()[1].config()['text'][4] == 'sin'):
		value.set(math.sin(value.get()) if(angle.get() == "rad") else math.sin(math.radians(value.get())))
	else:
		value.set(math.asin(value.get()) if(angle.get() == "rad") else math.degrees(math.asin(value.get())))
	dot = False
	updatetext()
	calc_ended = True

def ln_func():
	global value, dot, calc_ended
	if(Pannel2_1.winfo_children()[2].config()['text'][4] == 'ln'):
		if(value.get() == 0):
			error()
		else:
			value.set(math.log(value.get()))
	else:
		value.set(math.exp(value.get()))
	dot = False
	updatetext()
	calc_ended = True

def inv_func():
	global value, dot
	dot = False
	if(value.get() == 0):
		error()
	value.set(1 / value.get())
	updatetext()

def fact_func():
	global value, dot, calc_ended
	dot = False
	if(int(value.get()) == value.get()):
		value.set(math.factorial(value.get()))
		updatetext()
		calc_ended = True
	else:
		error()

def open_par():
	global value1, value2, value3, value, dot, par, par_value
	dot = False
	if(value1 != None and value2 != None):
		par.append(value1)
		par.append(value2)
		value1 = value2 = None
		par_value += 2
		value.set(0)

def close_par():
	global value1, value2, value3, value, dot, par, par_value
	if(par_value > 0):
		equ_func()
		value2 = par[par_value]
		value1 = par[par_value - 1]
		par_value -= 2
		print("value =",value.get(), " | value1 = ", value1, " | value2 = ", value2, " | value3 = ", value3, " | dot = ", dot, " | par = ", par, " | par_value = ", par_value)		
		equ_func()

def neg_func():
	global value
	value.set(-value.get())
	updatetext()

# Close Button
Close = tkinter.Button(fenetre, text="Fermer", width=6, height=2, command=fenetre.quit)
Close.pack()




# Display Box
Frame0 = tkinter.Frame(fenetre, borderwidth=2, relief=tkinter.GROOVE)
Frame0.pack(side=tkinter.TOP, padx=30, pady=30)
Label0_0 = tkinter.Label(Frame0, width=32, height=2, text=value.get(), anchor=tkinter.E)
Label0_0.pack(side=tkinter.RIGHT, padx=15);


# frame 2
Frame2 = tkinter.Frame(fenetre, borderwidth=2, relief=tkinter.GROOVE)
Frame2.pack(side=tkinter.LEFT, padx=30, pady=30)


# Pannel 2_6
Pannel2_6 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_6.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

base = tkinter.IntVar()
base.set(10)
Pannel2_6.add(tkinter.Radiobutton(Pannel2_6, text='Dec', variable=base, value=10))
Pannel2_6.add(tkinter.Radiobutton(Pannel2_6, text='Bin', variable=base, value=2))
Pannel2_6.add(tkinter.Radiobutton(Pannel2_6, text='Oct', variable=base, value=8))
Pannel2_6.add(tkinter.Radiobutton(Pannel2_6, text='Hexa', variable=base, value=16))


# Pannel 2_5
Pannel2_5 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_5.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel2_5.add(tkinter.Radiobutton(Pannel2_5, width=10, text='RAD', variable=angle, value="rad"))
Pannel2_5.add(tkinter.Radiobutton(Pannel2_5, width=10, text='DEG', variable=angle, value="deg"))


# Pannel 2_0
Pannel2_0 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_0.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel2_0.add(tkinter.Button(Pannel2_0, width=5, height=2, text="2nde", anchor=tkinter.CENTER, command=Seconde_func))
Pannel2_0.add(tkinter.Button(Pannel2_0, width=5, height=2, text="-x", anchor=tkinter.CENTER, command=neg_func))
Pannel2_0.add(tkinter.Button(Pannel2_0, width=5, height=2, text='x!', anchor=tkinter.CENTER, command=fact_func))



# Pannel 2_1
Pannel2_1 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_1.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)
Pannel2_1.add(tkinter.Button(Pannel2_1, width=5, height=2, text='1/x', anchor=tkinter.CENTER, command=inv_func))
Pannel2_1.add(tkinter.Button(Pannel2_1, width=5, height=2, text=sin.get(), anchor=tkinter.CENTER, command=sin_func))
Pannel2_1.add(tkinter.Button(Pannel2_1, width=5, height=2, text=ln.get(), anchor=tkinter.CENTER, command=ln_func))


# Pannel 2_2
Pannel2_2 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_2.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel2_2.add(tkinter.Button(Pannel2_2, width=5, height=2, text='π', anchor=tkinter.CENTER, command=add_pi))
Pannel2_2.add(tkinter.Button(Pannel2_2, width=5, height=2, text=cos.get(), anchor=tkinter.CENTER, command=cos_func))
Pannel2_2.add(tkinter.Button(Pannel2_2, width=5, height=2, text=log.get(), anchor=tkinter.CENTER, command=log_func))


# Pannel 2_3
Pannel2_3 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_3.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel2_3.add(tkinter.Button(Pannel2_3, width=5, height=2, text='e', anchor=tkinter.CENTER, command=add_e))
Pannel2_3.add(tkinter.Button(Pannel2_3, width=5, height=2, text=tan.get(), anchor=tkinter.CENTER, command=tan_func))
Pannel2_3.add(tkinter.Button(Pannel2_3, width=5, height=2, text=sqrt.get(), anchor=tkinter.CENTER, command=sqrt_func))


# Pannel 2_4
Pannel2_4 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_4.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel2_4.add(tkinter.Button(Pannel2_4, width=5, height=2, text=ans.get(), anchor=tkinter.CENTER, command=ans_func))
Pannel2_4.add(tkinter.Button(Pannel2_4, width=5, height=2, text='EXP', anchor=tkinter.CENTER, command=x10_func))
Pannel2_4.add(tkinter.Button(Pannel2_4, width=5, height=2, text=power.get(), anchor=tkinter.CENTER, command=pow_func))





#frame 1
Frame1 = tkinter.Frame(fenetre, borderwidth=2, relief=tkinter.GROOVE)
Frame1.pack(side=tkinter.LEFT, padx=0, pady=30)



# Pannel 1_0
Pannel1_0 = tkinter.PanedWindow(Frame1, orient=tkinter.HORIZONTAL)
Pannel1_0.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel1_0.add(tkinter.Button(Pannel1_0, width=2, height=2, text='(', anchor=tkinter.CENTER, command=open_par))
Pannel1_0.add(tkinter.Button(Pannel1_0, width=2, height=2, text=')', anchor=tkinter.CENTER, command=close_par))
Pannel1_0.add(tkinter.Button(Pannel1_0, width=2, height=2, text='%', anchor=tkinter.CENTER, command=perc_func))
Pannel1_0.add(tkinter.Button(Pannel1_0, width=2, height=2, text='AC', anchor=tkinter.CENTER, command=reset_func))


# Pannel 1_1
Pannel1_1 = tkinter.PanedWindow(Frame1, orient=tkinter.HORIZONTAL)
Pannel1_1.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel1_1.add(tkinter.Button(Pannel1_1, width=2, height=2, text='7', anchor=tkinter.CENTER, command=add_7))
Pannel1_1.add(tkinter.Button(Pannel1_1, width=2, height=2, text='8', anchor=tkinter.CENTER, command=add_8))
Pannel1_1.add(tkinter.Button(Pannel1_1, width=2, height=2, text='9', anchor=tkinter.CENTER, command=add_9))
Pannel1_1.add(tkinter.Button(Pannel1_1, width=2, height=2, text='÷', anchor=tkinter.CENTER, command=div_func))


# Pannel 1_2
Pannel1_2 = tkinter.PanedWindow(Frame1, orient=tkinter.HORIZONTAL)
Pannel1_2.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel1_2.add(tkinter.Button(Pannel1_2, width=2, height=2, text='4', anchor=tkinter.CENTER, command=add_4))
Pannel1_2.add(tkinter.Button(Pannel1_2, width=2, height=2, text='5', anchor=tkinter.CENTER, command=add_5))
Pannel1_2.add(tkinter.Button(Pannel1_2, width=2, height=2, text='6', anchor=tkinter.CENTER, command=add_6))
Pannel1_2.add(tkinter.Button(Pannel1_2, width=2, height=2, text='×', anchor=tkinter.CENTER, command=mult_func))


# Pannel 1_3
Pannel1_3 = tkinter.PanedWindow(Frame1, orient=tkinter.HORIZONTAL)
Pannel1_3.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel1_3.add(tkinter.Button(Pannel1_3, width=2, height=2, text='1', anchor=tkinter.CENTER, command=add_1))
Pannel1_3.add(tkinter.Button(Pannel1_3, width=2, height=2, text='2', anchor=tkinter.CENTER, command=add_2))
Pannel1_3.add(tkinter.Button(Pannel1_3, width=2, height=2, text='3', anchor=tkinter.CENTER, command=add_3))
Pannel1_3.add(tkinter.Button(Pannel1_3, width=2, height=2, text='-', anchor=tkinter.CENTER, command=sub_func))




# Pannel 1_4
Pannel1_4 = tkinter.PanedWindow(Frame1, orient=tkinter.HORIZONTAL)
Pannel1_4.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel1_4.add(tkinter.Button(Pannel1_4, width=2, height=2, text='0', anchor=tkinter.CENTER, command=add_0))
Pannel1_4.add(tkinter.Button(Pannel1_4, width=2, height=2, text='.', anchor=tkinter.CENTER, command=add_coma))
Pannel1_4.add(tkinter.Button(Pannel1_4, width=2, height=2, text='=', anchor=tkinter.CENTER, command=equ_func))
Pannel1_4.add(tkinter.Button(Pannel1_4, width=2, height=2, text='+', anchor=tkinter.CENTER, command=add_func))



Frame3 = tkinter.Frame(fenetre, borderwidth=2, relief=tkinter.GROOVE)
Frame3.pack(side=tkinter.LEFT, padx=15, pady=30)


def test():
	print("test")
#KeyEvent
def key(event):
	key_pressed = {
	21 : equ_func,
	36 : equ_func,
	104 : equ_func,
	90 : add_0,
	87 : add_1,
	88 : add_2,
	89 : add_3,
	83 : add_4,
	84 : add_5,
	85 : add_6,
	79 : add_7,
	80 : add_8,
	81 : add_9,
	91 : add_coma,
	86 : add_func,
	82 : sub_func,
	63 : mult_func,
	106 : div_func,
	18 : pow_func,
	48 : perc_func,
	61 : fact_func,
	14 : open_par,
	20 : close_par
	}.get(event.keycode, None)
	if(key_pressed != None):
		key_pressed()

fenetre.bind("<Key>", key)

fenetre.mainloop()