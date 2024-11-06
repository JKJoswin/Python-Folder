class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print("First Name: ",self.fname)
        print("Last Name: ",self.lname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year=year
    def display_year(self):
        print("Graduation Year: ",self.year)

stud1=student("Joswin","Jayakumar",2035)
stud1.display()
stud1.display_year()