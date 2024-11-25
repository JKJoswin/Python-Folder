file=open("calculator.txt","r")
print(file.read())
file.close()
print()


file2=open("calculator.txt","r")
print(file2.read(20))
file2.close()
print()


file3=open("calculator.txt","a")
file3.write("\n Hello! I am Joswin!")
file3.close()
print()