class person:
    def __init__(self,name,idno):
        self.name=name
        self.id=idno
    def display(self):
        print("Name: ",self.name)
        print("Id Number: ",self.id)
class employee(person):
    def __init__(self,name,idno,salary,post):
        person.__init__(self,name,idno)
        self.salary=salary
        self.post=post
    def display_emp(self):
        print("Salary: ",self.salary)
        print("Post: ",self.post)

emp=employee("Joswin",187,1000000000,"IT Engineer")
emp.display()
emp.display_emp()