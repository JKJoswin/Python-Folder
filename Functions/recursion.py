#recursion function
def f(num):
    if num==1:
        return num
    else:
        return num * f(num-1)

num=int(input("Enter The Number! "))
if num<0:
    print("There are no factorial for negative numbers!")
elif num==0:
    print("The factorial of 0 is 1.")
else:
    print("The factorial of ",num," is ",f(num),".")