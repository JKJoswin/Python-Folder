from abc import ABC,abstractmethod

class animal(ABC):
    @ abstractmethod

    def move():
        pass

class human(animal):
    def move(self):
        print("Human can walk and run.")

class snake(animal):
    def move(self):
        print("Snake can slither.")

#a=animal()
#a.move()
h=human()
s=snake()
h.move()
s.move()