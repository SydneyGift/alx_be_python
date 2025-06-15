class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    #Create a method to display student information
    def get_student_info(self):
        print(f"Your name is {self.name} and you are {self.age} years old.")

student_1 = Student("Onyango", 13)
student_1.get_student_info()