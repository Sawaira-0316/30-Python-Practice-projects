from tkinter import Tk, Label, Entry, Button
from textblob import TextBlob

def correct_spelling():
    get_data = entry1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    entry2.delete(0, 'end')
    entry2.insert(0, data)

win = Tk()
win.geometry("500x400")
win.config(bg="blue")

label1 = Label(win, text="Incomplete spelling", font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
label1.place(x=50, y=20, height=30, width=400)

entry1 = Entry(win, font=("Times New Roman", 25))
entry1.place(x=50, y=60, height=50, width=400)

label2 = Label(win, text="Correct spelling", font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
label2.place(x=50, y=130, height=30, width=400)

entry2 = Entry(win, font=("Times New Roman", 25))
entry2.place(x=50, y=170, height=50, width=400)

button = Button(win, text="Done", font=("Times New Roman", 25, "bold"), bg="yellow", command=correct_spelling)
button.place(x=200, y=260, height=50, width=100)

win.mainloop()