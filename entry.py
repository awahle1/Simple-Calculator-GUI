from tkinter import *

root = Tk()


e = Entry(root, width=50)
e.pack()

def myClick():
	myLabel = Label(root, text="Look! I clicked")
	myLabel.pack()


myButton = Button(root, text="button", command=myClick)

myButton.pack()

root.mainloop()