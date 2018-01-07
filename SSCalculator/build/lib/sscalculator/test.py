print(int("10", 2))
print(bin(2)[2:])
print(oct(8)[2:])
print(hex(16)[2:])
"""
from tkinter import *

root = Tk()

def key(event):
	print("pressed", repr(event.char), event.keycode, type(event.keycode))

def callback(event):
	frame.focus_set()
	print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
"""