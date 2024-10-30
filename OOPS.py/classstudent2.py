class student:
    name="James"
    age=16

    def intro(self):
       print("I am a student!!!")

    def details(self):
       print("Name: ",self.name)
       print("Age: ",self.age)

obj=student()
obj.intro()
obj.details()