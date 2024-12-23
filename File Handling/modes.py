f=open("calculator.txt","r")
print(f.read())
f.close()

f1=open("calculator.txt","w")
f1.write("I like to play chess too!")
f1.close()

f3=open("calculator.txt","a")
f3.write("I also play basketball!")
f3.close()