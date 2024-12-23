import tkinter
from tkinter import *
import random

win=Tk()
win.title("Password Generator")
win.configure(bg="beige")
win.geometry("400x300")
l1=Label(win,text="How many digits do you need?",relief="raised",bg="antique white")
l1.pack(pady=10)
e1=OptionMenu(win,"selected_option",6,7,8,9,10)
e1.pack(pady=10)
button=Button(win,text="Generate",relief="raised")
button.pack(pady=10)
lowercase="abcdefghijklmnopqrstuvwxyz"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
spl="!@#$%^&*`~?₹"



win.mainloop()