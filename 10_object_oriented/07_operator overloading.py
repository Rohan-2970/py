# Abstraction  ----> implementation part nhi dikhare
# Encapsulation -----> data hiding to protect the object’s internal state from being modified unexpectedly.

#  underscore method -> dandor methods 
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)
