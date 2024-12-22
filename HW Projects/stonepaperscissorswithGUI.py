import tkinter
from tkinter import *
from tkinter import messagebox
import random
up=0
cp=0
comp=["Stone","Paper","Scissors"]
comcho=random.choice(comp)

def tieMsg():
    mbox=messagebox.showinfo("It is a tie!")
    if mbox=="ok":
        reset()

def comMsg():
    mbox=messagebox.showinfo("Computer wins!")
    if mbox=="ok":
        reset()

def userMsg():
    mbox=messagebox.showinfo("User wins!")
    if mbox=="ok":
        reset()   

def reset():
    exit()

def sto():
    cop=Label(root,text=comcho)
    cop.place(x=150,y=180)
    if comcho=="Stone":
        tieMsg()
        cop.destroy()
    elif comcho=="Paper":
        comMsg()
        cop.destroy()
    else:
        userMsg()
        cop.destroy()

def pap():
    cop=Label(root,text=comcho)
    cop.place(x=150,y=180)
    if comcho=="Stone":
        userMsg()
        cop.destroy()
    elif comcho=="Paper":
        tieMsg()
        cop.destroy()
    else:
        comMsg()
        cop.destroy()

def sci():
    cop=Label(root,text=comcho)
    cop.place(x=150,y=180)
    if comcho=="Stone":
        comMsg()
        cop.destroy()
    elif comcho=="Paper":
        userMsg()
        cop.destroy()
    else:
        tieMsg()
        cop.destroy()


root=Tk()
root.title("Stone Paper Scissors Shoot!")
root.geometry("400x400")
root.configure(bg="teal")

l1=Label(root,text="Lets Play!",relief="raised")
l1.pack()
bl1=Label(root,bg="teal")
bl1.pack()
b1=Button(root,text="Stone",bg="grey",command=sto)
b2=Button(root,text="Paper",bg="azure",command=pap)
b3=Button(root,text="Scissors",bg="red",command=sci)
b1.place(x=90,y=50)
b2.place(x=180,y=50)
b3.place(x=270,y=50)

root.mainloop()