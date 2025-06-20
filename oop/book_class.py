#program with a Book class that uses specific magic methods to enhance its functionality. 
class Book:
    def __init__(self, title, author, year):
      self.title = title
      self.author = author
      self.year = year

#Display this information with a string representation
    def __str__(self):
       return f"{self.title} by {self.author}, published in {self.year}"

#Dislplay this information with official representation
    def __repr__(self):
       return f"Book('{self.title}', '{self.author}', {self.year})"
    
#Use a destructor for object deletion
    def __del__(self):
       print(f"Deleting {self.title}")