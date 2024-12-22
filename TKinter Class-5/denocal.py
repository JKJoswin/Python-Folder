import tkinter
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Denomination Calculation")
root.geometry("400x400")
root.configure(bg="azure")

def topwin():
    def calculate():
        global amount
        amount=int(entry1.get())
        note2000=amount//2000
        amount=amount%2000
        note500=amount//500
        amount=amount%500
        note100=amount//100
        amount=amount%100
        e1.insert(END,str(note2000))
        e2.insert(END,str(note500))
        e3.insert(END,str(note100))

    print("ok")
    top=Toplevel()
    top.title("Toplevel window")
    top.geometry("300x300")

    label2=Label(top,text="Enter the amount")
    entry1=Entry(top)
    label2.place(x=20,y=50)
    entry1.place(x=100,y=50)
    label3=Label(top,text="Here are the number of notes of denomination")
    button3=Button(top,text="Calculate",command=calculate)
    button3.place(x=20,y=70)
    label3.place(x=20,y=90)
    l1=Label(top,text="2000")
    l2=Label(top,text="500")
    l3=Label(top,text="100")

    e1=Entry(top)
    e2=Entry(top)
    e3=Entry(top)

    l1.place(x=20,y=110)
    l2.place(x=20,y=130)
    l3.place(x=20,y=150)

    e1.place(x=100,y=110)
    e2.place(x=100,y=130)
    e3.place(x=100,y=150)

def message():
    mbox=messagebox.showinfo("Alert!","Do you want to calculate?")
    if mbox=="ok":
        topwin()

label1=Label(root,text="Welcome to denomination calculator")
button1=Button(root,text="Click Me",command=message)
label1.place(x=150,y=200)
button1.place(x=150,y=220)

root.mainloop()