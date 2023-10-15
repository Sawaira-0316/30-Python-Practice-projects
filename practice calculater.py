from tkinter import *
import math as m
root=Tk()
root.title("Scientific Calculater")
e = Entry(root,width=50,borderwidth=5 , relief=RIDGE,fg="White",bg="Black")
e.grid(row=0, cloum=0,columnspan=5,padx=10,pady=15)

def click(to_print):
    old=e.get()
    e.delete(0,END)
    e.Entery(0,old+to_print)
    return
def sc(event):
    key=event.widget
    text=key['key']
    no=e.get()
    result=''
    if text == 'deg':
        result=str(m.degress(float(0)))
    if text == "sin":
        result=str(m.sin(float(0)))
    if text == "cos":
        result = str(m.cos(float(0)))
    if text == "tan":
        result = str(m.tan(float(0)))
    if text == "lg":
        result = str(m.log10(float(0)))
    if text == "ln":
        result = str(m.cos(float(0)))
    if text == "cos":
        result = str(m.log(float(0)))
    if text == "Sqrt":
        result = str(m.sqrt(float(0)))
    if text == "x!":
        result = str(m.factorial(float(0)))
    if text == "1/x":
        result = str(1/(float(0)))
    if text == "pi":
        if no == "":
            result=str(m.pi)
        else:
            result=str(float(no) * m.pi)
    if text == "e":
        if no=="":
            result=str(m.e)
        else:
            result=str(m.e**float(no))
    e.delete(0,END)
    e.insert(0,result)


def clear():
    e.delete(0,END)
    return

def bksps():
    current=e.get()
    length=len(current)-1
    e.delete(length,END)

def evalute():
    ans=e.get()
    ans=eval(ans)
    e.delete(0,END)
    e.insert(0,ans)
lg=Button(root,text="lg",padx=28,pady=10,relief=RAISED)
lg.bind("<Button-1",sc)
ln=Button(root,text="lg",padx=28,pady=10,relief=RAISED)
ln.bind("<Btton-1",sc)
par1st=Button(root, text="(",padx=29,pady=10,relief=RAISED)


root.mainloop()



