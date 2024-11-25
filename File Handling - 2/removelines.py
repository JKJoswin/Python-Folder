file1=open("calculator.txt","r")
file2=open("calculatorupdated.txt","w")


for lines in file1.readlines():
    if not(lines.startswith("K")):
        print(lines)
        file2.write(lines)

file1.close()
file2.close()

file=open("calculatorupdated.txt","r")
print(file.read())
file.close()