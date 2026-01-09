class Employee:
    name= "Rohan"
    language ="py" # class attribute
    salary = 12345678
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}") 
    
    @staticmethod
    def greet(self):
        print("Good Morning")

Rohan= Employee()
# harry.language = "JavaScript" # This is an instance attribute
Rohan.greet()
Rohan.getInfo()
# Employee.getInfo(harry)
