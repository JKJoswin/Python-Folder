import tkinter
from tkinter import *
from tkinter import messagebox

root=Tk()
root.configure(bg="teal")
root.geometry("400x400")

def msg_box():
    msg=messagebox.showwarning("Virus Alert!","Check!")

button1=Button(root,text="Click me!",command=msg_box)
button1.place(x=200,y=200)

root.mainloop()