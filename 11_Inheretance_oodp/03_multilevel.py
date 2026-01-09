class employee:
    a=1
class progammer(employee):
    b=69
class name(progammer):
    c = 45

c= employee()
print(c.a)
c= progammer()
print(c.b,c.a)
c= name()
print(c.c,c.b,c.a)