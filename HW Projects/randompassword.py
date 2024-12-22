import tkinter
from tkinter import *
import random

win=Tk()
win.title("Password Generator")
win.configure(bg="beige")
win.geometry("500x500")
button=Button(win,text="Generate",command=gen)
button.place(x=150,y=150)

lowercase="abcdefghijklmnopqrstuvwxyz"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
spl="!@#$%^&*`~?₹"
password=""

def gen():
    for i in range(1,len(lowercase)+1):
        password=

win.mainloop()