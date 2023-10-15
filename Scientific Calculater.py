from tkinter import *
import math as m

root = Tk()
root.title("Scientific Calculator")
e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old + to_print)


def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result = ''

    if text == 'deg':
        result = str(m.degrees(float(no)))
    elif text == "sin":
        result = str(m.sin(float(no)))
    elif text == "cos":
        result = str(m.cos(float(no)))
    elif text == "tan":
        result = str(m.tan(float(no)))
    elif text == "lg":
        result = str(m.log10(float(no)))
    elif text == "ln":
        result = str(m.log(float(no)))
    elif text == "sqrt":
        result = str(m.sqrt(float(no)))
    elif text == "x!":
        result = str(m.factorial(float(no)))
    elif text == "1/x":
        result = str(1 / float(no))
    elif text == "pi":
        if no == "":
            result = str(m.pi)
        else:
            result = str(float(no) * m.pi)
    elif text == "e":
        if no == "":
            result = str(m.e)
        else:
            result = str(m.e ** float(no))

    e.delete(0, END)
    e.insert(0, result)


def clear():
    e.delete(0, END)


def bksps():
    current = e.get()
    length = len(current) - 1
    e.delete(length, END)


def evaluate():
    ans = e.get()
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)


# Buttons
lg = Button(root, text="lg", padx=28, pady=10, relief=RAISED)
lg.bind("<Button-1>", sc)
lg.grid(row=1, column=0)

ln = Button(root, text="ln", padx=28, pady=10, relief=RAISED)
ln.bind("<Button-1>", sc)
ln.grid(row=1, column=1)

par1st = Button(root, text="(", padx=29, pady=10, relief=RAISED)
par1st.bind("<Button-1>", sc)
par1st.grid(row=1, column=2)

par2nd = Button(root, text=")", padx=29, pady=10, relief=RAISED)
par2nd.bind("<Button-1>", sc)
par2nd.grid(row=1, column=3)

sin = Button(root, text="sin", padx=25, pady=10, relief=RAISED)
sin.bind("<Button-1>", sc)
sin.grid(row=2, column=0)

cos = Button(root, text="cos", padx=24, pady=10, relief=RAISED)
cos.bind("<Button-1>", sc)
cos.grid(row=2, column=1)

tan = Button(root, text="tan", padx=24, pady=10, relief=RAISED)
tan.bind("<Button-1>", sc)
tan.grid(row=2, column=2)

sqrt = Button(root, text="sqrt", padx=22, pady=10, relief=RAISED)
sqrt.bind("<Button-1>", sc)
sqrt.grid(row=2, column=3)

ln = Button(root, text="ln", padx=28, pady=10, relief=RAISED)
ln.bind("<Button-1>", sc)
ln.grid(row=3, column=0)

log = Button(root, text="log", padx=26, pady=10, relief=RAISED)
log.bind("<Button-1>", sc)
log.grid(row=3, column=1)

exp = Button(root, text="exp", padx=26, pady=10, relief=RAISED)
exp.bind("<Button-1>", sc)
exp.grid(row=3, column=2)

factorial = Button(root, text="x!", padx=27, pady=10, relief=RAISED)
factorial.bind("<Button-1>", sc)
factorial.grid(row=3, column=3)

btn_pi = Button(root, text="pi", padx=29, pady=10, relief=RAISED)
btn_pi.bind("<Button-1>", sc)
btn_pi.grid(row=4, column=0)

btn_e = Button(root, text="e", padx=30, pady=10, relief=RAISED)
btn_e.bind("<Button-1>", sc)
btn_e.grid(row=4, column=1)

btn_square = Button(root, text="^2", padx=26, pady=10, relief=RAISED)
btn_square.bind("<Button-1>", sc)
btn_square.grid(row=4, column=2)

btn_cubic = Button(root, text="^3", padx=26, pady=10, relief=RAISED)
btn_cubic.bind("<Button-1>", sc)
btn_cubic.grid(row=4, column=3)

btn_1 = Button(root, text="1", padx=30, pady=10, relief=RAISED, command=lambda: click("1"))
btn_2 = Button(root, text="2", padx=30, pady=10, relief=RAISED, command=lambda: click("2"))
btn_3 = Button(root, text="3", padx=30, pady=10, relief=RAISED, command=lambda: click("3"))
btn_4 = Button(root, text="4", padx=30, pady=10, relief=RAISED, command=lambda: click("4"))
btn_5 = Button(root, text="5", padx=30, pady=10, relief=RAISED, command=lambda: click("5"))
btn_6 = Button(root, text="6", padx=30, pady=10, relief=RAISED, command=lambda: click("6"))
btn_7 = Button(root, text="7", padx=30, pady=10, relief=RAISED, command=lambda: click("7"))
btn_8 = Button(root, text="8", padx=30, pady=10, relief=RAISED, command=lambda: click("8"))
btn_9 = Button(root, text="9", padx=30, pady=10, relief=RAISED, command=lambda: click("9"))
btn_0 = Button(root, text="0", padx=30, pady=10, relief=RAISED, command=lambda: click("0"))

btn_1.grid(row=5, column=0)
btn_2.grid(row=5, column=1)
btn_3.grid(row=5, column=2)
btn_4.grid(row=6, column=0)
btn_5.grid(row=6, column=1)
btn_6.grid(row=6, column=2)
btn_7.grid(row=7, column=0)
btn_8.grid(row=7, column=1)
btn_9.grid(row=7, column=2)
btn_0.grid(row=8, column=0)

btn_plus = Button(root, text="+", padx=29, pady=10, relief=RAISED, command=lambda: click("+"))
btn_minus = Button(root, text="-", padx=31, pady=10, relief=RAISED, command=lambda: click("-"))
btn_multiply = Button(root, text="*", padx=30, pady=10, relief=RAISED, command=lambda: click("*"))
btn_divide = Button(root, text="/", padx=31, pady=10, relief=RAISED, command=lambda: click("/"))
btn_decimal = Button(root, text=".", padx=31, pady=10, relief=RAISED, command=lambda: click("."))
btn_clear = Button(root, text="C", padx=29, pady=10, relief=RAISED, command=clear)
btn_equals = Button(root, text="=", padx=66, pady=10, relief=RAISED, command=evaluate)

btn_plus.grid(row=5, column=3)
btn_minus.grid(row=6, column=3)
btn_multiply.grid(row=7, column=3)
btn_divide.grid(row=8, column=3)
btn_decimal.grid(row=8, column=1)
btn_clear.grid(row=8, column=2, columnspan=2)
btn_equals.grid(row=9, column=0, columnspan=4)

root.mainloop()

