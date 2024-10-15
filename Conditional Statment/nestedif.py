num=int(input("Enter A Number Greater Than 50! "))
if num>50:
    if num%2==0:
        print("The number ",num," is even!")
    else:
        print("The number ",num," is odd!")
else:
    print("The number ",num," is invalid!")