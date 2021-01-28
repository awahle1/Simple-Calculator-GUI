from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

first = 0
delete = False
add = 0
just_pressed = False

def button_click(number):
	global delete
	global second
	global just_pressed
	just_pressed = False
	if delete:
		e.delete(0, END)
		delete = False
	current = e.get()
	e.delete(0, END)
	print(f"current:{current}, number:{number}")
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_plus():
	global delete
	global first
	first = e.get()
	delete = True


def button_equals():
	global first
	global add
	global just_pressed
	if not(just_pressed):
		add = e.get()
	sum= int(first) + int(add)
	first = sum
	just_pressed = True


	e.delete(0, END)
	e.insert(0, str(sum))



nine = Button(root, text="9", padx=40, pady=20, command= lambda: button_click(9)).grid(row=1, column=2)
eight = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=1, column=1)
seven = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=1, column=0)

six = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=2, column=2)
five = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=2, column=1)
four = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=2, column=0)

three = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=3, column=2)
two = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=3, column=1)
one = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=3, column=0)

zero = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0)).grid(row=4, column=0)

plus = Button(root, text="+", padx=39, pady=20, command=button_plus).grid(row=5, column=0)
clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear).grid(row=4, column=1, columnspan=2)
equals = Button(root, text="=", padx=91, pady=20, command=button_equals).grid(row=5, column=1, columnspan=2)




root.mainloop()