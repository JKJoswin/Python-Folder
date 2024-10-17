def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

x=float(input("Enter The First Number! "))
y=float(input("Enter The Second Number! "))

print("By adding ",x," and ",y,", we get ",add(x,y))
print("By subtracting ",x," and ",y,", we get ",sub(x,y))
print("By multiplying ",x," and ",y,", we get ",mul(x,y))
print("By dividing ",x," and ",y,", we get ",div(x,y))