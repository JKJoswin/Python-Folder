file1=open("calculator.txt","r")
file2=open("calculatorupdated.txt","w")

cont=file1.readlines()
for i in range(1,len(cont)+1):
    if (i % 2 != 0):
        file2.write(cont[i-1])

file1.close()
file2.close()