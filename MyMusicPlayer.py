from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter import Tk, Label, PhotoImage

root = Tk()
root.title("My Pizza Window")

pizza = PhotoImage(file='')
label = Label(root, image=pizza)
label.pack()

root.mainloop()
