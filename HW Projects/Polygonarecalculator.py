class arsq:
    def __init__(self,sides):
        self.s=sides
    
    def area(self):
        return pow(self.s,2)
    
class artri:   
    def __init__(self,sides):
        self.s=sides

    def area(self):
        return (self.s**2)/2

sqside=int(input("Enter The Side Of Square: "))
triside=int(input("Enter The Side Of Triangle: "))
sofsq=arsq(sqside)
softri=artri(triside)
for x in (sofsq,softri):
    print(x.area())