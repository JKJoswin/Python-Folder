f=open("calculator.txt","r")
print(f.read())
f.close()

f=open("calculator.txt","w")
f.write("I like to play chess too!")
f.close()

f=open("calculator.txt","a")
f.write("I also play basketball!")
f.close()