from tkinter import *

root = Tk()


def myClick():
	myLabel = Label(root, text="Look! I clicked")
	myLabel.pack()


myButton = Button(root, text="button", command=myClick)

myButton.pack()

root.mainloop()