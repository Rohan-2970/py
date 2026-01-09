class Employee:# base class / parent class
    company = "ITC"
   
    def __init__(self,name,salary):
        self.name = name
        self.salary= salary
        
    def show(self):
        
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):   # derived class
    company = "ITC Infotech"

    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language = language

    def showLanguage(self):
        
        print(f"The name is {self.name} and he is good with {self.language} language")



a = Employee("rohan",4567)
b = Programmer("aryan",987,"python")

print(a.name , a.salary, b.language )
print(a.company, b.company)

a.show()
b.show()
b.showLanguage()
