file=open("calculator.txt","r")
print(file.read())
file.close()
print()

file2=open("calculator.txt","w")
print(file2.write("Buenos dias!"))
file2.close()
print()

file3=open("calculator.txt","a")
print(file3.write(" Mucho gusto!"))
file3.close()
print()