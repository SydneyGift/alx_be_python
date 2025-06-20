#program to practice object oriented programming

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f"{self.name} has eaten"
    def sleep(self):
        return f"{self.name} is sleeping"
    
#Create a sub class called dog that inherits from animal

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

#Add a method bark
    def bark(self):
        print(f"The dog {self.name} of the breed {self.breed} says Woof!")

gui = Dog("Treb", "Labrador")
print(gui.eat())
print(gui.sleep())
gui.bark()