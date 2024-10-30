class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,s):
        return "My name is " + self.name + ". My age is " + str(self.age) + ". I can sing " + s + "."
    def dance(self,d):
        return "My name is " + self.name + ". My age is " + str(self.age) + ". I can dance " + d + "."

p1=parrot("Candy",2)
print(p1.sing("Heal The World"))
print(p1.dance("Moonwalk"))
