class computer:
    def __init__(self):
        self.__max_price=75000
    
    def __display(self):
        print("The maximum price of the computer is",self.__max_price)
    
    def setmaxprice(self,price):
        self.__max_price=price
        self.__display()

comp1=computer()
comp1.setmaxprice(7500)