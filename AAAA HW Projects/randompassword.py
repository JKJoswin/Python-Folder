import tkinter
from tkinter import *
import random

def generate():
    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    spl="!@#$%^&*_-"
    password=""
    for i in range(random.randint(8,15)):
        choice=random.randint(0,3)
        print(choice)
        if choice==0:
            n=random.randint(0,25)
            password= password + lowercase[n]
        elif choice==1:
            n=random.randint(0,25)
            password= password + uppercase[n]
        elif choice==2:
            n=random.randint(0,9)
            password= password + spl[n]
        else:
            n=random.randint(0,0)
            password= password + numbers[n]
    
    f=("Courier",15,"bold")
    l1=Label(win,text="Your new password is "+password,font=f,bg="teal",relief="raised")
    l1.place(y=50)


win=Tk()
win.title("Password Generator")
win.configure(bg="beige")
win.geometry("400x300")
button=Button(win,text="Generate",relief="raised",command=generate)
button.pack(pady=10)




win.mainloop()