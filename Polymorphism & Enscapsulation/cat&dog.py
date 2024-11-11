class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def info(self):
        print("My name is ",self.name,". I am ",self.age," years old.")
    
    def sound(self):
        print("I meow!")

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def info(self):
        print("My name is ",self.name,". I am ",self.age," years old.")
    
    def sound(self):
        print("I bark!")

catname=input("Enter Your Cat's Name: ")
catage=input("Enter Your Cat's Age: ")
cat1=cat(catname,catage)

dogname=input("Enter Your Dog's Name: ")
dogage=input("Enter Your Dog's Age: ")
dog1=dog(dogname,dogage)
for x in (cat1,dog1):
    x.info()
    x.sound()