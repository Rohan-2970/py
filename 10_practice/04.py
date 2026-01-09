# Add a static method in problem 2, to greet the user 
# with hello.

class calculator:
    def __init__(self,n): #  it is a constuctor 
        self.n= n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
    @staticmethod # when dont need instance class we donot need to access instance of calss 
    def hello():
        print("Hello World")    
num = int(input("Enter a number : "))
a= calculator(num)
a.hello()
a.square()
a.cube()
a.squareroot()
