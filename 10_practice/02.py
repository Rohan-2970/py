# Write a class "calculator" capable of finding 
# square, cube and square root of a number.

class calculator:
    def __init__(self,n): #  it is a constuctor 
        self.n= n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
        
num = int(input("Enter a number : "))
a= calculator(num)

a.square()
a.cube()
a.squareroot()

'''
What is a Constructor?
A constructor is a special method in a class.

In Python, the constructor method is always named __init__.

It runs automatically when you create an object from the class.


 Why your __init__ is a constructor!!!!!!!!!!!!!!

def __init__ is always the constructor of the class.
Even if you leave it empty (pass), its still a constructor — it just isn’t doing any setup work.
Its different from a normal function because:
You dont call it manually (calc.__init__()), Python calls it when you create the object.
It is meant for initialization, not just any task.

'''


