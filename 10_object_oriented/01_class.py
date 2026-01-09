# class -- blueprint of an object
class Employee:
    name= "Rohan"
    language ="py" # class attribute
    salary = 12345678

Rohan= Employee()
print(Rohan.name, Rohan.language)

harry=Employee()
harry.name = "uhfuifl" # instance attribute
print(harry.name,harry.language,harry.salary)
# name , language , salary --> attributes hai

# language , salary --> class attribute (because belong to a specific class)

# Here name is instance attribute and salary and 
# language are class attributes as they directly 
# belong to the class

# Instance Attribute	Data belonging to one specific object
# Object	A real, usable copy of a class