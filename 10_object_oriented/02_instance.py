class Employee:
    name= "Rohan"
    language ="py" # class attribute
    salary = 12345678

Rohan= Employee()
Rohan.language = "hindi"
print(Rohan.name, Rohan.language)

# class attributes take preference over calss attributes

