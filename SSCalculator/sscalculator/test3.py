#!/usr/bin/python3
#from tkinter import * 
import tkinter
import time
import math
import random


dot = False
Seconde = False
calc_ended = True
value = '0'
value1 = None
value2 = None
value3 = None
par = []
par_value = -1
fenetre = tkinter.Tk()
displayValue = tkinter.StringVar()
sin = tkinter.StringVar()
cos = tkinter.StringVar()
tan = tkinter.StringVar()
ln = tkinter.StringVar()
log = tkinter.StringVar()
sqrt = tkinter.StringVar()
power = tkinter.StringVar()
ans = tkinter.StringVar()
angle = tkinter.StringVar()
fromBase = tkinter.StringVar()
toBase = tkinter.StringVar()

displayValue.set("0")
sin.set('sin')
cos.set('cos')
tan.set('tan')
ln.set('ln')
log.set('log')
sqrt.set('√')
power.set('x^y')
ans.set('Ans')
angle.set("rad")
fromBase.set("dec")
toBase.set("dec")

def convertValue(value, toBase):
	if(toBase.get() == "dec"):
		return(str(value))
	if(toBase.get() == "bin"):
		return(bin(value)[2:] if (int(value) >= 0) else "-" + bin(-int(value))[2:])
	if(toBase.get() == "oct"):
		return(oct(value)[2:] if (int(value) >= 0) else "-" + oct(-int(value))[2:])
	if(toBase.get() == "hex"):
		return(hex(value)[2:] if (int(value) >= 0) else "-" + hex(-int(value))[2:])

def updateFromBase(value):
	if(fromBase.get() == "bin"):
		Pannel1_Hex2.pack_forget()
		Pannel1_Hex1.pack_forget()
		Pannel1_3.winfo_children()[1].config(state=tkinter.DISABLED)
		Pannel1_3.winfo_children()[2].config(state=tkinter.DISABLED)
		Pannel1_2.winfo_children()[0].config(state=tkinter.DISABLED)
		Pannel1_2.winfo_children()[1].config(state=tkinter.DISABLED)
		Pannel1_2.winfo_children()[2].config(state=tkinter.DISABLED)
		Pannel1_1.winfo_children()[0].config(state=tkinter.DISABLED)
		Pannel1_1.winfo_children()[1].config(state=tkinter.DISABLED)
		Pannel1_1.winfo_children()[2].config(state=tkinter.DISABLED)
	if(fromBase.get() == "oct"):
		Pannel1_Hex2.pack_forget()
		Pannel1_Hex1.pack_forget()
		Pannel1_3.winfo_children()[1].config(state=tkinter.NORMAL)
		Pannel1_3.winfo_children()[2].config(state=tkinter.NORMAL)
		Pannel1_2.winfo_children()[0].config(state=tkinter.NORMAL)
		Pannel1_2.winfo_children()[1].config(state=tkinter.NORMAL)
		Pannel1_2.winfo_children()[2].config(state=tkinter.NORMAL)
		Pannel1_1.winfo_children()[0].config(state=tkinter.NORMAL)
		Pannel1_1.winfo_children()[1].config(state=tkinter.DISABLED)
		Pannel1_1.winfo_children()[2].config(state=tkinter.DISABLED)
	if(fromBase.get() == "dec"):
		Pannel1_Hex2.pack_forget()
		Pannel1_Hex1.pack_forget()
		Pannel1_3.winfo_children()[1].config(state=tkinter.NORMAL)
		Pannel1_3.winfo_children()[2].config(state=tkinter.NORMAL)
		Pannel1_2.winfo_children()[0].config(state=tkinter.NORMAL)
		Pannel1_2.winfo_children()[1].config(state=tkinter.NORMAL)
		Pannel1_2.winfo_children()[2].config(state=tkinter.NORMAL)
		Pannel1_1.winfo_children()[0].config(state=tkinter.NORMAL)
		Pannel1_1.winfo_children()[1].config(state=tkinter.NORMAL)
		Pannel1_1.winfo_children()[2].config(state=tkinter.NORMAL)
	if(fromBase.get() == "hex"):
		Pannel1_1.pack_forget()
		Pannel1_2.pack_forget()
		Pannel1_3.pack_forget()
		Pannel1_4.pack_forget()
		Pannel1_3.winfo_children()[1].config(state=tkinter.NORMAL)
		Pannel1_3.winfo_children()[2].config(state=tkinter.NORMAL)
		Pannel1_2.winfo_children()[0].config(state=tkinter.NORMAL)
		Pannel1_2.winfo_children()[1].config(state=tkinter.NORMAL)
		Pannel1_2.winfo_children()[2].config(state=tkinter.NORMAL)
		Pannel1_1.winfo_children()[0].config(state=tkinter.NORMAL)
		Pannel1_1.winfo_children()[1].config(state=tkinter.NORMAL)
		Pannel1_1.winfo_children()[2].config(state=tkinter.NORMAL)
		Pannel1_Hex2.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)
		Pannel1_Hex1.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)
		Pannel1_1.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)
		Pannel1_2.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)
		Pannel1_3.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)
		Pannel1_4.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

def updatetext(value):
	global Seconde, calc_ended, displayValue, toBase
	displayValue.set(convertValue(int(value), toBase).upper())
	Label0_0.config(text = displayValue.get())
	if(Seconde == True):
		Seconde_func()
	calc_ended = False

def updateDisplay(event):
	global value
	if(fromBase.get() != Label0_3.config()['text'][4]):
		updateFromBase(value)
	if(toBase.get() != Label0_5.config()['text'][4]):
		updatetext(value)
	Label0_1.config(text = angle.get())
	Label0_3.config(text = fromBase.get())
	Label0_5.config(text = toBase.get())

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
	value = 'ERROR'
	updatetext(value)


def add_0():
	global dot, calc_ended, value
	value = ('0' if(calc_ended == True or value == '0') else value + '0')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_1():
	global dot, calc_ended, value
	value = ('1' if(calc_ended == True or value == '0') else value + '1')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_2():
	global dot, calc_ended, value
	value = ('2' if(calc_ended == True or value == '0') else value + '2')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_3():
	global dot, calc_ended, value
	value = ('3' if(calc_ended == True or value == '0') else value + '3')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_4():
	global dot, calc_ended, value
	value = ('4' if(calc_ended == True or value == '0') else value + '4')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_5():
	global dot, calc_ended, value
	value = ('5' if(calc_ended == True or value == '0') else value + '5')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_6():
	global dot, calc_ended, value
	value = ('6' if(calc_ended == True or value == '0') else value + '6')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_7():
	global dot, calc_ended, value
	value = ('7' if(calc_ended == True or value == '0') else value + '7')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_8():
	global dot, calc_ended, value
	value = ('8' if(calc_ended == True or value == '0') else value + '8')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_9():
	global dot, calc_ended, value
	value = ('9' if(calc_ended == True or value == '0') else value + '9')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_A():
	global dot, calc_ended, value
	value = ('A' if(calc_ended == True or value == '0') else value + 'A')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_B():
	global dot, calc_ended, value
	value = ('B' if(calc_ended == True or value == '0') else value + 'B')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_C():
	global dot, calc_ended, value
	value = ('C' if(calc_ended == True or value == '0') else value + 'C')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_D():
	global dot, calc_ended, value
	value = ('D' if(calc_ended == True or value == '0') else value + 'D')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_E():
	global dot, calc_ended, value
	value = ('E' if(calc_ended == True or value == '0') else value + 'E')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);
def add_F():
	global dot, calc_ended, value
	value = ('F' if(calc_ended == True or value == '0') else value + 'F')
	dot = dot-1 if(dot != False) else dot
	updatetext(value);

def add_pi():
	global calc_ended, value
	if(value == 0):
		value = math.pi
	else:
		value = value * math.pi
	updatetext(value);
	calc_ended = True

def add_e():
	global calc_ended, value
	if(value == 0):
		value = math.exp(1)
	else:
		value = value * math.exp(1)
	updatetext(value);
	calc_ended = True

def reset_func():
	global value1, value2, value3, value, dot, calc_ended
	value1 = None
	value2 = None
	value = tkinter.DoubleVar()
	value = '0'
	dot = False
	updatetext(value)
	calc_ended = True

def equ_func():
	global value1, value2, value3, value, dot, calc_ended
	if(value1 != None and value2 != None):
		if(value2 == "+"):
			value = str(int(value1, fromBase.get()) + int(value, fromBase.get()))
		if(value2 == "-"):
			value = str(int(value1, fromBase.get()) - int(value, fromBase.get()))
		if(value2  == "*"):
			value = str(int(value1, fromBase.get()) * int(value, fromBase.get()))
		if(value2  == "/"):
			if(int(value) == 0):
				error()
			else:
				value = str(int(value1) / int(value))
		if(value2 == "^"):
			value = str(math.pow(int(value1), int(value)))
		if(value2 == "√"):
			value = str(math.pow(int(value1), (1 / int(value))))
		if(value2 == 'x10'):
			value = str(int(value1) * math.pow(10, int(value)))
		value1 = None
		value2 = None
		value3 = value
		updatetext(value)
		calc_ended = True


def add_func():
	global value1, value2, value3, dot, value
	if(value1 != None):
		equ_func()
	value1 = value
	value2 = "+"
	value = '0'
	dot = False


def sub_func():
	global value1, value2, value3, dot, value
	if(value1 != None):
		equ_func()
	value1 = value
	value2 = "-"
	value = '0'
	dot = False


def mult_func():
	global value1, value2, value3, dot, value
	if(value1 != None):
		equ_func()
	value1 = value
	value2 = "*"
	value = '0'
	dot = False


def div_func():
	global value1, value2, value3, dot, value
	if(value1 == None):
		equ_func()
	value1 = value;
	value2 = '/'
	value = '0'
	dot = False

def pow_func():
	global value1, value2, value3, dot, value
	if(Pannel2_4.winfo_children()[2].config()['text'][4] == 'x^y'):
		if(value1 == None):
			equ_func()
		value1 = value
		value2 = "^"
	else:
		if(value1 == None):
			equ_func()
		value1 = value
		value2 = "√"
	value = '0'
	dot = False


def perc_func():
	global value, calc_ended
	if(value > 1):
		error()
	else:
		value = str(int(value * 100))
		updatetext(value)
		value = value  + "%"
		calc_ended = True

def add_coma():
	global dot, value
	dot = -1

def ans_func():
	global value3, value, dot, calc_ended
	if(Pannel2_4.winfo_children()[2].config()['text'][4] == 'Ans'):
		value = value3
	else:
		if(value == 0):
			value = str(random.random())
		else:
			value = str(int(value) * random.random())
	dot = False
	updatetext(value)
	calc_ended = True

def sqrt_func():
	global value, dot, calc_ended
	if(Pannel2_3.winfo_children()[2].config()['text'][4] == '√'):
		value = str(math.sqrt(int(value)))
	else:
		value = str(math.pow(int(value), 2))
	dot = False
	updatetext(value)
	calc_ended = True

def tan_func():
	global value, dot, angle, calc_ended
	if(Pannel2_3.winfo_children()[1].config()['text'][4] == 'tan'):
		if(int(value)%math.pi == math.pi/2):
			error()
		else:
			value = str(math.tan(int(value))) if(angle.get() == "rad") else str(math.tan(math.radians(int(value))))
	else:
		value = str(math.atan(int(value))) if (angle.get() == "rad") else str(math.degrees(math.atan(int(value))))
	dot = False
	updatetext(value)
	calc_ended = True

def x10_func():
	global value1, value2, value, dot, value
	dot = False
	value1 = value
	value2 = 'x10'
	value = '0'

def log_func():
	global value, dot, calc_ended
	if(Pannel2_2.winfo_children()[2].config()['text'][4] == 'log'):
		if(value == 0):
			error()
		else:
			value = math.log(value, 10)
			updatetext(value)
			calc_ended = True
	else:
		value = math.pow(10, value)
		updatetext(value)
		calc_ended = True
	dot = False

def cos_func():
	global value, dot, calc_ended
	if(Pannel2_2.winfo_children()[1].config()['text'][4] == 'cos'):
		value = math.cos(value) if(angle.get() == "rad") else math.cos(math.radians(value))
	else:
		value = math.acos(value) if(angle.get() == "rad") else math.degrees(math.acos(value))
	dot = False
	updatetext(value)
	calc_ended = True

def sin_func():
	global value, dot, calc_ended
	if(Pannel2_1.winfo_children()[1].config()['text'][4] == 'sin'):
		value = math.sin(value) if(angle.get() == "rad") else math.sin(math.radians(value))
	else:
		value = math.asin(value) if(angle.get() == "rad") else math.degrees(math.asin(value))
	dot = False
	updatetext(value)
	calc_ended = True

def ln_func():
	global value, dot, calc_ended
	if(Pannel2_1.winfo_children()[2].config()['text'][4] == 'ln'):
		if(value == 0):
			error()
		else:
			value = math.log(value)
	else:
		value = math.exp(value)
	dot = False
	updatetext(value)
	calc_ended = True

def inv_func():
	global value, dot
	dot = False
	if(value == 0):
		error()
	value = 1 / value
	updatetext(value)

def fact_func():
	global value, dot, calc_ended
	dot = False
	if(int(value) == value):
		value = math.factorial(value)
		updatetext(value)
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
		value = '0'

def close_par():
	global value1, value2, value3, value, dot, par, par_value
	if(par_value > 0):
		equ_func()
		value2 = par[par_value]
		value1 = par[par_value - 1]
		par_value -= 2
		equ_func()

def neg_func():
	global value
	value = -value
	updatetext(value)

# Close Button
Close = tkinter.Button(fenetre, text="Fermer", width=6, height=2, command=fenetre.quit)
Close.pack()




# Display Box
Frame0 = tkinter.Frame(fenetre, borderwidth=2, relief=tkinter.GROOVE)
Frame0.pack(side=tkinter.TOP, padx=30, pady=30)
Label0_0 = tkinter.Label(Frame0, width=32, height=2, text=displayValue.get(), anchor=tkinter.E)
Label0_1 = tkinter.Label(Frame0, width=5, height=1, text=angle.get(), anchor= tkinter.NE)
Label0_2 = (tkinter.Label(Frame0, width=4, height=1, text="from", anchor= tkinter.W))
Label0_3 = (tkinter.Label(Frame0, fg='red', width=3, height=1, text=fromBase.get(), anchor= tkinter.W))
Label0_4 = (tkinter.Label(Frame0, width=2, height=1, text="to", anchor= tkinter.W))
Label0_5 = (tkinter.Label(Frame0, fg='blue', width=3, height=1, text=toBase.get(), anchor= tkinter.W))
Label0_0.pack(side=tkinter.RIGHT, padx=15);
Label0_1.pack(side=tkinter.TOP, padx=0);
Label0_2.pack(side=tkinter.LEFT, padx=0, pady=0);
Label0_3.pack(side=tkinter.LEFT, padx=0, pady=0);
Label0_4.pack(side=tkinter.LEFT, padx=0, pady=0);
Label0_5.pack(side=tkinter.LEFT, padx=0, pady=0);


# frame 2
Frame2 = tkinter.Frame(fenetre, borderwidth=2, relief=tkinter.GROOVE)
Frame2.pack(side=tkinter.LEFT, padx=30, pady=30)


# Pannel 2_7
Pannel2_7 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_7.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel2_7.add(tkinter.Radiobutton(Pannel2_7, fg='red', text='Dec', variable=fromBase, value="dec"))
Pannel2_7.add(tkinter.Radiobutton(Pannel2_7, fg='red', text='Bin', variable=fromBase, value="bin"))
Pannel2_7.add(tkinter.Radiobutton(Pannel2_7, fg='red', text='Oct', variable=fromBase, value="oct"))
Pannel2_7.add(tkinter.Radiobutton(Pannel2_7, fg='red', text='Hex', variable=fromBase, value="hex"))


# Pannel 2_6
Pannel2_6 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_6.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel2_6.add(tkinter.Radiobutton(Pannel2_6, fg='blue', text='Dec', variable=toBase, value="dec"))
Pannel2_6.add(tkinter.Radiobutton(Pannel2_6, fg='blue', text='Bin', variable=toBase, value="bin"))
Pannel2_6.add(tkinter.Radiobutton(Pannel2_6, fg='blue', text='Oct', variable=toBase, value="oct"))
Pannel2_6.add(tkinter.Radiobutton(Pannel2_6, fg='blue', text='Hex', variable=toBase, value="hex"))


# Pannel 2_5
Pannel2_5 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_5.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel2_5.add(tkinter.Radiobutton(Pannel2_5, width=10, text='RAD', variable=angle, value="rad"))
Pannel2_5.add(tkinter.Radiobutton(Pannel2_5, width=10, text='DEG', variable=angle, value="deg"))


# Pannel 2_0
Pannel2_0 = tkinter.PanedWindow(Frame2, orient=tkinter.HORIZONTAL)
Pannel2_0.pack(side=tkinter.TOP, expand=tkinter.Y, fill=tkinter.BOTH, pady=2, padx=2)

Pannel2_0.add(tkinter.Button(Pannel2_0, width=5, height=2, text="2nde", anchor=tkinter.CENTER, command=Seconde_func))
Pannel2_0.add(tkinter.Button(Pannel2_0, width=5, height=2, text="- x", anchor=tkinter.CENTER, command=neg_func))
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
Pannel1_Hex2 = tkinter.PanedWindow(Frame1, orient=tkinter.HORIZONTAL)

Pannel1_Hex2.add(tkinter.Button(Pannel1_Hex2, width=2, height=2, text='A', anchor=tkinter.CENTER, command=add_A))
Pannel1_Hex2.add(tkinter.Button(Pannel1_Hex2, width=2, height=2, text='B', anchor=tkinter.CENTER, command=add_B))
Pannel1_Hex2.add(tkinter.Button(Pannel1_Hex2, width=2, height=2, text='C', anchor=tkinter.CENTER, command=add_C))
Pannel1_Hex2.add(tkinter.Label(Pannel1_Hex2, width=2, height=2, text='', anchor=tkinter.CENTER))


# Pannel 1_Hex2
Pannel1_Hex1 = tkinter.PanedWindow(Frame1, orient=tkinter.HORIZONTAL)

Pannel1_Hex1.add(tkinter.Button(Pannel1_Hex1, width=2, height=2, text='D', anchor=tkinter.CENTER, command=add_D))
Pannel1_Hex1.add(tkinter.Button(Pannel1_Hex1, width=2, height=2, text='E', anchor=tkinter.CENTER, command=add_E))
Pannel1_Hex1.add(tkinter.Button(Pannel1_Hex1, width=2, height=2, text='F', anchor=tkinter.CENTER, command=add_F))
Pannel1_Hex1.add(tkinter.Label(Pannel1_Hex1, width=2, height=2, text='', anchor=tkinter.CENTER))


# Pannel 1_Hex1
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
fenetre.bind("<Button-1>", updateDisplay)

fenetre.mainloop()