import tkinter
from tkinter import *

root=Tk()
root.configure(bg="teal")
root.geometry("400x400")

def topwin():
    top=Toplevel()
    top.configure(bg="seagreen")
    top.geometry("100x100")
    label=Label(top,text="This is the toplevel window!")
    label.pack()

label2=Label(root,text="This is the main window!")
label2.pack()
button=Button(root,text="Click Me!",command=topwin)
button.pack()

root.mainloop()