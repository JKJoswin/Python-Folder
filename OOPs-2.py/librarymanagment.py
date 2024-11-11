class library:
    def __init__(self,list):
       self.booklist=list
    
    def addbook(self,bookn):
        self.booklist.append(bookn)
        print("Book Added!")
    
    def displaybooks(self,booklist):
        print("The books we have are- ")
        for i in self.booklist:
            print(i)



    print(input("1.Add Book \n 2.Lend Book \n 3.Return Book \n 4.Display Books"))
    