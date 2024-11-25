file=open("calculator.txt","r")
print(file.read())
file.close()
print()


file2=open("calculator.txt","w")
file2.write("\n \n I am Joswin.")
file2.close()
print()


file3=open("calculator.txt","a")
file3.write("\n \n This is the whole content.")
file3.close()