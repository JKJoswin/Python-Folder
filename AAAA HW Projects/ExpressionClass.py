class expression:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
num1=int(input("Number 1: "))
num2=int(input("Number 2: "))
exp1=expression(num1,num2)
print("1.Add \n 2.Subtract \n 3.Multiply")
choice=int(input("Enter Your Choice: "))
if choice==1 :
    print(exp1.add())
elif choice==2 :
    print(exp1.sub())
elif choice==3 :
    print(exp1.mul())
else:
    print("Invalid choice!")