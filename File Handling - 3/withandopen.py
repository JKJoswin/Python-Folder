with open("calculator.txt","w")as file1:
    file1.write("Hello! \nMy name is Joswin! \nI am going to turn 12 years old on 1st January!")

file1.close()

with open("calculatorupdated.txt","r")as file2:
    data=file2.readlines()
    for line in data:
        word=line.split()
        print(word)

file2.close()