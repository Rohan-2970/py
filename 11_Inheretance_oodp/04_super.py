class employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1
class progammer(employee):
    def __init__(self):
        print("const. of programmer")
    b=69
class name(progammer):
    def __init__(self):
        super().__init__() # it is used to run the costructor ofof its parent 
        print("const. of name")
    
    c = 45

c= employee()
print(c.a)
c= progammer()
print(c.b,c.a)
c= name()
print(c.c,c.b,c.a)