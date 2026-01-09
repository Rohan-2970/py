# Create a class with a class attribute a; create an 
# object from it and set 'a' directly using 
# object.a = o. Does this change the class attribute?

class demo:
    a=4

o = demo()
print(o.a) # prints class attribute bec. instance atribute is not present
o.a=0 # Instance attributeis set
print(o.a) # prints instance attribute bec. it is prsent 
print(demo.a) # prints class attribute