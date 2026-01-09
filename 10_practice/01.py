# Create a Class "Programmer" for storing 
# information of few programmers working at Microsoft.

class Programmer:
   company = "Microsoft"
   def __init__(self, name , salary,pincode):
      self.name = name
      self.salary= salary
      self.pincode = pincode

p = Programmer("Rohan",1244555,65789)
print(p.name, p.salary,p.pincode)