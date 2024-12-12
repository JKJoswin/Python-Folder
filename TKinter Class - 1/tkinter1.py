import tkinter
window1=tkinter.Tk()
window1.title("Graphical User Design -> GUD")
window1.geometry('500x400')

label1=tkinter.Label(window1,text="Hello! I am Joswin!")
button1=tkinter.Label(window1,text="Click Me!",bg="teal",fg="red")
entry1=tkinter.Entry()

label1.pack(pady=10)
button1.pack(pady=10)
entry1.pack(pady=10)

frame1=tkinter.Frame(window1,relief="sunken",width=200,height=100,border=5)
label2=tkinter.Label(frame1,text="My favorite football player is Pele!")
frame1.pack(pady=10)
label2.pack(pady=10)

window1.mainloop()