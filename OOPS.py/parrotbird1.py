class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=parrot("Candy",2)
p2=parrot("Rudy",3)
print(p1.species)
print("I am ",p1.name,". My age is ",p1.age,".")
print(p2.species)
print("I am ",p2.name,". My age is ",p2.age,".")