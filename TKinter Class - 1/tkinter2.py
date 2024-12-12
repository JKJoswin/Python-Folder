import tkinter
from tkinter import *
window1=Tk()
window1.title("Hello World!")
window1.geometry('400x300')

t=1
for i in range(1,4):
    window1.rowconfigure(i,weight=0,minsize=100)
    for j in range(1,4):
        window1.columnconfigure(j,weight=0,minsize=50)
        label=Label(window1,relief="sunken",fg="white",bg="black",text=t,width=2)
        t+=1
        label.grid(row=i,column=j)

window1.mainloop()