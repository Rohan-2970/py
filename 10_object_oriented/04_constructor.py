class Employee:
    name= "Rohan"
    language ="py" # class attribute
    salary = 12345678

# all dunder methods are not called only init dunder methods are called
    def __init__(self, name,salary,language):  # dunder method which is automatically called
       self.name = name
       self.salary = salary
       self.language = language
    print("I an creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}") 
    
    @staticmethod
    def greet(self):
        print("Good Morning")

Rohan= Employee("Rohan",1345678,"trdfgh")
# harry.language = "JavaScript" # This is an instance attribute
Rohan.name = "Rohan"
print(Rohan.name, Rohan.salary, Rohan.language)